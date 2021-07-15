import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class TestOrderplaneticket():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    # scenario: create transaction for flight product from search until choose payment method with non-login user
    def test_orderplaneticket(self):
        self.driver.get("https://www.tiket.com/")
        self.driver.set_window_size(1680, 20000)

        # SET DEPARTURE TO JAKARTA
        self.driver.find_element(
            By.CSS_SELECTOR, ".from-input > .product-search-input-label").click()
        self.driver.find_element(
            By.ID, "productSearchFrom").send_keys("Jakarta")
        self.driver.find_element(
            By.ID, "productSearchFrom").send_keys(Keys.ENTER)

        # SET DESTINATION TO SURABAYA
        self.driver.find_element(
            By.ID, "productSearchTo").send_keys("surabaya")
        self.driver.find_element(By.ID, "productSearchTo").send_keys(Keys.DOWN)
        self.driver.find_element(
            By.ID, "productSearchTo").send_keys(Keys.ENTER)

        # SET START DATE TO 22 JULY 2021
        self.driver.find_element(
            By.CSS_SELECTOR, "#startDate .product-search-input-label").click()

        element = self.driver.find_element(
            By.CSS_SELECTOR, ".CalendarMonthGrid_month__horizontal:nth-child(2) tr:nth-child(4) > .CalendarDay:nth-child(5) .widget-date-picker-date-content")
        element.location_once_scrolled_into_view

        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, ".CalendarMonthGrid_month__horizontal:nth-child(2) tr:nth-child(4) > .CalendarDay:nth-child(5) .widget-date-picker-date-content").click()

        # SET END DATE TO 29 JULY 2021
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, ".CalendarMonthGrid_month__horizontal:nth-child(2) tr:nth-child(5) > .CalendarDay:nth-child(5) .widget-date-picker-date-content").click()

        time.sleep(1)
        element = self.driver.find_element(
            By.CSS_SELECTOR, ".passenger-cabin-drop-down-content-container")
        element.location_once_scrolled_into_view

        # CHOOSE KELAS KABIN TO "BISNIS"
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "#passengerCabin > div.widget-drop-down > div > div > div.passenger-cabin-drop-down-content-container > div:nth-child(2) > div:nth-child(3)").click()

        # CLICK "SELESAI" TO CLOSE PENUMPANG & KELAS KABIN DIALOG
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, ".passenger-cabin-drop-down-text > span").click()

        # CLICK "CARI PENERBANGAN"
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, ".product-form-search-btn").click()

        # CLICK BUTTON "MENGERTI" TO CLOSE INFORMATION COACHMARK DIALOG
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".v3-btn__blue").click()

        # CHOOSE FIRST RECOMMENDED DEPARTURE AIRPLANE
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "div:nth-child(1) > .wrapper-flight-list .v3-btn").click()

        # CHOOSE FIRST RECOMMENDED RETURN AIRPLANE
        time.sleep(1)
        WebDriverWait(self.driver, 30000).until(expected_conditions.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "div:nth-child(1) > .wrapper-flight-list .v3-btn"), "PILIH"))

        self.driver.find_element(
            By.CSS_SELECTOR, "div:nth-child(1) > .wrapper-flight-list .v3-btn").click()
        time.sleep(1)

        # WAIT UNTIL ORDER DETAIL PAGE IS LOADED
        WebDriverWait(self.driver, 30000).until(expected_conditions.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "h3"), "Detail Pemesan"))

        # SET TITLE TO "TUAN"
        self.driver.find_element(
            By.CSS_SELECTOR, ".contact-person-dropdown > .title-flight-dropdown").click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "div.row.contact-name div.list-menu.list-menu-flight-dropdown> ul > li:nth-child(1)").click()

        # SET NAME OF ORDER DETAIL TO "JOHN DOE"
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-xs-9 .input-list-autocomplete").send_keys("John Doe")

        # SET EMAIL OF ORDER DETAIL TO "JOHNDOE@MAIL.COM"
        self.driver.find_element(
            By.NAME, "cp-email").send_keys("johndoe@mail.com")

        # SET PHONE NUMBER OF ORDER DETAIL TO "8123456789"
        self.driver.find_element(By.NAME, "cp-phone").send_keys("8123456789")

        # SCROLL AND TOGGLE "SAMA DENGAN PEMESAN" BUTTON OF PASSENGER DETAIL
        element = self.driver.find_element(
            By.CSS_SELECTOR, ".wrapper-passenger-details")
        element.location_once_scrolled_into_view

        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".thumb").click()

        # SET COUNTRY OF PASSENGER TO INDONESIA IF EXIST
        element = self.driver.find_element(
            By.CSS_SELECTOR, ".tix-core-country-dropdown .title-flight-dropdown-searchbox")

        if (element is not None):
            time.sleep(1)
            self.driver.find_element(
                By.CSS_SELECTOR, ".tix-core-country-dropdown .title-flight-dropdown-searchbox").click()

            time.sleep(1)
            self.driver.find_element(
                By.CSS_SELECTOR, ".filter > input").click()

            self.driver.find_element(
                By.CSS_SELECTOR, ".filter > input").send_keys("indonesia")

            time.sleep(1)
            self.driver.find_element(
                By.CSS_SELECTOR, "div.list-menu.list-menu-flight-dropdown-searchbox > ul > li").click()

        # SCROLL AND CLICK "LANJUTKAN KE PEMBAYARAN" BUTTON
        element = self.driver.find_element(By.CSS_SELECTOR, ".v3-btn")
        element.location_once_scrolled_into_view

        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".v3-btn").click()

        # MAKE SURE THE CONFIRMATION DIALOG SHOWS UP
        WebDriverWait(self.driver, 3000).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".notification")))

        # CLICK CONFIRM BUTTON IN THE DIALOG
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".v3-btn__blue").click()

        # MAKE SURE PAYMENT METHOD PAGE IS LOADED
        WebDriverWait(self.driver, 30000).until(expected_conditions.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".page-title"), "Metode Pembayaran"))

        # SCROLL AND CHOOSE "BNI VIRTUAL ACCOUNT" AS A PAYMENT METHOD
        element = self.driver.find_element(
            By.CSS_SELECTOR, ".payment-methods-list:nth-child(4) a:nth-child(5)")
        element.location_once_scrolled_into_view

        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, ".payment-methods-list:nth-child(4) a:nth-child(5)").click()

        # MAKE SURE PAYMENT DETAIL PAGE IS LOADED
        self.driver.execute_script("window.scrollTo(0,0)")

        WebDriverWait(self.driver, 30000).until(expected_conditions.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".page-title"), "BNI Virtual Account"))

        # CONFIRM PAYMENT METHOD
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "div.payment-button-next-step > button").click()

        # ASSERT PAYMENT IS DONE
        WebDriverWait(self.driver, 30000).until(expected_conditions.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".primary"), "LIHAT DAFTAR PESANAN"))
        assert self.driver.find_element(
            By.CSS_SELECTOR, ".primary").text == "LIHAT DAFTAR PESANAN"
