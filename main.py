from src.utils.email_fetcher import fetch_emails
from src.utils.email_classifier import classify_email
from src.utils.email_mover import move_email_to_label


def main():
    emails, mail = fetch_emails(limit=30)  

    for email_data in emails:
        category = classify_email(email_data["body"])
        print(f"Subject: {email_data['subject']}")
        print(f"Category: {category}\n")


        move_email_to_label(mail, email_data["email_id"], category)

    mail.logout()

if __name__ == "__main__":
    main()