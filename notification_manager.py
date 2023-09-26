import smtplib


class NotificationManager:

    def __init__(self):
        self.client = YOUR_EMAIL
        self.mail_key = EMAIL_SEC_KEY

    def send_sms(self, message):
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=self.client, password=self.mail_key)
        connection.sendmail(
            from_addr=self.client,
            to_addrs=RECIEVING_EMAIL,
            msg=f"SUBJECT: Flights this month!\n\n{message.encode('utf-8')}"
        )
        # Prints if successfully sent.
        print(message)
