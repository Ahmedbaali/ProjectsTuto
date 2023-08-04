import requests
import xlwt
from xlwt import Workbook
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

BASE_URL = 'https://remoteok.com/api/'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'
#this agnet is for this PC(Linux Manjaro) for other system I have to change the agent
#can use this site 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
REQUEST_HEADER = {
    'User-Agent': USER_AGENT,
    'Accept-Language': 'en-US, en;q=0.5'
}

def get_job_posting():
    res = requests.get(url=BASE_URL, headers=REQUEST_HEADER)
    return res.json()





if __name__ == "__main__":
    json = get_job_posting()[1:]
    print(json)
