#! python3
# myProject.py - python script to fetch current temperature of famous hill stations and send it to your Gmail account

"""
    File name: myProject.py
    Author: Mohammad Danish
    Date created: 12/09/2017
    Date last modified: 13/11/2017
    Python Version: 3.6
"""

import requests
import json
import smtplib

list_of_hillstation = ['Manali',
                       'Shimla',
                       'Mussoorie',
                       'Darjiling',
                       'Almora',
                       'Gangtok',
                       'Munnar',
                       'Ooty',
                       'Kodaikanal',
                       'Shillong',
                       'Ranikhet']

dispString = ''

# Get the data by calling the API and put it in an appropriate format.
for i in range(len(list_of_hillstation)):
    r = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?'
        'q=' + list_of_hillstation[i] + ',in&units=metric'
        '&APPID=<YOUR API KEY HERE>').json()            # Enter your API key here
    dispString += 'Current Temperature in ' + list_of_hillstation[i] + ' is ' + str(r['main']['temp']) + ' degree Celsius' + '\n'

#print(dispString)

# Method to send the acquired data to user's Gmail account.
def send_email(String):
    gmail_user = ''                    # Enter your email ID here
    gmail_pwd = ''                     # Enter password to your email ID
    FROM = ''                          # Email ID of sender
    TO = ''                            # Email ID of recipient
    SUBJECT = '-----Weather Info-----'
    TEXT = dispString

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

send_email(dispString)
