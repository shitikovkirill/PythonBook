import smtplib
import re
import time
from os import listdir
from os.path import isfile, join, getctime, dirname, realpath


class SendErrorAlarm:

    __fileobject = None
    __user = None
    __password = None
    __recipient = None
    __archive_file_path = None

    def __init__(self, user, pwd, recipient):
        """

        :param user: who send mail
        :param pwd:  password from this mail
        :param recipient:  who get mail
        """
        self.__user = user
        self.__password = pwd
        self.__recipient = recipient if type(recipient) is list else [recipient]
        self.__archive_file_path = dirname(realpath(__file__))+'/'

    def send_email(self, subject, body):
        """
        Send mail using smtp.gmail.com
        :param subject: title
        :param body: text
        :return:
        """
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (self.__user, ", ".join(self.__recipient), subject, body)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(self.__user, self.__password)
            server.sendmail(self.__user, self.__recipient, message)
            server.close()
            print('successfully sent the mail')
        except:
            print("failed to send mail")

    def get_log_file(self, log_file):
        """
        Create generator to iterator in log file
        :param log_file: path to log file
        :return: string (line from log file) and fileobject
        """
        with open(log_file) as fileobject:
            self.__fileobject = fileobject
            for line in fileobject:
                yield line

    def close_log_file(self):
        if self.__fileobject:
            self.__fileobject.close()

    @staticmethod
    def grep_error(log_line, error_msg='production.ERROR:'):
        """
        Find in string error message.
        :param log_line: string = line from log file
        :param error_msg: string which you find in log file
        :return: boolean
        """
        if re.search(error_msg, log_line):
            return True
        return False

    @staticmethod
    def get_list_file(dir_path):
        """
        get list of file sorted by modification time
        :param dir_path:
        :return: list of file
        """
        files = [dir_path + f for f in listdir(dir_path) if isfile(join(dir_path, f))]
        files = sorted(files, key=lambda file: getctime(file), reverse=True)
        return files

    def first_error(self, line_str, archive_file='archive.log'):
        file_path = self.__archive_file_path+archive_file
        if isfile(file_path):
            file = open(file_path, "r+")
            for line in file:
                if line.strip() == line_str.strip():
                    return False
            file.write(line_str)
            file.close()
            return True
        else:
            file = open(file_path, "w+")
            file.close()
            return self.first_error(line_str, archive_file)

if __name__ == '__main__':
    user = '********'
    pwd = '*******'
    recipient = '*******'
    subject = "subject"
    body = """Text

Error: 
    """

    grep = SendErrorAlarm(user, pwd, recipient)
    file_list = grep.get_list_file('/home/kirill/Programming/Python/Book/library/email/')
    if file_list:
        print (file_list[0])
        for line in grep.get_log_file(file_list[0]):
            error = grep.grep_error(line, 'ProcessTimedOutException')
            if error and grep.first_error(line):
                grep.close_log_file()
                print line
                grep.send_email(subject, body+line+'\n In log file = '+file_list[0])
                break
    grep.close_log_file()
