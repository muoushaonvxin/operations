#!/usr/local/python34/bin/python3
#-*- encoding: utf-8 -*-
import os, sys
import smtplib
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

def sendMail(email, subject, mailtext):
	
    mailInfo = {
	    "from": "15071567976@163.com",
	    "to": email,
	    "hostname": "smtp.zoho.com",
	    "username": "15071567976@163.com",
	    "password": "xxxxxxxxxxxx",
	    "mailsubject": subject,
	    "mailtext": mailtext,
	    "mailencoding": "utf-8",
    }

	smtp = SMTP_SSL(mailInfo["hostname"])
	smtp.set_debuglevel(1)
	smtp.ehlo(mailInfo["hostname"])
	smtp.login(mailInfo["username"],mailInfo["password"])

	msg = MIMEText(mailInfo["mailtext"], "text", mailInfo["mailencoding"])
	msg["Subject"] = Header(mailInfo["mailsubject"], mailInfo["mailencoding"])
	msg["from"] = mailInfo["from"]
	msg["to"] = mailInfo["to"]
	smtp.sendmail(mailInfo["from"], mailInfo["to"], msg.as_string())
	smtp.quit()
