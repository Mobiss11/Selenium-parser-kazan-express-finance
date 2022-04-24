import time
import random

from openpyxl import load_workbook
from selenium.webdriver.common.by import By

from consts import *
from settings import *

while True:

    try:

        driver.get(URL)
        driver.implicitly_wait(80)

        driver.find_element(By.XPATH, LOGIN_INPUT).send_keys(login)
        driver.implicitly_wait(80)

        driver.find_element(By.XPATH, PASS_INPUT).send_keys(password)
        driver.implicitly_wait(80)

        driver.find_element(By.XPATH, BUTTON_LOGIN).click()
        driver.implicitly_wait(80)
        time.sleep(2)

        driver.get(PATH_FILE_SAIT)

        number = driver.find_element(By.XPATH, NUMBER_ITEMS).send_keys(NUMBER_ITEMS_KEY)

        driver.find_element(By.XPATH, BUTTON_ITEMS).click()

        driver.implicitly_wait(80)

        column_date = list.col_values(3)
        column_number_order = list.col_values(5)

        driver.find_element(By.XPATH, BUTTON_SELECT_FILE).click()
        time.sleep(2)

        driver.find_element(By.CSS_SELECTOR, BUTTON_XLSX).click()

        time.sleep(10)

        driver.quit()

        wb = load_workbook(FILE)
        wb.active = 0
        sheet = wb.active
        num = len(sheet[COLUMN_1]) + 1

        for i in range(2, num):
            product_status = sheet[COLUMN_1 + str(i)].value
            product_date_start = sheet[COLUMN_2 + str(i)].value
            product_date_end = sheet[COLUMN_3 + str(i)].value
            product_number = sheet[COLUMN_4 + str(i)].value
            product_sku = sheet[COLUMN_5 + str(i)].value
            product_name = sheet[COLUMN_6 + str(i)].value
            product_quantity = sheet[COLUMN_7 + str(i)].value
            product_price = float(
                sheet[COLUMN_8 + str(i)].value.replace(RUBL, NO_SPACE).replace(COMMA, DOT))
            product_price_cost = float(
                sheet[COLUMN_9 + str(i)].value.replace(RUBL, NO_SPACE).replace(COMMA, DOT))
            product_conclusion = float(
                sheet[COLUMN_10 + str(i)].value.replace(RUBL, NO_SPACE).replace(COMMA, DOT).replace(SPACE, NO_SPACE))
            product_conclusion_2 = float(
                sheet[COLUMN_11 + str(i)].value.replace(RUBL, NO_SPACE).replace(COMMA, DOT))
            product_commission = float(
                sheet[COLUMN_12 + str(i)].value.replace(RUBL, NO_SPACE).replace(COMMA, DOT))

            print(
                product_status,
                product_date_start,
                product_date_end,
                product_number,
                product_sku,
                product_name,
                product_quantity,
                product_price,
                product_conclusion,
                product_conclusion_2,
                product_quantity
                  )

            product_table_date = sheet[f'{COLUMN_2}{i}'].value
            product_table_number = sheet[f'{COLUMN_4}{i}'].value

            if product_table_date in column_date and product_table_number in column_number_order:
                print(MESSAGE_ELEMENT)

            else:

                uniq_number = random.random()

                elements_column = list.col_values(14)
                last_element = elements_column[-1]
                index_last_element = elements_column.index(last_element)
                number_row = index_last_element + 2

                list.update(f'{COLUMN_2}{number_row}:{COLUMN_13}{number_row}',
                            [[
                                product_status,
                                product_date_start,
                                product_date_end,
                                product_number,
                                product_sku,
                                product_name,
                                product_quantity,
                                product_price,
                                product_conclusion,
                                product_conclusion_2,
                                product_quantity,
                                uniq_number
                            ]])

        os.remove(FILE)

    except:
        print(EROR)

    time.sleep(300)



















