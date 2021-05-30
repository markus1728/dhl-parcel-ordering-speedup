import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PaketScraping:

    def __init__(self, sender_address, receiver_address):

        self.sender_first_name = sender_address[0]
        self.sender_second_name = sender_address[1]
        self.sender_street = sender_address[2]
        self.sender_street_number = sender_address[3]
        self.sender_postal_code = sender_address[4]
        self.sender_city = sender_address[5]
        self.sender_email = sender_address[6]

        self.receiver_name = receiver_address[0]
        self.receiver_street = receiver_address[1]
        self.receiver_street_number = receiver_address[2]
        self.receiver_postal_code = receiver_address[3]
        self.receiver_city = receiver_address[4]

        self.opts = webdriver.FirefoxOptions()
        self.opts.headless = False
        self.driver = webdriver.Firefox(options=self.opts)

        self.driver.implicitly_wait(6)
        self.driver.get("https://www.dhl.de/de/privatkunden/pakete-versenden/deutschlandweit-versenden/paket.html")

        self.element = self.driver.find_element_by_id("confirm-choices-handler")
        self.driver.execute_script("arguments[0].click();", self.element)

        if receiver_address[5] == "2kg":
            self.element = self.driver.find_element_by_css_selector("a[href*='id=PAK02']")
            self.driver.execute_script("arguments[0].click();", self.element)
        else:
            self.element = self.driver.find_element_by_css_selector("a[href*='id=PAK05']")
            self.driver.execute_script("arguments[0].click();", self.element)

        self.element = self.driver.find_element_by_xpath('//button[normalize-space()="Weiter zur Adresseingabe"]')
        self.driver.execute_script("arguments[0].click();", self.element)

        self.element = self.driver.find_element_by_id("address.receiver.name2")
        self.driver.execute_script("arguments[0].click();", self.element)
        self.element.send_keys(self.receiver_name)
        time.sleep(0.2)

        self.element = self.driver.find_element_by_id("address.receiver.plz")
        self.driver.execute_script("arguments[0].click();", self.element)
        self.element.send_keys(self.receiver_postal_code)
        time.sleep(0.2)

        self.element = self.driver.find_element_by_id("address.receiver.city")
        self.driver.execute_script("arguments[0].click();", self.element)
        self.element.send_keys(self.receiver_city)
        time.sleep(0.2)

        self.element = self.driver.find_element_by_id("address.receiver.street")
        self.driver.execute_script("arguments[0].click();", self.element)
        self.element.send_keys(self.receiver_street)
        time.sleep(0.2)

        self.element = self.driver.find_element_by_id("address.receiver.streetNumber")
        self.driver.execute_script("arguments[0].click();", self.element)
        self.element.send_keys(self.receiver_street_number)
        time.sleep(0.2)

        self.element = self.driver.find_element_by_id("address.sender.name2")
        self.driver.execute_script("arguments[0].click();", self.element)
        self.element.send_keys(self.sender_first_name + " " + self.sender_second_name)
        time.sleep(0.2)

        self.element = self.driver.find_element_by_id("address.sender.plz")
        self.driver.execute_script("arguments[0].click();", self.element)
        self.element.send_keys(self.sender_postal_code)
        time.sleep(0.2)

        self.element = self.driver.find_element_by_id("address.sender.city")
        self.driver.execute_script("arguments[0].click();", self.element)
        self.element.send_keys(self.sender_city)
        time.sleep(0.2)

        self.element = self.driver.find_element_by_id("address.sender.street")
        self.driver.execute_script("arguments[0].click();", self.element)
        self.element.send_keys(self.sender_street)
        time.sleep(0.2)

        self.element = self.driver.find_element_by_id("address.sender.streetNumber")
        self.driver.execute_script("arguments[0].click();", self.element)
        self.element.send_keys(self.sender_street_number)
        time.sleep(0.2)

        self.element = self.driver.find_element_by_id("address.sender.email")
        self.driver.execute_script("arguments[0].click();", self.element)
        self.element.send_keys(self.sender_email)
        self.element.send_keys(Keys.ENTER)
        time.sleep(1)

        self.element = self.driver.find_element_by_xpath("//*[contains(@value,'paypal')]")
        self.driver.execute_script("arguments[0].click();", self.element)
        time.sleep(1)

        self.element = self.driver.find_element_by_xpath("//*[contains(@name,'agb')]")
        self.driver.execute_script("arguments[0].click();", self.element)
