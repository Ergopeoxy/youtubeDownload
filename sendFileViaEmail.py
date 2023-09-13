import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

from dotenv import load_dotenv

# Load environment variables from the .env file senderEmail & emailAppPass
load_dotenv()



port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = os.getenv("senderEmail")  # Enter your address
receiver_email = os.getenv("senderEmail")
# str(input("what is your email?")) # Enter receiver address
password = os.getenv("emailAppPass")
print (password)
# inpupassword("Type your password and press enter: ")

# Create a multipart message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Mp3 sent. Save file as .mp3"

# Add the text message to the email
text = """\
This message is sent from Python."""
message.attach(MIMEText(text, "plain"))

# Attach the MP3 file
filename = str(input("What is your song name?"))    
mp3_filename = "mp3File/"+filename  # Replace with the actual filename
with open(mp3_filename, "rb") as mp3_file:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(mp3_file.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {mp3_filename}",
    )
    message.attach(part)

# Create a secure SSL context
context = ssl.create_default_context()

# Send the email
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
