import requests
from requests import HTTPError
import lxml
from bs4 import BeautifulSoup

URL ="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
HEADERS = {
    "User-Agent": "Defined",
    "Accept-Language": "en-US,en;q=0.5"
}
BUY_PRICE = 90
try:
    response = requests.get(url=URL, headers=HEADERS)
    response.raise_for_status()
    print(f"Response code is: {response.status_code}")
    soup = BeautifulSoup(response.text, "html.parser")
    # To view the code locally
    # with open("index.html", "w",encoding="utf-8") as f:
    #     f.write(soup.prettify())
    price = soup.find(class_="a-offscreen").get_text()
    # print(f"Price: {price}")
    price_without_currency = float(price.split("$")[1])
    print(f"Price without currency: {price_without_currency}")
    title = soup.find(id="productTitle").get_text().strip()
    if price_without_currency<BUY_PRICE:
        message = f"{title} is now {price}"
        # TODO setup smtp mail for sending alert 
    else:
        message = f"{title} is now {price}"
    print(message)
except HTTPError:
    print(f"Response code is: {response.status_code}")


