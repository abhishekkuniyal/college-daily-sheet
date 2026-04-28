import requests
from bs4 import BeautifulSoup

session = requests.Session()

# Step 1: GET page
page = session.get("https://student.uttaranchaluniversity.ac.in/Account/Login_UU", headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
})

soup = BeautifulSoup(page.text, "html.parser")

# Step 2: Extract token
token = soup.find("input", {"name": "__RequestVerificationToken"})["value"]
print("Token:", token)

# Step 3: GET captcha image and save it
captcha_response = session.post("https://app.uudoon.in/Mobile_General/showrefreshcaptchaImage", headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
})

with open("captcha.txt", "wb") as f:
    f.write(captcha_response.content)

print("Captcha saved as captcha.png")

# Step 4: Open captcha.png, read it manually, then enter value below
captcha_value = input("Enter captcha value: ")

# Step 5: POST login
response = session.post("https://app.uudoon.in/", data={
    "__RequestVerificationToken": token,
    "MUserName": "23210101322",
    "MMobileNo": "6397973641",
    "MPassword": "abhishek@12",
    "captcha": captcha_value
}, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
})

print("Login Status:", response.status_code)
print(response.text[:2000])