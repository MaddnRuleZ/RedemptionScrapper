import random
import re
import time
from urllib.parse import urlparse, urljoin
from selenium import webdriver
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import Utilö


#tom@rozeedigital.com RuneScape05%

class Scrapper:
    def __init__(self, url):
        print("starting Arbitary Scrapper")
        self.url = url

        # HEADLESS OPTION
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.set_window_size(1800, 900)
        # Set page load timeout value in seconds
        page_load_timeout = 30
        # Set script timeout value in seconds
        script_timeout = 30

        # Set page load timeout and script timeout
        self.driver.set_page_load_timeout(page_load_timeout)
        self.driver.set_script_timeout(script_timeout)

        try:
            self.driver.get(url)
            time.sleep(5)
        except Exception as e:
            print("Error occurred while loading the page:", e)
            self.driver.quit()
            raise

    def login(self, email, password):
        print("logging in")
        email_input = self.driver.find_element(By.XPATH, "//input[@name='email']")
        email_input.send_keys(email)

        password_input = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_input.send_keys(password)

        sign_in_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in')]")
        sign_in_button.click()
        time.sleep(3)
        '''
        self.click_add_remove_filters_button()
        time.sleep(1)
        self.click_checkbox()
        time.sleep(1)
        self.click_apply_button()
        time.sleep(1)
        self.enter_text("0000")
        time.sleep(1)
        '''


        x = input("FIRST")

        elements = self.get_text_in_h6_elements()
        for elem in elements:
            Utilö.append_no_duplicates("cleaned.txt", elem)
            print(elem)
        x = input("SEC")

        for x in range(0, 50):
            self.random_sleep()
            print("Rand Sleep iter" + str(x))
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.END).perform()
        x = input("1")

        elements = self.get_text_in_h6_elements()
        for elem in elements:
            Utilö.append_no_duplicates("cleaned.txt", elem)
            print(elem)

        for x in range(0, 50):
            self.random_sleep()
            print("Rand Sleep iter" + str(x))
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.END).perform()

        elements = self.get_text_in_h6_elements()
        for elem in elements:
            Utilö.append_no_duplicates("cleaned.txt", elem)
            print(elem)

        input("X")

    def searchRoutine(self, email, password):
        print("logging in")
        email_input = self.driver.find_element(By.XPATH, "//input[@name='email']")
        email_input.send_keys(email)

        password_input = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_input.send_keys(password)

        sign_in_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in')]")
        sign_in_button.click()
        time.sleep(3)

        lines = Utilö.read_text_file("cleaned.txt")
        for index, line in enumerate(lines, start=1):
            if index > 2983: # todo del at cleaonlogic
                try:
                    self.driver.get("https://app.trendrocket.io/search/" + line)
                    self.random_sleep()
                    ref = self.get_first_href()
                    num = self.extract_number(ref)
                    print(num)
                    self.driver.get("https://app.trendrocket.io/brands/" + str(num) + "/overview")
                    self.random_sleep()
                    url = self.get_href_from_element("MuiBox-root.css-wbddbz")
                    Utilö.append_string_to_file("final2.txt", f"[{index}]{line}, {url}")
                except:
                    Utilö.append_string_to_file("final2.txt", f"!!!!{line}, Index: {index}")

    def get_href_from_element(self, class_name):
            # Find the element by class name
            element = self.driver.find_element(By.CLASS_NAME, class_name)

            # Extract the href attribute
            href = element.get_attribute("href")

            return href

    def get_text_in_h6_elements(self):
        try:
            h6_elements = self.driver.find_elements(By.TAG_NAME, 'h6')
            h6_texts = [element.text for element in h6_elements]
            return h6_texts
        except NoSuchElementException:
            print("No <h6> elements found.")
            return None


    def get_text_in_elements(self, class_name):
        try:
            elements = self.driver.find_elements(By.CLASS_NAME, class_name)
            return elements
        except NoSuchElementException:
            print("Element not found.")
            return None

    def get_first_href(self):
            # Find the first <a> element with the specified class
            first_element = self.driver.find_element(By.CSS_SELECTOR, 'a.MuiStack-root.css-iaq3z7')

            # Extract the href attribute
            href = first_element.get_attribute("href")

            return href

    def extract_number(self, text):
        # Using regular expression to find the first occurrence of a number in the string
        match = re.search(r'\d+', text)

        # If a number is found, return it as an integer, otherwise return None
        if match:
            return int(match.group())
        else:
            return None

    def random_sleep(self, minimum=1.5, maximum=2.5):
        """
        Introduces a random sleep delay between the given minimum and maximum seconds.
        Default minimum delay is 1 second and maximum delay is 5 seconds.
        """
        delay = random.uniform(minimum, maximum)
        print("Sleeping for {:.2f} seconds...".format(delay))
        time.sleep(delay)

    def get_element_url(self):
        print("getting element URL")
        # Find the span element containing the link
        link_element = self.driver.find_element(By.CSS_SELECTOR, 'span[data-darkreader-inline-color=""]')

        # Extract the link URL from the href attribute
        link_url = link_element.get_attribute('href')

        print(link_url)

    def click_add_remove_filters_button(self):
        print("clicking add/remove filters button")
        add_remove_filters_button = self.driver.find_element(By.XPATH,
                                                             "//button[contains(text(), 'Add/Remove filters')]")
        add_remove_filters_button.click()

    def click_checkbox(self):
        print("clicking checkbox")
        checkboxs = self.driver.find_elements(By.CLASS_NAME, "PrivateSwitchBase-input")
        checkboxs[1].click()

    def click_apply_button(self):
        print("clicking apply button")
        apply_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Apply')]")
        apply_button.click()

    def enter_text(self, text):
        print("entering text")
        input_field = self.driver.find_element(By.ID, "igfollowers-min")
        input_field.clear()  # Clear any existing text
        input_field.send_keys(str(text))

    def scroll_to_end(self):
        print("scrolling to the end of the page")
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.END).perform()

    def start(self):
        print("Start")

    def save_page_source(self, filename):
        print("saving page source")
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.driver.page_source)
        print("Page source saved to", filename)
