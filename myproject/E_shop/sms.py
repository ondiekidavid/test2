import africastalking

username = "sandbox"
api_key = "[4a4dcac8f1197fe7fb9e6547c38d96da64389d1f91a20e245f2a43e27a63d980]"
africastalking.initialize(username, api_key)


def send(self):
    # Set the numbers in international format
    recipients = ["+254746113037"]
    # Set your message
    message = "Thank you for your order!";
    # Set your shortCode or senderId
    sender = "TECH"
    try:
        response = self.sms.send(message, recipients, sender)
        print(response)
    except Exception as e:
        print(f'Customer, we have a problem: {e}')
