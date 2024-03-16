import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
def bulk_send_email(sender_email, sender_password, receiver_email, subject, message,attachment_path):
    message_obj = MIMEMultipart()
    message_obj['From'] = sender_email
    message_obj['To'] = receiver_email
    message_obj['Subject'] = subject
    

    if attachment_path:
        attachment = open(attachment_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + os.path.basename(attachment_path))
        message_obj.attach(part)

    message_obj.attach(MIMEText(message, 'plain'))
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.set_debuglevel(1)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message_obj)
            print(f"Email sent successfully to {receiver_email}")

    except smtplib.SMTPAuthenticationError:
        print(f"Failed to authenticate with the SMTP server. Check your username/password.")
    except smtplib.SMTPConnectError:
        print(f"Failed to connect to the SMTP server. Check your network connection.")
    except smtplib.SMTPServerDisconnected:
        print(f"The SMTP server unexpectedly disconnected. Try again later.")
    except smtplib.SMTPRecipientsRefused:
        print(f"The recipient's email address was refused: {receiver_email}. Check the email address.")
    except smtplib.SMTPSenderRefused:
        print(f"The sender's email address was refused: {sender_email}. Check the email address.")
    except smtplib.SMTPDataError:
        print(f"The SMTP server refused to accept the message data.")
    except smtplib.SMTPException as e:
        print(f"An error occurred. Error: {str(e)}")
    except Exception as e:
        print(f"Failed to send email to {receiver_email}. Error: {str(e)}")
        print(f"SMTP Server Response: {e.smtp_error.decode()}")
        import traceback
        traceback.print_exc()

sender_email = 'senderemail@gmail.com' #replace with ethe sender email id
sender_password = 'password'  # replace with the application-specific password
subject = 'Invitation to Selection Test for UI/UX Designers at Cognifyr'


participants = {

  
'sender_email_id1','sender_email_id2'      #reciever email id list
}

message = f'''
Subject: Exciting Opportunity: Join Our Team at XYZ Corporation!

Dear [Candidate's Name],

We hope this email finds you well!

We are thrilled to inform you about an exciting opportunity at XYZ Corporation. Based on your impressive background and skills, we believe you could be a great addition to our team.

At XYZ Corporation, we are committed to innovation and excellence. As a leading company in our industry, we value individuals who are passionate, creative, and dedicated to making a difference.

Currently, we have openings for various positions, including software developers, marketing specialists, and customer service representatives. We are looking for talented individuals like you to join us in our mission to revolutionize the way businesses operate.

If you're interested in exploring this opportunity further, please reply to this email or visit our careers page at [XYZ Corporation Careers Page] to learn more about the available positions and how to apply.

We look forward to hearing from you and potentially welcoming you to our team at XYZ Corporation!

Best regards,

[Your Name]
Human Resources
XYZ Corporation

'''
attachment_path = r"C:\Users\XYZ\OneDrive\Desktop\attachment_path.pdf"  # Replace with the actual path to your attachment file

for email in participants:
    bulk_send_email(sender_email, sender_password, email, subject, message,attachment_path)


