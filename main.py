import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class SeamlessScraper:
    def __init__(self, username, password, page_number, login_path, saved_search_path, filter_path, next_page_path,
                 find_all_path):
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)

        self.url = f'https://login.seamless.ai/search/contacts?page={page_number}&locations=United%20States%20of%20America&industries=112&seniorities=1|2|3|30&employeeSizes=3|2&locationTypes=both&estimatedRevenues=3'
        self.username = username
        self.password = password
        self.login_path = login_path
        self.saved_search_path = saved_search_path
        self.filter_path = filter_path
        self.next_page_path = next_page_path
        self.find_all_path = find_all_path
        self.page_number = page_number

    def login(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")
        username_field.clear()
        username_field.send_keys(self.username)
        password_field.clear()
        password_field.send_keys(self.password)

        try:
            self.driver.find_element(By.XPATH, f"{self.login_path}").click()  # Login button
            self.driver.implicitly_wait(20)
            time.sleep(15)
            # self.driver.find_element(By.XPATH, f"{self.saved_search_path}").click() #saved Search Button
            # self.driver.implicitly_wait(10)
            # self.driver.find_element(By.XPATH, f"{self.filter_path}").click() # filters in saved searched button
            time.sleep(10)
            # self.driver.get('https://login.seamless.ai/search/contacts?page=2106&industries=70&locations=2&locationTypes=both&seniorities=1|2&titlesExactMatch=false&companiesExactMatch=false')
            # time.sleep(2)
            print('new page')
            # print("start page number")
            # page_number = self.driver.find_element(By.XPATH,'//*[@id="PageContainer"]/div[2]/div[2]/div[2]/div[2]/div/input')
            # page_number.clear()
            # page_number.send_keys(self.page_number)
            # page_number.send_keys(Keys.ENTER)
            # print("end start page number")

            completed_count = self.driver.find_element(By.XPATH,
                                                       "//*[@id='PageContainer']/div[1]/div/div/div[2]/div/div/div/span/span").text
            print(completed_count)

            split_input = completed_count.split(' ')

            # The first element of the list is the number as a string
            number_str = split_input[0]

            # Remove the comma from the number string
            number_str = number_str.replace(',', '')

            # Check if there is at least one match
            if number_str:
                # Convert the first match to an integer
                number = int(number_str)
                print(f"Extracted Number: {number}")
            else:
                print("No number found in the input string.")

            while number >= 500:
                find_all = self.driver.find_element(By.XPATH, f"{self.find_all_path}")

                if find_all.is_enabled():
                    print("clickable Find All")
                    self.driver.implicitly_wait(10)
                    self.driver.find_element(By.XPATH, f"{self.find_all_path}").click()  # Find All Button
                    print('done with finding')

                    print('waiting')
                    time.sleep(8)
                    self.driver.implicitly_wait(12)

                    self.driver.find_element(By.XPATH, f"{self.next_page_path}").click()  # Next Page Button
                    print("Page changed")
                    time.sleep(5)
                    self.driver.implicitly_wait(10)

                    number -= 25
                    print(number)

                else:
                    print('Not Clickable Find All')
                    print('wait to load')
                    time.sleep(8)
                    print('Loading Completed')
                    self.driver.find_element(By.XPATH, f"{self.next_page_path}").click()  # Next Page Button
                    print("Page changed")
                    self.driver.implicitly_wait(10)

                    time.sleep(10)

            print("successful")
        except Exception as e:
            print(e)
            print("not successful")


if __name__ == "__main__":
    username = "username"
    password = "password"
    page_number = '60'
    login_path = '//*[@id="root"]/div/div/div/div/div[1]/div/div/div[2]/form/button'
    saved_search_path = '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/span/button'

    filter_path = '//*[@id="dialog-:r52:"]/div/div/div[2]/div/div[1]'

    next_page_path = '//*[@id="PageContainer"]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[3]'
    find_all_path = '//*[@id="PageContainer"]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[1]'
    scraper = SeamlessScraper(username, password, page_number, login_path, saved_search_path, filter_path,
                              next_page_path, find_all_path)
    scraper.login()
