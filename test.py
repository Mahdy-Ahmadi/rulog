from rulog import Client

client = Client()

print("Phone format examples: Iran 98xxxxxxxxxx | US 1xxxxxxxxxx | UK 44xxxxxxxxxx")
phone = input("Phone (no +, e.g. 98912...): ").strip()

if not phone.isdigit():
    print("Error: Phone must contain only digits.")
    exit()
if not (9 <= len(phone) <= 15):
    print("Error: Phone length must be between 9 and 15 digits.")
    exit()

try:
    print("Sending code...")
    resp = client.sendCode("android", phone)
    code_hash = resp['data']['phone_code_hash']
    print("Code sent.")
except Exception as e:
    print("Failed to send code:", e)
    exit()

code = input("Enter code: ").strip()

try:
    print("Signing in...")
    login_resp = client.signIn("android", phone, code_hash, code, save=phone)
    print("Login successful.")
except Exception as e:
    print("Login error:", e)
    exit()

try:
    print("Registering (if needed)...")
    ok = client.register(platform="android", auths=login_resp['Auth'], keys=login_resp['Key'])
    if ok:
        print("Registered successfully.")
    else:
        print("Register returned False (maybe already registered).")
except Exception as e:
    print("Register error:", e)
