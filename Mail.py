import email
import imaplib
import threading
import time

previous_email_id = ''

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('<Your Email>','<Your Password>')


while (True):
    mail.list()
    mail.select('inbox')

    def PrintBody(data):
        print(data.strip())

    def get_first_text_block(email_message_instance):
        maintype = email_message_instance.get_content_maintype()
        if maintype == 'multipart':
            for part in email_message_instance.get_payload():
                if part.get_content_maintype() == 'text':
                    PrintBody (part.get_payload())
                    break
        elif maintype == 'text':
            PrintBody (email_message_instance.get_payload())

    result, data = mail.search(None,'ALL')


    ids = data[0]
    id_list = ids.split()
    latest_email_id = id_list[-1]

    print(latest_email_id)

    if latest_email_id != previous_email_id :
        previous_email_id = latest_email_id
        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]

        email_message = email.message_from_string(raw_email)

        get_first_text_block(email_message)
    else : print("NO NEW EMAILS")
time.sleep(500)
