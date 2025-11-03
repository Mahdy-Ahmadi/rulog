from rulog import Client

client = Client()

phone = input("📱 Phone (Help: 98918467....): ").strip()

try:
    response = client.sendCode("android", phone)
    code_hash = response['data']['phone_code_hash']
except Exception:exit()

code = input("Code : ").strip()

try:
    login_response = client.signIn("android", phone, code_hash, code,save="session")
    print("✅ Ok Login")
    print(login_response)
except Exception as e:
    print("❌ Error Login :", e)
    exit()
try:
    result = client.register(platform="android", auths=login_response['Auth'], keys=login_response['Key'])
    if result:print("✅ Ok Regester")
    else:print("❌ Not Regester")
except Exception as e:print(e)
