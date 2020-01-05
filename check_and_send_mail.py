import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.de/dp/B07SFJK8FH/ref=sr_1_1?crid=20ZQT0ANBKITV&keywords=cod+mw+ps4&qid=1578241703&sprefix=cod+mw%2Caps%2C164&sr=8-1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    print('Checking COD MW PS4 price, hold on!')
    print(price)
    converted_price = float(price[0:2])

    if(converted_price < 55.00):
        send_mail()
        print(converted_price)
        print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('user_email@gmail.com', 'generated_password')
    subject = 'Price fell down!'
    body = 'Check the amazon link  https://www.amazon.de/dp/B07SFJK8FH/ref=sr_1_1?crid=20ZQT0ANBKITV&keywords=cod+mw+ps4&qid=1578241703&sprefix=cod+mw%2Caps%2C164&sr=8-1'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'sender_email@gmail.com', 'receiver_email@gmail.com', msg
    )
    print('Hey email has been sent')
    server.quit()


check_price()    
