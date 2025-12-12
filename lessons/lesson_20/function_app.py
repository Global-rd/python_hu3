#just a template code, follow recording for the full solution

import azure.functions as func
import logging
from email_sender import EmailSender
import os

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="frobotdreamspython3")
def frobotdreamspython3(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    email_sender = EmailSender(
        smtp_server=os.environ.get("GMAIL_SMTP_HOST"),
        smtp_port=os.environ.get("GMAIL_TLS_PORT"),
        sender_email=os.environ.get("GMAIL_EMAIL"),
        sender_password=os.environ.get("GMAIL_PW")
    )

    email_sender.send_email(recipients=["nigrushid@gmail.com"],
                            subject="Test Email",
                            body="Test",
                            attachments=["lessons/lesson_18/to_send.csv"])

    challenge = req.params.get("challenge")

    if challenge:
        return func.HttpResponse(challenge, status_code=200)
    
    return func.HttpResponse("All good!", status_code=200)