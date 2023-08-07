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
#USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'#this agent in manjaro linux PC
#this agnet is for this PC(Linux Manjaro) for other system I have to change the agent
#can use this site 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0'#this agent in windows PC
REQUEST_HEADER = {
    'User-Agent': USER_AGENT,
    'Accept-Language': 'en-US, en;q=0.5'
}

def get_job_posting():
    res = requests.get(url=BASE_URL, headers=REQUEST_HEADER)
    return res.json()

def output_jobs_to_xls(data):
    wb = Workbook()
    job_sheet = wb.add_sheet('Jobs')
    headers = list(data[0].keys())
    for i in range(len(headers)):
        job_sheet.write(0,i,headers[i])
    for i in range(len(data)):
        job = data[i]
        values = list(job.values())
        for x in range(len(values)):
            job_sheet.write(i+1,x,values[x])
    wb.save('ScrapeAPI/remote_jobs.xls')




if __name__ == "__main__":
    json = get_job_posting()[1:]
    #print(json)
    output_jobs_to_xls(json)
    print('done!!')
