from twilio.rest import Client

# Twilio hesap bilgilerini ayarlayın
account_sid = 'AC62a4f6b764547d81079d80742c1e17a8'
auth_token = '6bc8038c54463a182eb3a131aa62b2f4'
client = Client(account_sid, auth_token)

# Mesaj gönderme işlemi
message = client.messages.create(
    body='Merhaba, bu bir test mesajıdır!',
    from_='+16205368159',
    to='+97433860678'
)

# Mesajı doğrulayın
print(message.sid)
