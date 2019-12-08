from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC293eb75e040f4b3b7bac23a6a23b255b"
# Your Auth Token from twilio.com/console
auth_token  = "1dd041ca5e10cb4f41912a44596ba2c0"

client = Client(account_sid, auth_token)

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+5511963964336'

client.messages.create(body='Incidência: incêndio; Crítico; Area 3',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
