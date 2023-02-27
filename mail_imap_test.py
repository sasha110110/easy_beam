import os
import imaplib
import email
from email.header import Header, decode_header
from email.parser import HeaderParser

import re

def check_email():
    mail = imaplib.IMAP4_SSL('imap.mail.ru')
    passw=os.environ.get("passw")
    #print(passw)
    #passw=""
    mail.login('marsasha@mail.ru', passw) #TODO GMAIL PASSWORD
    #print(mail.list()[:10])
    letters=mail.select()
    
    num = int(letters[1][0].decode('utf-8'))
    print(num)
    number=int(num)
    #10
    #for n in range(num-9, num):
    #resp, lst = mail.fetch(str(n), '(RFC822)')
    
    #while True:
    resp, lst = mail.fetch(str(num), '(RFC822)') #?????????/////
    body = lst[0][1]
    
    msg = email.message_from_bytes(body)
    #print(msg)
    
        #if "yoomoney" in msg["Return-path"] #.encode().decode('utf-8'):
          #  break
##    body_m=""
##    if msg.is_multipart():
##        
##        for part in msg.walk():
##    
##            content_type = part.get_content_type()
##            content_disposition = str(part.get("Content-Disposition"))
##            try:
##            
##                body_part = part.get_payload(decode=True).decode()
##            except:
##                pass
##            if content_type == "text/plain" and "attachment" not in content_disposition:
##                body_m+=body_part
##
##    operation=re.search("^notification_type =(\w+)", body_m).groups()
##    money=re.search("^amount = (\w+)", body_m).grops()
##    operation_id=e.search("^operation_id = (\w+)", body_m).grops()
##
##    if 'card-incoming' in operation:
##        return(float(money))
##    else:
##        return "Произошла чудовищная ошибка"
##   
    return [441361714955017004, 100]
