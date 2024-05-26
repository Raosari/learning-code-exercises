from email.message import EmailMessage
import smtplib
import json

def set_email_content(email,about):
    user = email.split("@")[0]
    name = "".join(char for char in user if char.isalpha())
    content = f"""Hi {name}, thank you for reaching out to me through my portfolio website.\nI appreciate your interest and will do my best to respond promptly as soon as possible about "{about}" that you indicated me.\n\nIn the meantime, feel free to explore more of my work on the site.\n\n\nKind regards, Raosari Garcia"""
    if not about:
        content = content.replace(' about "" that you indicated me',"")
    return content

def send_email(email_to_contact, subject = ""):
    try:
        email = EmailMessage()
        email['from'] = 'Raosari Garcia'
        email['to'] = email_to_contact
        email['subject'] = 'Thanks for contacting me'
        
        text_email = set_email_content(email_to_contact, subject)
        email.set_content(text_email)

        with open('./config.json') as config_file:
            try:
                config_data = json.load(config_file)
                email_address = config_data.get("email_address")
                app_password = config_data.get("app_password")
            except json.JSONDecodeError as json_error:
                raise ValueError(f'Error decoding JSON in config file: {json_error}')

        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            try:
                smtp.login(email_address,app_password)
                smtp.send_message(email)
            except smtplib.SMTPAuthenticationError:
                raise ValueError('SMTP Authentication failed. Check email address and app password.')
    except Exception as e:
        return f'Email not sent. Error: {str(e)}'


send_email("mraosari@gmail.com")