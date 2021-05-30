import time
from selenium import webdriver


class WarenversandScraping:

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

        self.options = webdriver.FirefoxProfile()
        self.options.set_preference("browser.download.folderList", 2)
        self.options.set_preference("browser.download.dir", "...")
        self.options.set_preference("browser.download.forbid_open_with", True)
        self.options.set_preference("browser.download.manager.alertOnEXEOpen", False)
        self.options.set_preference("browser.helperApps.neverAsk.openFile",
                                    "application/unknown, application/x-www-form-urlencoded, application/msword, application/csv, application/ris, text/csv, image/png, application/pdf, text/html, text/plain, application/zip, application/x-zip, application/x-zip-compressed, application/download, application/x-download, application/octet-stream")
        self.options.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                    "application/unknown, application/x-www-form-urlencoded, application/msword, application/csv, application/ris, text/csv, image/png, application/pdf, text/html, text/plain, application/zip, application/x-zip, application/x-zip-compressed, pplication/download, application/x-download, application/octet-stream")
        self.options.set_preference("browser.download.manager.showWhenStarting", False)
        self.options.set_preference("browser.download.manager.focusWhenStarting", False)
        self.options.set_preference("browser.download.useDownloadDir", True)
        self.options.set_preference("browser.helperApps.alwaysAsk.force", False)
        self.options.set_preference("browser.download.manager.alertOnEXEOpen", False)
        self.options.set_preference("browser.download.manager.closeWhenDone", True)
        self.options.set_preference("browser.download.manager.showAlertOnComplete", False)
        self.options.set_preference("browser.download.manager.useWindow", False)
        self.options.set_preference("services.sync.prefs.sync.browser.download.manager.showWhenStarting", False)
        self.options.set_preference("pdfjs.disabled", True)

        self.opts = webdriver.FirefoxOptions()
        self.opts.headless = False
        self.driver = webdriver.Firefox(options=self.opts, firefox_profile=self.options)

        self.driver.implicitly_wait(6)
        self.driver.get(
            "https://shop.deutschepost.de/briefversand/spezielle-versandformen/buechersendung-und-warensendung")

        self.element = self.driver.find_element_by_id("confirm-choices-handler")
        self.driver.execute_script("arguments[0].click();", self.element)

        if receiver_address[5] == "500g":
            self.element = self.driver.find_element_by_css_selector("a[href*='Id=282']")
            self.driver.execute_script("arguments[0].click();", self.element)
        else:
            self.element = self.driver.find_element_by_css_selector("a[href*='Id=290']")
            self.driver.execute_script("arguments[0].click();", self.element)

        self.element = self.driver.find_element_by_xpath('//*[@title="Absender und Empfänger hinzufügen"]')
        self.driver.execute_script("arguments[0].click();", self.element)

        self.element = self.driver.find_element_by_id("sender_addressfield")
        self.driver.execute_script("arguments[0].click();", self.element)

        sender_input_string = self.sender_first_name + " " + self.sender_second_name + "\n" \
                              + self.sender_street + "  " + self.sender_street_number + "\n" \
                              + self.sender_postal_code + " " + self.sender_city

        self.element.send_keys(sender_input_string)

        self.element = self.driver.find_element_by_id("recipient_addressfield")
        self.driver.execute_script("arguments[0].click();", self.element)

        receiver_input_string = self.receiver_name + "\n" \
                                + self.receiver_street + "  " + self.receiver_street_number \
                                + "\n" + self.receiver_postal_code + " " + self.receiver_city

        self.element.send_keys(receiver_input_string)

        self.element = self.driver.find_element_by_xpath('//button[normalize-space()="Adresse(n) übernehmen"]')
        self.driver.execute_script("arguments[0].click();", self.element)

        self.element = self.driver.find_element_by_xpath('//a[@title="PDF Datei zum Testdruck erzeugen"]')
        self.driver.execute_script("arguments[0].click();", self.element)

        time.sleep(1)

        self.element = self.driver.find_element_by_xpath('//button[normalize-space()="In den Warenkorb"]')
        self.driver.execute_script("arguments[0].click();", self.element)

        self.element = self.driver.find_element_by_id("agbcheck")
        self.driver.execute_script("arguments[0].click();", self.element)

        self.element = self.driver.find_element_by_xpath('//a[normalize-space()="Nächster Schritt"]')
        self.driver.execute_script("arguments[0].click();", self.element)

        self.element = self.driver.find_element_by_xpath('//a[normalize-space()="Gastzugang nutzen"]')
        self.driver.execute_script("arguments[0].click();", self.element)

        self.driver.implicitly_wait(6)

        self.element = self.driver.find_element_by_xpath("//*[contains(@class,'form__input jsvRequired jsvFirstname')]")
        self.element.send_keys(self.sender_first_name)

        self.element = self.driver.find_element_by_xpath("//*[contains(@class,'form__input jsvRequired jsvLastname')]")
        self.element.send_keys(self.sender_second_name)

        self.element = self.driver.find_element_by_xpath("//*[contains(@class,'jsvRequired typeahead-street')]")
        self.element.send_keys(self.sender_street)

        self.element = self.driver.find_element_by_xpath('//*[@data-validation-title="Hausnummer"]')
        self.element.send_keys(self.sender_street_number)

        self.element = self.driver.find_element_by_xpath("//*[contains(@class,'jsvRequired jsvZipNat')]")
        self.element.send_keys(self.sender_postal_code)

        self.element = self.driver.find_element_by_xpath("//*[contains(@class,'jsvRequired typeahead-city')]")
        self.element.send_keys(self.sender_city)

        self.element = self.driver.find_element_by_xpath("//*[contains(@class,'form__input jsvRequired jsvEmail')]")
        self.element.send_keys(self.sender_email)

        time.sleep(0.5)

        self.element = self.driver.find_element_by_xpath('//a[normalize-space()="Nächster Schritt"]')
        self.driver.execute_script("arguments[0].click();", self.element)
