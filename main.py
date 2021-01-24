from bs4 import BeautifulSoup
import lxml
import requests
import smtplib
link = "https://www.amazon.in/Crompton-Greaves-Speed-Ceiling-Standard/dp/B07VKDPXBZ/ref=sr_1_10?crid=157F8ISWEVQM7&dchild=1&keywords=ceiling%2Bfan&qid=1611468617&sprefix=ceilin%2Caps%2C705&sr=8-10&th=1"
header = {
"Accept-Language" : "en-US,en;q=0.9",
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
}
user_name = "Your mail address"
password = "password"
to_ADD = "email address of to who want to send"

response = requests.get(url=link, headers=header)
page = response.text
soup = BeautifulSoup(page, "lxml")
Product_name = soup.find(name="span", id="productTitle").getText()
value = float(soup.find(name="span", id="priceblock_ourprice").getText().split()[1].replace(",",""))
if value <=3550.0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = user_name, password = password)
        connection.sendmail(from_addr = user_name,
                            to_addrs= to_ADD , msg = f"Subject:Price Drop alert from Amazon\n\n {Product_name}\n"
                                                     f"is at desired price checkout this page to buy know\n{link}")
