import os
from twilio.rest import Client
import keys

ct = Client(keys.account_sid, keys.auth_token)

ct.messages.create(body= "You have a pending payment towards layout mantainance,\n Make sure to complete the same within the end of this month.\n -RWA",from_=keys.twilio_number,to=keys.target_number)

#print(message.body)