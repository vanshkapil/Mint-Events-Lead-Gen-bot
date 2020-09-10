from typing import Any, Text, Dict, List
import json
from rasa_sdk.events import AllSlotsReset
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk.forms import FormAction
import csv
import random
import pandas
import re

INTENT_DESCRIPTION_MAPPING_PATH = "actions/intent_mapping.csv"

class visitorForm(FormAction):

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "visitor_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["visitor_name","visitor_phone_number","visitor_email","visitor_event_type"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"visitor_name": self.from_text(intent="inform"),
                "visitor_phone_number": self.from_entity(entity="visitor_phone_number", intent=["inform"]),
                "visitor_email": self.from_entity(entity="visitor_email", intent=["inform"]),
                "visitor_event_type": self.from_entity(entity="visitor_event_type",intent=["inform", "corporate", "weddings", "exhibitions"])
                }



    def validate_visitor_email(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate email value."""

        if re.match(r"[^@]+@[^@]+\.[^@]+",value):
            return {"visitor_email": value}
        else:
            dispatcher.utter_message(template="utter_wrong_visitor_email")
            return {"visitor_email": None}

    def validate_visitor_phone_number(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate email value."""

        if re.match(r"^[6-9]\d{9}$",value):
            return {"visitor_phone_number": value}
        else:
            dispatcher.utter_message(template="utter_wrong_phone_number")
            return {"visitor_phone_number": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(text="Thanks")
        return []


class Actioneventwelcome(Action):
    def name(self) -> Text:
        return "action_eventwelcome"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        value = tracker.get_slot('visitor_event_type')
        if value == 'weddings':
            dispatcher.utter_message(template="utter_wedding_ack")
            dispatcher.utter_message(template="utter_request_question")
            return None
        elif value == 'corporate':
            dispatcher.utter_message(template="utter_corporate_ack")
            dispatcher.utter_message(template="utter_request_question")
            return None
        elif value == 'exhibitions':
            dispatcher.utter_message(template="utter_exhibitions_ack")
            dispatcher.utter_message(template="utter_request_question")
            return None




class ActionDefaultAskAffirmation(Action):
    """Asks for an affirmation of the intent if NLU threshold is not met."""

    def name(self) -> Text:
        return "action_default_ask_affirmation"

    def __init__(self) -> None:
        import pandas as pd

        self.intent_mappings = pd.read_csv(INTENT_DESCRIPTION_MAPPING_PATH)
        self.intent_mappings.fillna("", inplace=True)
        self.intent_mappings.entities = self.intent_mappings.entities.map(
            lambda entities: {e.strip() for e in entities.split(",")}
        )

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) :

        intent_ranking = tracker.latest_message.get("intent_ranking", [])
        if len(intent_ranking) > 1:
            diff_intent_confidence = intent_ranking[0].get(
                "confidence"
            ) - intent_ranking[1].get("confidence")
            if diff_intent_confidence < 0.2:
                intent_ranking = intent_ranking[:2]
            else:
                intent_ranking = intent_ranking[:1]

        # for the intent name used to retrieve the button title, we either use
        # the name of the name of the "main" intent, or if it's an intent that triggers
        # the response selector, we use the full retrieval intent name so that we
        # can distinguish between the different sub intents
        first_intent_names = [
            intent.get("name", "")
            if intent.get("name", "") not in ["out_of_scope", "faq", "chitchat"]
            else tracker.latest_message.get("response_selector")
            .get(intent.get("name", ""))
            .get("full_retrieval_intent")
            for intent in intent_ranking
        ]

        message_title = (
            "Sorry, I'm not sure I've understood " "you correctly 🤔 Do you mean..."
        )

        entities = tracker.latest_message.get("entities", [])
        entities = {e["entity"]: e["value"] for e in entities}

        entities_json = json.dumps(entities)

        buttons = []
        for intent in first_intent_names:
            button_title = self.get_button_title(intent, entities)
            if "/" in intent:
                # here we use the button title as the payload as well, because you
                # can't force a response selector sub intent, so we need NLU to parse
                # that correctly
                buttons.append({"title": button_title, "payload": button_title})
            else:
                buttons.append(
                    {"title": button_title, "payload": f"/{intent}{entities_json}"}
                )

        buttons.append({"title": "Something else", "payload": "/out_of_scope"})

        dispatcher.utter_message(text=message_title, buttons=buttons)

        return []

    def get_button_title(self, intent: Text, entities: Dict[Text, Text]) -> Text:
        default_utterance_query = self.intent_mappings.intent == intent
        utterance_query = (self.intent_mappings.entities == entities.keys()) & (
            default_utterance_query
        )

        utterances = self.intent_mappings[utterance_query].button.tolist()

        if len(utterances) > 0:
            button_title = utterances[0]
        else:
            utterances = self.intent_mappings[default_utterance_query].button.tolist()
            button_title = utterances[0] if len(utterances) > 0 else intent

        return button_title.format(**entities)