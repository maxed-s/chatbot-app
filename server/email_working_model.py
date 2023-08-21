from langchain.prompts import ChatPromptTemplate
from langchain.prompts.chat import SystemMessage, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI
from email.message import EmailMessage
from flask import jsonify
import json
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_ID = os.getenv("EMAIL_ID")
OPENAI_KEY = os.getenv("OPENAI_KEY")


def send_email(res):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    
    msg = EmailMessage()
    msg.set_content(f"{res['email_header']} \n\n {res['email_body']} \n\n {res['email_footer']}")

    msg['Subject'] = f"{res['subject']}"
    msg['From'] = EMAIL_ID
    msg['To'] = f"{res['email_to']}"

    s.login(EMAIL_ID, EMAIL_PASSWORD)

    s.send_message(msg)
    print("mail sent")

template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                """You are a helpful assistant that returns a dictonary/obejct that contains following things: 
                1. an email address mentioned in user text input with key name email_to
                2. appropriate subject name for which user asked you to create a mail with key name subject
                3. starting of a mail with key name email_header
                4. description about that topic for that user want to write a mail email_body
                5. email ending footer email_footer
                """
            )
        ),
        HumanMessagePromptTemplate.from_template("{text}"),
    ]
)

# template

llm = ChatOpenAI(openai_api_key=OPENAI_KEY)
res = llm(template.format_messages(text='send email from Aditya Raj to Atishay Jain whose email is atishayjain0314@gmail.com about a compnay named atishay that is masturbation and its good health effcts'))

result = json.loads(res.content)

print(result)

send_email(result)