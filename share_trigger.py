#!/usr/bin/env python
# coding: utf-8


from bs4 import BeautifulSoup
import requests
import smtplib

#requesting the data from the Market platform
req=requests.get('https://www.borsaitaliana.it/borsa/etc-etn/scheda/GB00B15KXV33.html?lang=en')
r=req.text
soup = BeautifulSoup(r)

#Selecting the necessary data to be reported
openprice=float(soup.findAll("span", {"class": "t-text -right"})[0].text)
dayhigh=float(soup.findAll("span", {"class": "t-text -right"})[1].text)
daylow = float(soup.findAll("span", {"class": "t-text -right"})[2].text)
threshold=3.9703


#Setting the email settings
gmail_user = 'simonas.audickas@gmail.com'
gmail_password = 'svedas1234'
    
sent_from = "Simonas Audickas <simonas.audickas@gmail.com"
to = ['info@teipsiko.lt']

if float(openprice) >= threshold:
    
    subject = 'Geros Naujienos'
    body = 'Akciju atidarymo kaina virsijo '+str(threshold)+'\n\n'+'Akciju kaina dabar yra '+str(openprice)+'.\n'+'Akciju auksciausias dienos taskas '+str(dayhigh)+'\n'+"Akciju zemiausias dienos taskas "+str(daylow)+'\n'+'https://www.borsaitaliana.it/borsa/etc-etn/scheda/GB00B15KXV33.html?lang=en'
    email_text = """From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('Emailas issiustas')
    except:
        print ('Klaida...')
else:
    subject1 = 'Nieko gero del akciju'
    
    body1 = 'Akciju atidarymo kaina nevirsijo '+str(threshold)+'\n'+'Akciju kaina dabar yra '+str(openprice)+'.\n'+'Akciju auksciausias dienos taskas '+str(dayhigh)+'\n'+"Akciju zemiausias dienos taskas "+str(daylow)+'\n'+'https://www.borsaitaliana.it/borsa/etc-etn/scheda/GB00B15KXV33.html?lang=en'
            

    email_text1 = """From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject1, body1)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text1)
        server.close()

        print ('Emailas issiustas')
    except:
        print ('Klaida...')