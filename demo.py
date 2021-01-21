#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Splurket
"""
import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
username = "#Your Email Goes Here!"
password= "#Email Password Goes Here!"
imap_url = "imap.gmail.com"


def email():
    import email
    def clean(text):
        # clean text for creating a folder
        return "".join(c if c.isalnum() else "_" for c in text)
    def Yesemail():
        import smtplib, ssl
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        
        sender_email = "Your Email Goes Here!!"
        receiver_email = email
        password = "Email Password"
        
        message = MIMEMultipart("alternative")
        message["Subject"] = "Thanks For Participating In Our Demo For the 2021 Postman Galaxy Hackathon"
        message["From"] = sender_email
        message["To"] = receiver_email
        
        # Create the plain-text and HTML version of your message

        html = """\
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <body style="position: relative";>
        
           <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
                      <tr>
                        <td bgcolor="#65ba79" background="https://i.imgur.com/75qB6VW.jpg" alt="background" title="background" width="100%" height="400" align="center" valign="top"><!--[if gte mso 9]>
                        <v:rect xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false" style="width:600px; height:600px;">
                        <v:fill type="tile" src="https://i.imgur.com/75qB6VW.jpg" alt="background" title="background" color="#65ba79" />
                        <v:textbox inset="0,0,0,0">
                     <![endif]-->
        
                          <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr>
                              <td width="100%" align="center"><table cellpadding="0" cellspacing="0" border="0">
        
                                  <tr><center>
                                    <meta charset="UTF-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1.0" style="background-image: url('https://ci3.googleusercontent.com/proxy/oSHSvAKhBSdeEtI1ooeUQwjbJBctDJoPWitPYWBMw7XvcFYTbBNke9d2RpHaR2P6yeW8LNfm5EuZSyAAv-KI_6ggUeDNxGGr74kUR-YfJ6hkQw787qCxeoGXCzsxzCHASw=s0-d-e1-ft#https://lp.postman.com/rs/067-UMD-991/images/comp-api-hack-email-banner-2x.png')">
                                    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                    <title style="color:black;">Postman Hackathon 2021</title>
                                    <link href="https://fonts.googleapis.com/css?family=Karla:400,700&display=swap" rel="stylesheet">
        
                                </head>
                                
                                <body class="min-vh-100 d-flex flex-column">
                                
                                    <header>
                                        <div class="container">
                                                <a class="navbar-brand" href="#">
                                                    <img src="https://i.imgur.com/eSUsQZH.png" alt="Splurket Logo" style="display:block; padding-top:20px;"width="90" height="87" align="left"/>
                                                </a>
                                        </div>
                                    </header>
                                    <main class="my-auto">
                                        <div class="container">
                                            <h1 class="page-title" style="color:white; padding:10px;"><center>Thanks For Participating In Our Demo For The 2021 Postman Hackathon!</h1>
                                            <p class="page-description" style="color:black; text-align:center; background-color:white ;padding-left:20px; padding-right:20px; padding-top:20px; padding-bottom:20px">We Hope You Enjoyed Our Demo, And We Hope You'll Join Us In Our Anticipation To Win This Hackathon, And Move On To Greater Things!
                                            <br>
                                            <br>
                                            -The Splurket Team
                                            <br>
                                            Software Has No Limits
                                            <br>
                                            <br>
                                            P.S: Thanks For Believing In Us!.😉💯👍
                                
                                
                                            <center><p style="color:white">Join Us</p>
                                            <nav class="footer-social-links" style="display: inline-block; text-align: center; line-height: 40px; width: 40px; height: 40px; border-radius: 50%; background-color: #ffffff; color: #000000; margin-right: 16px; transition: all 0.3s ease-in-out;   margin-right: 0; text-decoration: none; background-color: #000000; color: #ffffff;"><center>
                                                <a href="https://twitter.com/Splurket_Store"><class="social-link"><i class="mdi mdi-twitter"></i></a>
                                                <a href="https://www.google.com/search?q=splurket&rlz=1C5CHFA_enUS916US916&oq=splurket&aqs=chrome.0.69i59j69i60l6.1950j1j9&sourceid=chrome&ie=UTF-8"><class="social-link"><i class="mdi mdi-google"></i></a>
                                                <a href="https://www.instagram.com/splurket_store/"><class="social-link"><i class="mdi mdi-instagram"></i></a>
                                                <a href="https://discord.gg/psPrHQnt5V"><class="social-link"><i class="mdi mdi-discord"></i></a>
                                             </p>
                                              <center><p style="color:white;">@Splurket_Store on all major platforms!</p><center>
                                            <center><p style="color:white;">Copyright 2021 Splurket. All Rights Reserved</p>
                                            </nav>
                                        </div>
                                    </main>
                                </body>
                                  </tr>
        
                                </table></td>
                            </tr>
                          </table>
        
                          <!--[if gte mso 9]>
                            </v:textbox>
                            </v:rect>
                            <![endif]--></td>
                      </tr>
                    </table>
        
        </body>
        </head>
        </html>
            """

        # Turn these into plain/html MIMEText objects
        part2 = MIMEText(html, "html")
        
        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
                )
    def Noemail():
        import smtplib, ssl
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        
        sender_email = "Your Email Address To send Email After Complete"
        receiver_email = email
        password = "Email Password"
        
        message = MIMEMultipart("alternative")
        message["Subject"] = "Thanks For Participating In Our Demo For the 2021 Postman Hackathon"
        message["From"] = sender_email
        message["To"] = receiver_email
        
        # Create the plain-text and HTML version of your message

        html = """\
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <body style="position: relative";>
        
           <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
                      <tr>
                        <td bgcolor="#65ba79" background="https://i.imgur.com/75qB6VW.jpg" alt="background" title="background" width="100%" height="400" align="center" valign="top"><!--[if gte mso 9]>
                        <v:rect xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false" style="width:600px; height:600px;">
                        <v:fill type="tile" src="https://i.imgur.com/75qB6VW.jpg" alt="background" title="background" color="#65ba79" />
                        <v:textbox inset="0,0,0,0">
                     <![endif]-->
        
                          <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
                            <tr>
                              <td width="100%" align="center"><table cellpadding="0" cellspacing="0" border="0">
        
                                  <tr><center>
                                    <meta charset="UTF-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1.0" style="background-image: url('https://ci3.googleusercontent.com/proxy/oSHSvAKhBSdeEtI1ooeUQwjbJBctDJoPWitPYWBMw7XvcFYTbBNke9d2RpHaR2P6yeW8LNfm5EuZSyAAv-KI_6ggUeDNxGGr74kUR-YfJ6hkQw787qCxeoGXCzsxzCHASw=s0-d-e1-ft#https://lp.postman.com/rs/067-UMD-991/images/comp-api-hack-email-banner-2x.png')">
                                    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                    <title style="color:black;">Postman Hackathon 2021</title>
                                    <link href="https://fonts.googleapis.com/css?family=Karla:400,700&display=swap" rel="stylesheet">
        
                                </head>
                                
                                <body class="min-vh-100 d-flex flex-column">
                                
                                    <header>
                                        <div class="container">
                                                <a class="navbar-brand" href="#">
                                                    <img src="https://i.imgur.com/eSUsQZH.png" alt="Splurket Logo" style="display:block; padding-top:20px;"width="90" height="87" align="left"/>
                                                </a>
                                        </div>
                                    </header>
                                    <main class="my-auto">
                                        <div class="container">
                                            <h1 class="page-title" style="color:white; padding:10px;"><center>Thanks For Participating In Our Demo For The 2021 Postman Hackathon!</h1>
                                            <p class="page-description" style="color:black; text-align:center; background-color:white ;padding-left:20px; padding-right:20px; padding-top:20px; padding-bottom:20px">We Hope You Enjoyed Our Demo, And We Hope You'll Join Us In Our Anticipation To Win This Hackathon, And Move On To Greater Things!
                                            <br>
                                            <br>
                                            -The Splurket Team
                                            <br>
                                            Software Has No Limits
                                            <br>
                                            <br>
                                            P.S: You Don't Think We Will Win.😉😭
                                
                                
                                            <center><p style="color:white">Join Us</p>
                                            <nav class="footer-social-links" style="display: inline-block; text-align: center; line-height: 40px; width: 40px; height: 40px; border-radius: 50%; background-color: #ffffff; color: #000000; margin-right: 16px; transition: all 0.3s ease-in-out;   margin-right: 0; text-decoration: none; background-color: #000000; color: #ffffff;"><center>
                                                <a href="https://twitter.com/Splurket_Store"><class="social-link"><i class="mdi mdi-twitter"></i></a>
                                                <a href="https://www.google.com/search?q=splurket&rlz=1C5CHFA_enUS916US916&oq=splurket&aqs=chrome.0.69i59j69i60l6.1950j1j9&sourceid=chrome&ie=UTF-8"><class="social-link"><i class="mdi mdi-google"></i></a>
                                                <a href="https://www.instagram.com/splurket_store/"><class="social-link"><i class="mdi mdi-instagram"></i></a>
                                                <a href="https://discord.gg/psPrHQnt5V"><class="social-link"><i class="mdi mdi-discord"></i></a>
                                             </p>
                                              <center><p style="color:white;">@Splurket_Store on all major platforms!</p><center>
                                            <center><p style="color:white;">Copyright 2021 Splurket. All Rights Reserved</p>
                                            </nav>
                                        </div>
                                    </main>
                                </body>
                                  </tr>
        
                                </table></td>
                            </tr>
                          </table>
        
                          <!--[if gte mso 9]>
                            </v:textbox>
                            </v:rect>
                            <![endif]--></td>
                      </tr>
                    </table>
        
        </body>
        </head>
        </html>
            """

        # Turn these into plain/html MIMEText objects
        part2 = MIMEText(html, "html")
        
        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
                )
    # create an IMAP4 class with SSL 
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    # authenticate
    imap.login(username, password)
            
    status, messages = imap.select("Inbox")
    # number of top emails to fetch
    N = 1
    # total number of emails
    messages = [messages[0]]
    str(messages).strip('[]')
    for mail in messages:
        _, msg = imap.fetch(mail, "(RFC822)")
        # you can delete the for loop for performance if you have a long list of emails
        # because it is only for printing the SUBJECT of target email to delete
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                
                subject = decode_header(msg["Subject"])[0][0]
                if isinstance(subject, bytes):
                    # if it's a bytes type, decode to str
                    subject = subject.decode()
                    #print("Deleting", subject)
                    # mark the mail as deleted
                        
    imap.store(mail, "+FLAGS", "\\Deleted")

    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    #Client_Secret.json generated by the google sheets API
    creds = ServiceAccountCredentials.from_json_keyfile_name('./client_secret.json', scope)
    client = gspread.authorize(creds)
    key="TRELLO API KEY"
    token="TRELLO TOKEN"
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("SHEET BEING OPENED").sheet1
    name=sheet.cell(subject,2).value
    email=sheet.cell(subject,3).value
    Sample=sheet.cell(subject,4).value
    if "Yes"in Sample or "yes" in Sample:
        #print('This is a Product Request')
        idList='#Trello List Id'
        #These are The variables Pulled from the google sheets
        Wanimal=sheet.cell(subject,5).value
        Rtype=sheet.cell(subject, 6).value
        url = ('https://api.trello.com/1/cards?key='+ key +'&token='+ token+'&idList='+ idList+'&name='+ name)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        r=response.text
        
        #print(r)
        chunks=r.split(',')
        #print(chunks)
        card_id= chunks[:1]
        hi=str(card_id)
        idlist=hi.split('"')
        #print(idlist)
        shit, more_shit,less_shit,cardid= idlist[:4]
        #print(cardid)
        url ='https://api.trello.com/1/checklists?key='+key+'&token='+token+'&idCard=' +cardid+ "&name=More Info about Form Response"  
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        hi1=response.text
        #print(hi1)
        #print(r)
        chunks=hi1.split(',')
        #print(chunks)
        checkid= chunks[:1]
        hi=str(checkid)
        idlist=hi.split('"')
        #print(idlist)
        shit, more_shit,less_shit,checklistid= idlist[:4]
        #print(checklistid)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name= Name:'+str(name)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name= Email:'+str(email)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name=Think we\'ll win?-'+str(Sample)
        payload = {}
        headers= {} 
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name=Favorite color:'+str(Rtype)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name=Favorite Animal:'+str(Wanimal)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        Yesemail()
        
        
    if "No" in Sample or "no" in Sample:
        #print('This is a Product Request')
        idList='#Trello List ID'
        #Variables pulled from google sheet
        Wanimal=sheet.cell(subject,5).value
        Rtype=sheet.cell(subject, 6).value
        url = ('https://api.trello.com/1/cards?key='+ key +'&token='+ token+'&idList='+ idList+'&name='+ name)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        r=response.text
        
        #print(r)
        chunks=r.split(',')
        #print(chunks)
        card_id= chunks[:1]
        hi=str(card_id)
        idlist=hi.split('"')
        #print(idlist)
        shit, more_shit,less_shit,cardid= idlist[:4]
        #print(cardid)
        url ='https://api.trello.com/1/checklists?key='+key+'&token='+token+'&idCard=' +cardid+ "&name=More Info about Form Response"  
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        hi1=response.text
        #print(hi1)
        #print(r)
        chunks=hi1.split(',')
        #print(chunks)
        checkid= chunks[:1]
        hi=str(checkid)
        idlist=hi.split('"')
        #print(idlist)
        shit, more_shit,less_shit,checklistid= idlist[:4]
        #print(checklistid)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name= Name:'+str(name)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name= Email:'+str(email)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name=Think we\'ll win?:'+str(Sample)
        payload = {}
        headers= {} 
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name=Favorite color:'+str(Rtype)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name=Favorite Animal:'+str(Wanimal)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        Noemail()
    if "Of Course" in Sample:
        #print('This is a Product Request')
        idList='Trello List ID'
        #Variables from Google sheet
        Wanimal=sheet.cell(subject,5).value
        Rtype=sheet.cell(subject, 6).value
        url = ('https://api.trello.com/1/cards?key='+ key +'&token='+ token+'&idList='+ idList+'&name='+ name)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        r=response.text
        
        #print(r)
        chunks=r.split(',')
        #print(chunks)
        card_id= chunks[:1]
        hi=str(card_id)
        idlist=hi.split('"')
        #print(idlist)
        shit, more_shit,less_shit,cardid= idlist[:4]
        #print(cardid)
        url ='https://api.trello.com/1/checklists?key='+key+'&token='+token+'&idCard=' +cardid+ "&name=More Info about Form Response"  
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        hi1=response.text
        #print(hi1)
        #print(r)
        chunks=hi1.split(',')
        #print(chunks)
        checkid= chunks[:1]
        hi=str(checkid)
        idlist=hi.split('"')
        #print(idlist)
        shit, more_shit,less_shit,checklistid= idlist[:4]
        #print(checklistid)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name= Name:'+str(name)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name= Email:'+str(email)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name=Think we\'ll win?:'+str(Sample)
        payload = {}
        headers= {} 
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name=Favorite color:'+str(Rtype)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name=Favorite Animal:'+str(Wanimal)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        Noemail()
    if "Never" in Sample:
        #print('This is a Product Request')
        #variables from Google sheet
        idList='Trello List ID'
        Wanimal=sheet.cell(subject,5).value
        Rtype=sheet.cell(subject, 6).value
        url = ('https://api.trello.com/1/cards?key='+ key +'&token='+ token+'&idList='+ idList+'&name='+ name)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        r=response.text
        
        #print(r)
        chunks=r.split(',')
        #print(chunks)
        card_id= chunks[:1]
        hi=str(card_id)
        idlist=hi.split('"')
        #print(idlist)
        shit, more_shit,less_shit,cardid= idlist[:4]
        #print(cardid)
        url ='https://api.trello.com/1/checklists?key='+key+'&token='+token+'&idCard=' +cardid+ "&name=More Info about Form Response"  
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        hi1=response.text
        #print(hi1)
        #print(r)
        chunks=hi1.split(',')
        #print(chunks)
        checkid= chunks[:1]
        hi=str(checkid)
        idlist=hi.split('"')
        #print(idlist)
        shit, more_shit,less_shit,checklistid= idlist[:4]
        #print(checklistid)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name= Name:'+str(name)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name= Email:'+str(email)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name=Think we\'ll win?:'+str(Sample)
        payload = {}
        headers= {} 
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name=Favorite color:'+str(Rtype)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name=Favorite Animal:'+str(Wanimal)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        Noemail()
while True:
    try:
        email()
        continue
    except: continue

