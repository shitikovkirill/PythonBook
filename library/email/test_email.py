from __future__ import absolute_import
import unittest
import email.utils

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText


class TestEmailMethods(unittest.TestCase):

    def test_my_exception(self):
        """SMTP, POP3, IMAP сервер: mail.ukraine.com.ua
            Порт SMTP сервера: 25 или 2525 или 465 (SMTP+SSL)
            Порт POP3 сервера: 110 или 995 (POP3+SSL)
            Порт IMAP сервера: 143 или 993 (IMAP4+SSL)
            mailer_host: mail.ukraine.com.ua
            mailer_user: admin@xxx
            mailer_password: ********
        :return: 
        """
        # Create a text/plain message
        message = 'text'
        msg = MIMEText(message)

        # me == the sender's email address
        me = 'admin@xxxx'
        # you == the recipient's email address
        you = 'sh.kiruh2@gmail.com'
        host = 'mail.ukraine.com.ua'
        port = 25
        username = 'admin@xxxx'
        password = '**********'

        msg['Subject'] = 'The contents of %s' % message
        msg['From'] = me
        msg['To'] = you

        # Send the message via our own SMTP server, but don't include the
        # envelope header.

        server = smtplib.SMTP(host, port)

        server.starttls()
        server.login(username, password)

        server.sendmail(me, [you], msg.as_string())
        server.quit()

if __name__ == '__main__':
    unittest.main()
