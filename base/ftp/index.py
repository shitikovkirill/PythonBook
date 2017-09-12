from ftplib import FTP

# domain name or server ip:
ftp = FTP('*******')
ftp.login(user='*****', passwd='*****')


# ftp.cwd('/whyfix/')

def grabFile(filename):
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)

    ftp.quit()
    localfile.close()


if __name__ == '__main__':
    grabFile('ACC_SOLD.CSV')