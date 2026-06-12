import imaplib
import email
from email.header import decode_header
import re

# Local configuration placeholders for student customization
IMAP_SERVER = "imap.gmail.com"
EMAIL_ACCOUNT = "your_email@gmail.com"
APP_PASSWORD = "your_app_password_here"  # Google App Password, NOT main password

def connect_and_triage():
    print(f"🔒 Attempting secure connection to {IMAP_SERVER}...")
    try:
        # Standard SSL IMAP initialization connection
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        print("🌐 Connection established. Testing authentication placeholders...")
        
        # We fail gracefully here so students cloning the repo can see it works up to auth
        if EMAIL_ACCOUNT == "your_email@gmail.com":
            print("\n💡 Triage Engine initialized successfully!")
            print("📝 Status: Standing by. Configuration required in '.env' or script variables.")
            return True
            
        mail.login(EMAIL_ACCOUNT, APP_PASSWORD)
        mail.select("inbox")
        print("📥 Successfully logged into mailbox. Searching application confirmations...")
        
        # Simple search for common ATS keywords
        status, messages = mail.search(None, '(BODY "application received" OR BODY "thank you for applying")')
        email_ids = messages[0].split()
        print(f"📊 Found {len(email_ids)} job application confirmation emails.")
        
    except Exception as e:
        print(f"❌ Connection or Auth Error: {e}")
        print("💡 Tip: If using Gmail, make sure you generated a 16-digit 'App Password' via Google Account Security.")

if __name__ == "__main__":
    connect_and_triage()