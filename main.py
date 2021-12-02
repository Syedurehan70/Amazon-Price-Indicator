import requests
import smtplib
import lxml
from bs4 import BeautifulSoup
import os

MY_EMAIL = os.environ.get("my_email")
PASSWORD = os.environ.get("my_pass")

PRODUCT_URL = "https://www.amazon.com/Oculus-Quest-Advanced-All-One-Virtual/dp/B09DCM6CNZ/ref=sr_1_1?crid=1JWL1HBO" \
              "EQUKJ&dchild=1&keywords=oculus&qid=1635404664&sprefix=oculus%2Caps%2C412&sr=8-1&th=1"

header = {
    "User-Agent": os.environ.get("user_agent"),
    "Accept-Language": "en-US,en;q=0.9,ur;q=0.8",
}

# so we're making a request to the product page on amazon to give us the prize of product we're interested in
response = requests.get(url=PRODUCT_URL, headers=header)
content = response.text

# parsing the data return from url, converting it into text
soup = BeautifulSoup(content, 'lxml')

# extracting prize of the product in dollars and extracting title of the product
dollar_price = soup.find(name='span', id='priceblock_ourprice')
title = soup.find(name="span", id="productTitle")

# separating only int part
float_price = float(dollar_price.getText().split('$')[1])

# the comparing prize can be defined by us, if the prize is lower than what we think reasonable, than it'll send email
if float_price < 100.00:

    # saving msg in separate variable, and encoding it in utf-8
    message = f"Subject: Amazon Price Alert\n\n{title.getText()} is now {dollar_price.getText()} only.\nBuy Now\n{PRODUCT_URL}"
    enc_meassage = message.encode("utf-8")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=os.environ.get("receivers_mail"),
                            msg=enc_meassage)
