import requests

def suggest_emails(username, domains=None):
    if not domains:
        domains = [
            "gmail.com", "yahoo.com", "outlook.com", "hotmail.com",
            "icloud.com", "protonmail.com", "mail.com"
        ]
    return [f"{username}@{d}" for d in domains]

def verify_email_hunter(email, api_key=None):
    # إذا لم يوجد API Key، تحقق من الصياغة فقط
    if not api_key:
        if "@" in email and "." in email.split("@")[1]:
            return "صياغة صحيحة (لم يتم التحقق الفعلي)"
        else:
            return "صياغة غير صحيحة"
    # تحقق فعلي عبر Hunter.io
    try:
        resp = requests.get(
            "https://api.hunter.io/v2/email-verifier",
            params={"email": email, "api_key": api_key},
            timeout=10
        )
        data = resp.json()
        if resp.status_code == 200 and "data" in data:
            result = data["data"]
            status = result.get("status", "unknown")
            score = result.get("score", 0)
            return f"Hunter: {status} (Score: {score})"
        else:
            return f"خطأ API: {data.get('errors', 'غير معروف')}"
    except Exception as e:
        return f"خطأ في الاتصال: {e}"