
def send_email(user, pwd, recipient, subject, body):
    """
    Send mail using smtp.gmail.com

    :param user: who send mail
    :param pwd:  password from this mail
    :param recipient:  who get mail
    :param subject: title
    :param body: text
    :return:
    """

    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")
if __name__ == '__main__':

    user = 'superliv.no@gmail.com'
    pwd = '**********'
    recipient = 'sh.kiruh@gmail.com'
    subject = 'The contents of %s'
    body = 'text'

    send_email(user, pwd, recipient, subject, body)