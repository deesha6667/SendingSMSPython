import twilio.rest

# importing twilio

from twilio.rest import Client

account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

auth_token = 'your_auth_token'

client = Client(account_sid, auth_token)

message = client.messages.create(

from_=‘Twilio trial number',

body =‘your message',

to =‘whom you are sending this message'

)

print(“Your message has been sent”)

print(message.sid)
