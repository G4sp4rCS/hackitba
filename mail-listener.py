import email_listener
import email_listener
from getCreds import mailCredentials
# Set your email, password, what folder you want to listen to, and where to save attachments
mail, password = mailCredentials()
app_password = password
email = mail
folder = "Inbox"
attachment_dir = "./attachments"
el = email_listener.EmailListener(email, app_password, folder, attachment_dir)

# Log into the IMAP server
el.login()

# Get the emails currently unread in the inbox
messages = el.scrape()
print(messages)

# Start listening to the inbox and timeout after ten minutes
timeout = 10
el.listen(timeout)