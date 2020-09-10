## say goodbye
* start
  - utter_greet
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## formHappyPath
* start
   - utter_greet
   - visitor_form
   - form{"name":"visitor_form"}
   - form{"name":null}
   - action_eventwelcome

## formunhappypath
* start
   - utter_greet
   - visitor_form
   - form{"name":"visitor_form"}
* corporate
   - visitor_form
   - form{"name":null}
   - action_eventwelcome


## interactive_story_8
* start
    - utter_greet
    - visitor_form
    - form{"name": "visitor_form"}
    - slot{"requested_slot": "visitor_name"}

## interactive_story_9
* start
    - utter_greet
    - visitor_form
    - form{"name": "visitor_form"}
    

## interactive_story_10
* start
    - utter_greet
    - visitor_form
    - form{"name": "visitor_form"}
    - slot{"requested_slot": "visitor_name"}

## interactive_story_11
* start
    - utter_greet
    - visitor_form
    - form{"name": "visitor_form"}
    - slot{"requested_slot": "visitor_name"}

## interactive_story_12
* start
    - utter_greet
    - visitor_form
    - form{"name": "visitor_form"}
    - slot{"requested_slot": "visitor_name"}

## interactive_story_13
* start
    - utter_greet
    - visitor_form
    - form{"name": "visitor_form"}
    - slot{"requested_slot": "visitor_name"}

## chitchatunhappypath
* start
  - utter_greet
  - visitor_form
  - form{"name":"visitor_form"}
* chitchat
  - respond_chitchat    
  - visitor_form
  - form{"name":null}
  - action_eventwelcome

## formunhappypath
* start
   - utter_greet
   - visitor_form
   - form{"name":"visitor_form"}
* weddings
   - visitor_form
   - form{"name":null}
   - action_eventwelcome

## formunhappypath
* start
   - utter_greet
   - visitor_form
   - form{"name":"visitor_form"}
* exhibitions
   - visitor_form
   - form{"name":null}
   - action_eventwelcome

## interactive_story_1
* start
    - utter_greet
    - visitor_form
    - form{"name": "visitor_form"}
    - slot{"requested_slot": "visitor_name"}
* form: inform{"visitor_name": "vansh"}
    - slot{"visitor_name": "vansh"}
    - form: visitor_form
    - slot{"visitor_name": "vansh"}
    - slot{"requested_slot": "visitor_phone_number"}
* form: inform{"visitor_phone_number": "9876543211"}
    - slot{"visitor_phone_number": "9876543211"}
    - form: visitor_form
    - slot{"visitor_phone_number": "9876543211"}
    - slot{"requested_slot": "visitor_email"}
* form: inform{"visitor_email": "vansh@gmail.com"}
    - slot{"visitor_email": "vansh@gmail.com"}
    - form: visitor_form
    - slot{"visitor_email": "vansh@gmail.com"}
    - slot{"requested_slot": "visitor_event_type"}
    - slot{"visitor_event_type": "weddings"}
    - form: visitor_form
    - slot{"visitor_email": "vansh@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_eventwelcome

## interactive_story_2
* start
    - utter_greet
    - visitor_form
    - form{"name": "visitor_form"}
    - slot{"requested_slot": "visitor_name"}
* form: inform{"visitor_name": "vansh"}
    - slot{"visitor_name": "vansh"}
    - form: visitor_form
    - slot{"visitor_name": "vansh"}
    - slot{"requested_slot": "visitor_phone_number"}
* form: inform{"visitor_phone_number": "9876543211"}
    - slot{"visitor_phone_number": "9876543211"}
    - form: visitor_form
    - slot{"visitor_phone_number": "9876543211"}
    - slot{"requested_slot": "visitor_email"}
* form: inform{"visitor_email": "vansh@gmail.com"}
    - slot{"visitor_email": "vansh@gmail.com"}
    - form: visitor_form
    - slot{"visitor_email": "vansh@gmail.com"}
    - slot{"requested_slot": "visitor_event_type"}
    - slot{"visitor_event_type": "corporate"}
    - form: visitor_form
    - slot{"visitor_email": "vansh@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_eventwelcome

## interactive_story_3
* start
    - utter_greet
    - visitor_form
    - form{"name": "visitor_form"}
    - slot{"requested_slot": "visitor_name"}
* form: inform{"visitor_name": "vansh"}
    - slot{"visitor_name": "vansh"}
    - form: visitor_form
    - slot{"visitor_name": "vansh"}
    - slot{"requested_slot": "visitor_phone_number"}
* form: inform{"visitor_phone_number": "9876543211"}
    - slot{"visitor_phone_number": "9876543211"}
    - form: visitor_form
    - slot{"visitor_phone_number": "9876543211"}
    - slot{"requested_slot": "visitor_email"}
* form: inform{"visitor_email": "vansh@gmail.com"}
    - slot{"visitor_email": "vansh@gmail.com"}
    - form: visitor_form
    - slot{"visitor_email": "vansh@gmail.com"}
    - slot{"requested_slot": "visitor_event_type"}
    - slot{"visitor_event_type": "exhibitions"}
    - form: visitor_form
    - slot{"visitor_email": "vansh@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_eventwelcome

## interactive_story_4
* start
    - utter_greet
    - visitor_form
    - form{"name": "visitor_form"}
    - slot{"requested_slot": "visitor_name"}
    - slot{"visitor_event_type": "weddings"}
    - utter_wedding_ack
    - visitor_form
    - slot{"requested_slot": "visitor_name"}
* form: inform{"visitor_name": "kapil"}
    - slot{"visitor_name": "kapil"}
    - form: visitor_form
    - slot{"visitor_name": "kapil"}
    - slot{"requested_slot": "visitor_phone_number"}
* form: inform{"visitor_phone_number": "8765432112"}
    - slot{"visitor_phone_number": "8765432112"}
    - form: visitor_form
    - slot{"visitor_phone_number": "8765432112"}
    - slot{"requested_slot": "visitor_email"}
* form: inform{"visitor_email": "kap@cmail.com"}
    - slot{"visitor_email": "kap@cmail.com"}
    - form: visitor_form
    - slot{"visitor_email": "kap@cmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_eventwelcome

## interactive_story_5
* start
    - utter_greet
    - visitor_form
    - form{"name": "visitor_form"}
    - slot{"requested_slot": "visitor_name"}
    - slot{"visitor_event_type": "corporate"}
    - utter_corporate_ack
    - visitor_form
    - slot{"requested_slot": "visitor_name"}
* form: inform{"visitor_name": "kapil"}
    - slot{"visitor_name": "kapil"}
    - form: visitor_form
    - slot{"visitor_name": "kapil"}
    - slot{"requested_slot": "visitor_phone_number"}
* form: inform{"visitor_phone_number": "8765432112"}
    - slot{"visitor_phone_number": "8765432112"}
    - form: visitor_form
    - slot{"visitor_phone_number": "8765432112"}
    - slot{"requested_slot": "visitor_email"}
* form: inform{"visitor_email": "kap@cmail.com"}
    - slot{"visitor_email": "kap@cmail.com"}
    - form: visitor_form
    - slot{"visitor_email": "kap@cmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_eventwelcome

## interactive_story_6
* start
    - utter_greet
    - visitor_form
    - form{"name": "visitor_form"}
    - slot{"requested_slot": "visitor_name"}
    - slot{"visitor_event_type": "exhibitions"}
    - utter_exhibitions_ack
    - visitor_form
    - slot{"requested_slot": "visitor_name"}
* form: inform{"visitor_name": "kapil"}
    - slot{"visitor_name": "kapil"}
    - form: visitor_form
    - slot{"visitor_name": "kapil"}
    - slot{"requested_slot": "visitor_phone_number"}
* form: inform{"visitor_phone_number": "8765432112"}
    - slot{"visitor_phone_number": "8765432112"}
    - form: visitor_form
    - slot{"visitor_phone_number": "8765432112"}
    - slot{"requested_slot": "visitor_email"}
* form: inform{"visitor_email": "kap@cmail.com"}
    - slot{"visitor_email": "kap@cmail.com"}
    - form: visitor_form
    - slot{"visitor_email": "kap@cmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_eventwelcome

    
## interactive_story_7
* start
    - utter_greet
    - visitor_form
    - form{"name": "visitor_form"}
    - slot{"requested_slot": "visitor_name"}
    - slot{"visitor_name": "Ganpat Singh"}
    - visitor_form
    - slot{"requested_slot": "visitor_phone_number"}
* chitchat
    - respond_chitchat
    - visitor_form
    - slot{"requested_slot": "visitor_phone_number"}
* form: inform{"visitor_phone_number": "8765433336"}
    - slot{"visitor_phone_number": "8765433336"}
    - form: visitor_form
    - slot{"visitor_phone_number": "8765433336"}
    - slot{"requested_slot": "visitor_email"}
* form: inform{"visitor_email": "gs@yahoo.com"}
    - slot{"visitor_email": "gs@yahoo.com"}
    - form: visitor_form
    - slot{"visitor_email": "gs@yahoo.com"}
    - slot{"requested_slot": "visitor_event_type"}
* form: exhibitions{"visitor_event_type": "exhibitions"}
    - slot{"visitor_event_type": "exhibitions"}
    - form: visitor_form
    - slot{"visitor_event_type": "exhibitions"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_eventwelcome


