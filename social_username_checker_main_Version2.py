from platforms import SOCIAL_PLATFORMS
from email_check import suggest_emails, verify_email_hunter
import requests

def check_social(username):
    results = {}
    for platform, url in SOCIAL_PLATFORMS.items():
        profile_url = url.format(username)
        try:
            resp = requests.get(profile_url, timeout=5)
            if resp.status_code == 200:
                results[platform] = {"exists": True, "url": profile_url}
            else:
                results[platform] = {"exists": False, "url": profile_url}
        except Exception:
            results[platform] = {"exists": False, "url": profile_url}
    return results

def main():
    username = input("أدخل اسم المستخدم للبحث عنه: ").strip()
    print("\n[+] البحث في الشبكات الاجتماعية...\n")
    results = check_social(username)
    for platform, info in results.items():
        status = "✅ موجود" if info["exists"] else "❌ غير موجود"
        print(f"{platform:12}: {status} - {info['url']}")

    print("\n[+] احتمالات البريد الإلكتروني والنتيجة (عبر Hunter.io):")
    emails = suggest_emails(username)
    api_key = input("\nأدخل مفتاح API الخاص بـ Hunter.io (أو اتركه فارغًا لفحص الصياغة فقط): ").strip()
    for email in emails:
        result = verify_email_hunter(email, api_key=api_key)
        print(f"- {email} - {result}")

if __name__ == "__main__":
    main()