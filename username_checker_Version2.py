import requests

SOCIAL_PLATFORMS = {
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://instagram.com/{}",
    "Facebook": "https://facebook.com/{}",
    "GitHub": "https://github.com/{}",
    "Reddit": "https://reddit.com/user/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "Pinterest": "https://pinterest.com/{}",
    "YouTube": "https://www.youtube.com/{}",
    "Medium": "https://medium.com/@{}"
}

def check_social(username):
    results = {}
    for platform, url in SOCIAL_PLATFORMS.items():
        profile_url = url.format(username)
        try:
            resp = requests.get(profile_url, timeout=5)
            if resp.status_code == 200:
                results[platform] = profile_url
            else:
                results[platform] = None
        except Exception:
            results[platform] = None
    return results

def check_email(username, domains=None):
    if not domains:
        domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
    emails = [f"{username}@{d}" for d in domains]
    # ملاحظة: هذا لا يتحقق فعليا من وجود الإيميل، فقط يعطي احتمالات
    # للتحقق الفعلي استخدم API مثل Hunter.io أو email-verifier.io
    return emails

def main():
    username = input("أدخل اسم المستخدم للبحث عنه: ").strip()
    print("جاري البحث في الشبكات الاجتماعية...")
    results = check_social(username)
    for platform, url in results.items():
        if url:
            print(f"✅ {platform}: {url}")
        else:
            print(f"❌ {platform}: غير موجود")

    print("\nاحتمالات البريد الإلكتروني:")
    emails = check_email(username)
    for email in emails:
        print(f"- {email}")

if __name__ == "__main__":
    main()