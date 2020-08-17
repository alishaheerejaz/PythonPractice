from twilio.rest import Client

account_sid = "***************"
auth_token = "**********************"
client = Client(account_sid, auth_token)

call = client.messages.create(to="+971544******", from_="+1334******", body="This is first message from twilio")
