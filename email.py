import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

sender_email = "your_email@gmail.com"
receiver_email = "recipient@example.com"
password = "your_app_password"

# Create email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Email with Attachment"

# Attach body
body = "Please find the attachment."
message.attach(MIMEText(body, "plain"))

# Attach file
filename = "example.pdf"
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)
part.add_header("Content-Disposition", f"attachment; filename={filename}")
message.attach(part)

# Send email
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email with attachment sent successfully!")
except Exception as e:
    print(f"Error: {e}")
