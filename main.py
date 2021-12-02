import requests
import smtplib
import lxml
from bs4 import BeautifulSoup

MY_EMAIL = "usamatest32@gmail.com"
PASSWORD = "Angela$32"

PRODUCT_URL = "https://www.amazon.com/Oculus-Quest-Advanced-All-One-Virtual/dp/B09DCM6CNZ/ref=sr_1_1?crid=1JWL1HBO" \
              "EQUKJ&dchild=1&keywords=oculus&qid=1635404664&sprefix=oculus%2Caps%2C412&sr=8-1&th=1"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/95.0.4638.54 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ur;q=0.8",
}
response = requests.get(url=PRODUCT_URL, headers=header)
content = response.text

# with open("amazon.txt", mode='w', encoding="utf-8") as at:
#     at.write(content)

# with open("amazon.txt", mode='r', encoding='utf-8') as rat:
#     info = rat.read()

soup = BeautifulSoup(content, 'lxml')
dollar_price = soup.find(name='span', id='priceblock_ourprice')
title = soup.find(name="span", id="productTitle")
float_price = float(dollar_price.getText().split('$')[1])

if float_price < 100.00:
    message = f"Subject: Amazon Price Alert\n\n{title.getText()} is now {dollar_price.getText()} only.\nBuy Now\n{PRODUCT_URL}"
    enc_meassage = message.encode("utf-8")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="Syedusama70@gmail.com",
                            msg=enc_meassage)
