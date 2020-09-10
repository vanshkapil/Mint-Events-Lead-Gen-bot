## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there
- namaskar
- wassup
- namaste
- whats up
- hey How are you
- hello How are you
- hi there
- Hrllo

## intent:goodbye
- bye
- goodbye
- see you around
- see you later
- tata
- ok bye
- acha to hum chalte hain
- thanks, bye
- Stop
- End

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct
- yeah
- ya
- haan
- sahi

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really
- na
- naa
- nope

## intent:filler
- ok
- hmm
- acha
- good
- interesting
- wow
- Hehe
- Ok
- nothing

## intent:inform
- [9560833330](visitor_phone_number)
- my phone number is [9560833330](visitor_phone_number)
- [vansh@gmail.com](visitor_email)
- my email is [vansh@gmail.com](visitor_email)
- [va@gmail.com](visitor_email)
- [vansh@cmail.com](visitor_email)
- [vanshkapil@email.com](visitor_email)
- [sachi@gmail.com](visitor_email)
- [v@gmail.com](visitor_email)
- [sachin@gmail.com](visitor_email)
- [vansh](visitor_name)
- [vansh Kapil](visitor_name)
- [Sachin Tendulkar](visitor_name)
- I am [Robin Singh](visitor_name)
- my name is [sucheta](visitor_name)
- my email id is [vansh87493@gmail.com](visitor_email)
- [surbhi](visitor_name)
- [sourav duggal](visitor_name)
- [duggal](visitor_name)
- [tendulkar](visitor_name)
- [1234567890](visitor_phone_number)
- [9876543211](visitor_phone_number)
- [tendu@st.com](visitor_email)
- [babbar](visitor_name)
- [babbar singh](visitor_name)
- [9876543455](visitor_phone_number)
- [singh@babbar.com](visitor_email)
- [bilbo babins](visitor_name)
- [VVS Laxman](visitor_name)
- [don](visitor_name)
- [khgf@gmai.com](visitor_email)
- [9876543456](visitor_phone_number)
- [kapil](visitor_name)
- [8765432112](visitor_phone_number)
- [kap@cmail.com](visitor_email)
- Ganpat [Singh](visitor_name)
- [8765433336](visitor_phone_number)
- [gs@yahoo.com](visitor_email)

## intent:chitchat/ask_abuse
- bc
- behenchod
- kutte
- kamine
- bhosdike
- fuck
- dog
- harami
- lodu
- lund
- chut
- fuck you
- idiot
- stupid
- are you crazy
- who you fucking
- who fucked you.

## intent:chitchat/ask_bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?
- Who are you ?

## intent:exhibitions
- do you do [exhibitions](visitor_event_type)
- I want to enquire about [exhibitions](visitor_event_type)
- /exhibitions{"visitor_event_type":"exhibitions"}

## intent:weddings
- do you do [weddings](visitor_event_type)
- /weddings{"visitor_event_type":"weddings"}
- weddings
- do you do weddings

## intent:corporate
- do you do [corporate](visitor_event_type)
- /corporate{"visitor_event_type":"corporate"}

## intent:start
- start
- Start
- START
- start it

## intent:chitchat
- are you a bot

## regex:visitor_email
- [^@]+@[^@]+\.[^@]+

## regex:visitor_phone_number
- ^[6-9]\d{9}$
