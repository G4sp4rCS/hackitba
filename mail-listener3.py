import email
import imaplib
from imap_tools import MailBox, AND
from datetime import datetime, timedelta

from getCreds import mailCredentials
mail, password = mailCredentials()

now = datetime.now()
now_plus_10 = now - timedelta(minutes = 4)


# get list of email subjects from INBOX folder
#with MailBox('imap.gmail.com').login(mail, password) as mailbox:
#    for msg in mailbox.fetch(AND(all=True)):
#        print(msg)
# get list of email subjects from INBOX folder - equivalent verbose version
mailbox = MailBox('imap.gmail.com')
mailbox.login(mail, password, initial_folder='INBOX')  # or mailbox.folder.set instead 3d arg
subjects = [msg for msg in mailbox.fetch(AND(all=True))]
print(subjects)
mailbox.logout()