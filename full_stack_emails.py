import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os

# ----------------------------
# Load environment variables
# ----------------------------
load_dotenv()
sender_email = os.getenv("EMAIL_USER")
sender_password = os.getenv("EMAIL_PASS") 

# ----------------------------
# Read CSV file
# ----------------------------
df = pd.read_csv("hr_contacts.csv")
df.columns = df.columns.str.strip() 

print("Columns in CSV:", df.columns.tolist()) 

# ----------------------------
# Setup SMTP server
# ----------------------------
smtp_server = "smtp.gmail.com"
port = 587

try:
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_email, sender_password)
    print("✅ Logged in to SMTP server")
except Exception as e:
    print(f"Failed to connect/login to SMTP: {e}")
    exit()

# ----------------------------
# Loop through HR contacts
# ----------------------------
for index, row in df.iterrows():
    name = str(row["Name"]).strip()
    email = str(row["Email"]).strip()
    company = str(row["Company"]).strip()

    # ----------------------------
    # Email content
    # ----------------------------
    subject = f"Job Application And Interview Request For Full (MERN) stack Developer Position"
    body = f"""
Hiii  Good morning mam,
Greetings of the day.
As an IT professional with over 2.6+ years of experience in the fields of software development , I believe I have the qualification and skills necessary to excel in this role.

In my most recent role at Quadb tech pvt ltd, I worked as a full stack web developer, where I was responsible for creating a fully dynamic E commerce, accounting & CRM website with very smoothness. I am highly motivated and able to work effectively under presure, both independently and as a part of my team. My ability to collaborate with colleagues and communicate complex technical information clearly allows me to ensure that developments are resolved quickly and efficiently.

In addition to my experience, I possess a strong set of technical skills , including skills , including expertise in various programming languages . I am also proficient in Windows and Linux operating systems . Moreover , I hold a certificate  Full stack developer from Ducat-India.

Thank you! Regards
Anish Singh Rawat
"""
    # ----------------------------
    # Create email message
    # ----------------------------
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # ----------------------------
    # Optional: Attach resume
    # ----------------------------
    filename = "Anish Full stack Developer 2 Year 2026.pdf"
    if os.path.exists(filename):
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        msg.attach(part)

    try:
        server.sendmail(sender_email, email, msg.as_string())
        print(f"✅ Email sent to {name} ({email})")
    except Exception as e:
        print(f"❌ Failed to send email to {email}: {e}")


server.quit()
print("✅ All emails processed, server connection closed")
