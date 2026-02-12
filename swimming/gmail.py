import imaplib
import email
from email.header import decode_header
import os
import time
import pdf

IMAP_SERVER = "imap.gmail.com"
EMAIL_ACCOUNT = "tamar.swimming@gmail.com"
APP_PASSWORD = "uwco aejg erid zurk"

PATH_ALL_PDF_MAIL = "C:/Users/yehon/OneDrive/Dokumenter/tamar_swimming/all_pdf_mail"
PATH_PDF_SWIMMING = "C:/Users/yehon/OneDrive/Dokumenter/tamar_swimming/pdf_swimming"

os.makedirs(PATH_ALL_PDF_MAIL, exist_ok=True)
os.makedirs(PATH_PDF_SWIMMING, exist_ok=True)


imap = imaplib.IMAP4_SSL(IMAP_SERVER)
imap.login(EMAIL_ACCOUNT, APP_PASSWORD)
imap.select("INBOX")


def mail():
    status, messages = imap.search(None, "UNSEEN")
    mail_ids = messages[0].split()

    print(f"נמצאו {len(mail_ids)} מיילים שלא נקראו")

    for mail_id in mail_ids:
        status, msg_data = imap.fetch(mail_id, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        subject = msg["Subject"]
        decoded = decode_header(subject)[0]
        subject = decoded[0]
        if isinstance(subject, bytes):
            subject = subject.decode(decoded[1] or "utf-8")

        print("נושא:", subject)

        for part in msg.walk():
            content_type = part.get_content_type()
            disposition = str(part.get("Content-Disposition"))

            if content_type == "application/pdf" and "attachment" in disposition:
                filename = part.get_filename()

                if filename:
                    decoded_tuple = decode_header(filename)[0]
                    filename_str = decoded_tuple[0]
                    encoding = decoded_tuple[1]

                    if isinstance(filename_str, bytes):
                        filename_str = filename_str.decode(encoding or "utf-8")

                    filename_str = filename_str.replace("/", "_").replace("\\", "_").replace(":", "_") \
                        .replace("*", "_").replace("?", "_").replace("\"", "_") \
                        .replace("<", "_").replace(">", "_").replace("|", "_")

                    if "מילוי לטופס הצהרת בריאות" in filename_str or "מילוי לטופס הצהרת בריאות" in subject:
                        save_to = PATH_PDF_SWIMMING
                    else:
                        save_to = PATH_ALL_PDF_MAIL

                    unique_filename = os.path.join(save_to, f"{int(time.time())}_{filename_str}")

                    with open(unique_filename, "wb") as f:
                        f.write(part.get_payload(decode=True))

                    print(f"✔ נשמר קובץ PDF: {unique_filename}")

        imap.store(mail_id, '+FLAGS', '\\Seen')

    imap.logout()




