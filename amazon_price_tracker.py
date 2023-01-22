from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from smtplib import SMTP
import time

print("Hello and welcome to PriceHawk")
print("\nTo begin kindly open up your browser and enter the following words 'what is my user agent")
print("\nCopy paste this text and enter it below...")

user_agent = input("\nUser-Agent: ")
url = input("\nEnter the amazon product URL that you are interested in buying: ")
RECIEVER_EMAIL = input(
    "\nEnter your email where you wish to recieve the updates: ")
AFFORDABLE_PRICE = float(
    input("\nWhat price are you willing to pay for the product: "))
SMTP_SERVER = "smtp.gmail.com"
PORT = 587
EMAIL_ID = "pricehawk.bot@gmail.com"
PASSWORD = "shubhankarisdumb"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()


def extract_price():
    driver.get(url)
    # Wait for the price element to be loaded
    price_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "a-price-whole"))
    )

    # Extract the price text
    price = float(price_element.text)
    return price


def notify(price):
    server = SMTP(SMTP_SERVER, PORT)
    server.starttls()
    server.login(EMAIL_ID, PASSWORD)

    subject = "BUY NOW!!!"
    body = "Price has fallen to " + str(price) + " go buy it NOW! - " + url
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(EMAIL_ID, RECIEVER_EMAIL, msg)
    server.quit()


while True:
    price = extract_price()
    if price and price <= AFFORDABLE_PRICE:
        notify(price)
        break
    else:
        print("Price is not affordable yet, checking again in 10 minutes...")
        time.sleep(600)

driver.quit()
