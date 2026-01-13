import imaplib
import email


IMAP_SERVER = "imap.gmail.com"
EMAIL_ACCOUNT = "your-email"
APP_PASSWORD = "your-app-pass"
SENDER_EMAIL = "xyz@example.com"


def delete_emails_from_sender():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ACCOUNT, APP_PASSWORD)

    mail.select("inbox")

    status, messages = mail.search(None, f'FROM "{SENDER_EMAIL}"')

    if status != "OK":
        print("Koi email nahi hai .")
        return

    email_ids = messages[0].split()

    if not email_ids:
        print("Koi Email nahi bacha Hai.")
        return

    for email_id in email_ids:
        mail.store(email_id, '+FLAGS', '\\Deleted')

    mail.expunge()
    mail.logout()

    print(f"Delete ho gaye {len(email_ids)} emails from {SENDER_EMAIL}")

if __name__ == "__main__":
    delete_emails_from_sender()
