from selenium import webdriver
import gspread
import os

# Settings - driver selenium

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--incognito")

driver = webdriver.Chrome(
    executable_path="chromedriver",
    options=options
)

# Settings - google table

gc = gspread.service_account(filename='credentials.json')
sheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/1IDS7Gy2UUqWh_h_1xLTP_GUL9IvYexVxo6Ol-kQu4Iw/edit#gid=0")
list = sheet.worksheet("Финансы")

# Settings - users

login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
