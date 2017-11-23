import smtplib
from . import settings

host
port
username
password

email_conn = smtplib.SMTP(host, port)

email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)