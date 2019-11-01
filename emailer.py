import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER_EMAIL = "from@email.com"
SENDER_PASS = "password"
SENDER_SMTP = "smtp.email.com"

def Email(target, subject, contents):
    msg = MIMEMultipart('alternative')
    msg['From'] = SENDER_EMAIL
    msg['To'] = target
    msg['Subject'] = subject
    #text = MIMEText(contents, 'text')
    html = MIMEText(contents, 'html')
    #msg.attach(text)
    msg.attach(html)

    s = smtplib.SMTP(SENDER_SMTP)
    s.ehlo()
    s.starttls()
    s.login(SENDER_EMAIL, SENDER_PASS)
    s.sendmail(SENDER_EMAIL, TARGET_EMAIL, msg.as_string())
    s.quit()