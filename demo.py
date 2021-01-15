#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 14:17:59 2020

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
username = "splurket2trellodemo@gmail.com"
password= "Postmandemo"
imap_url = "imap.gmail.com"


def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)

# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# authenticate
imap.login(username, password)

status, messages = imap.select("Inbox")
# number of top emails to fetch
N = 1
# total number of emails
messages = int(messages[0])
for i in range(messages, messages-N, -1):
    # fetch the email message by ID
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])
            # decode the email subject
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                # if it's a bytes, decode to str
                subject = subject.decode(encoding)
            # decode email sender
            From, encoding = decode_header(msg.get("From"))[0]
            if isinstance(From, bytes):
                From = From.decode(encoding)
            #print("Subject:", subject)
           # print("From:", From)
            # if the email message is multipart
            if msg.is_multipart():
                # iterate over email parts
                for part in msg.walk():
                    # extract content type of email
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # get the email body
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        # use creds to create a client to interact with the Google Drive API
                        scope = ['https://spreadsheets.google.com/feeds',
                                 'https://www.googleapis.com/auth/drive']
                        creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/dylanclayton/Desktop/sheets2trello/client_secret.json', scope)
                        client = gspread.authorize(creds)

                        key="aa8ab2f4e1bf7b8f82f74196837c7d07"
                        token="21ac30700a5b6e3e7896973437807791ffc0955c6d7902df82f7d804a9ae5043"
                        # Find a workbook by name and open the first sheet
                        # Make sure you use the right name here.
                        sheet = client.open("Customer Requests").sheet1
                        username= sheet.cell(subject,2).value
                        name=sheet.cell(subject,3).value
                        email=sheet.cell(subject,4).value
                        phone=sheet.cell(subject,5).value
                        Sample=sheet.cell(subject,6).value
                        if "Product" in Sample:
                            #print('This is a Product Request')
                            idList='5fcfa030511b292fe2f58bf7'
                            Pname=sheet.cell(subject,7).value
                            Pcategory=sheet.cell(subject,8).value
                            Pskills=sheet.cell(subject,9).value
                            Pdescription=sheet.cell(subject,10).value
                            Ppermission=sheet.cell(subject,11).value
                            Ppayment=sheet.cell(subject,12).value
                            Rtype="New Product Request"
                            url = ('https://api.trello.com/1/cards?key='+ key +'&token='+ token+'&idList='+ idList+'&name='+ Pname+"&desc="+Pdescription)
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
                            url ='https://api.trello.com/1/checklists?key='+key+'&token='+token+'&idCard=' +cardid+ "&name=More Info About Request"  
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
                            
                            url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key=aa8ab2f4e1bf7b8f82f74196837c7d07&token=21ac30700a5b6e3e7896973437807791ffc0955c6d7902df82f7d804a9ae5043&name=Customer Name:'+str(name)
                            payload = {}
                            headers= {}
                            response = requests.request("POST", url, headers=headers, data = payload)
                            
                            url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key=aa8ab2f4e1bf7b8f82f74196837c7d07&token=21ac30700a5b6e3e7896973437807791ffc0955c6d7902df82f7d804a9ae5043&name=Customer Username:'+str(username)
                            payload = {}
                            headers= {}
                            response = requests.request("POST", url, headers=headers, data = payload)
                            
                            url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key=aa8ab2f4e1bf7b8f82f74196837c7d07&token=21ac30700a5b6e3e7896973437807791ffc0955c6d7902df82f7d804a9ae5043&name=Customer Email:'+str(email)
                            payload = {}
                            headers= {}
                            response = requests.request("POST", url, headers=headers, data = payload)
                            
                            url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key=aa8ab2f4e1bf7b8f82f74196837c7d07&token=21ac30700a5b6e3e7896973437807791ffc0955c6d7902df82f7d804a9ae5043&name=Customer Phone:'+str(phone)
                            payload = {}
                            headers= {} 
                            response = requests.request("POST", url, headers=headers, data = payload)
                            url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key=aa8ab2f4e1bf7b8f82f74196837c7d07&token=21ac30700a5b6e3e7896973437807791ffc0955c6d7902df82f7d804a9ae5043&name=Request Type:'+str(Rtype)
                            payload = {}
                            headers= {}
                            response = requests.request("POST", url, headers=headers, data = payload)
                            url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key=aa8ab2f4e1bf7b8f82f74196837c7d07&token=21ac30700a5b6e3e7896973437807791ffc0955c6d7902df82f7d804a9ae5043&name=Name Of Request:'+str(Pname)
                            payload = {}
                            headers= {}
                            response = requests.request("POST", url, headers=headers, data = payload)
                            url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key=aa8ab2f4e1bf7b8f82f74196837c7d07&token=21ac30700a5b6e3e7896973437807791ffc0955c6d7902df82f7d804a9ae5043&name=Software Category:'+str(Pcategory)
                            payload = {}
                            headers= {}
                            response = requests.request("POST", url, headers=headers, data = payload)
                            url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key=aa8ab2f4e1bf7b8f82f74196837c7d07&token=21ac30700a5b6e3e7896973437807791ffc0955c6d7902df82f7d804a9ae5043&name=Skills Needed:'+str(Pskills)
                            payload = {}
                            headers= {}
                            response = requests.request("POST", url, headers=headers, data = payload)
                            url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key=aa8ab2f4e1bf7b8f82f74196837c7d07&token=21ac30700a5b6e3e7896973437807791ffc0955c6d7902df82f7d804a9ae5043&name=Product Permissions:'+str(Ppermission)
                            payload = {}
                            headers= {}
                            response = requests.request("POST", url, headers=headers, data = payload)
                            url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key=aa8ab2f4e1bf7b8f82f74196837c7d07&token=21ac30700a5b6e3e7896973437807791ffc0955c6d7902df82f7d804a9ae5043&name=Payment Type:'+str(Ppayment)
                            payload = {}
                            headers= {}
                            response = requests.request("POST", url, headers=headers, data = payload)