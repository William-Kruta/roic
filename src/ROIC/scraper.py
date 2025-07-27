import pandas as pd
import datetime as dt

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Scraper:
    def __init__(self, headless: bool = False, wait_time: int = 5):
        self.headless = headless
        self.wait_time = wait_time
        self.driver = None
        self.wait = None

    def setup_driver(self) -> webdriver.Chrome:
        options = Options()
        if self.headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")

        # Prevent detection
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, self.wait_time)

    def create_browser(self, url: str):
        if self.driver is None:
            self.setup_driver()
        if self.driver.current_url != url:
            self.driver.get(url)

    def read_text(self, xpath: str) -> str:
        data = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        print(f"DATA: {data.text}")
        return data.text
        # data = self.driver.find_element(By.XPATH, xpath)
        # return data.text

    def read_text_by_tag(self, tag: str):
        data = self.driver.find_element(By.TAG_NAME, tag)
        return data.text

    def _scrape_table(
        self,
        min_col: int,
        max_col: int,
        base_xpath: str,
        keys: dict,
        row_index: int = 1,
        SKIP_INDEX: int = -1,
        split_cols: bool = True,
    ):
        print(f"MIN: {min_col} Max: {max_col}")
        data = {}
        running = True
        while running:
            index = 0
            try:
                for i in range(min_col, max_col + 1):
                    if i == SKIP_INDEX:
                        pass
                    else:
                        key = keys[index]
                        if split_cols:
                            key = key.split(" ")[0]
                        xpath = base_xpath.format(row_index, i)
                        text = self.read_text(xpath)
                        try:
                            data[key].append(text)
                        except KeyError:
                            data[key] = [text]
                        index += 1
            except TimeoutException:
                break
            row_index += 1
        df = pd.DataFrame(data)
        return df

    def scrape_row(self, xpath: str, min_index: int, max_index: int):
        data = []
        for i in range(min_index, max_index + 1):
            text = self.read_text(xpath.format(i))
            data.append(text)
        return data

    def get_table_labels(
        self,
        row_labels_xpath: str,
        col_labels_xpath: str,
        row_start_index: int,
        col_start_index: int,
    ):
        rows = []
        cols = []
        while True:
            try:
                xpath = row_labels_xpath.format(row_start_index)
                data = self.read_text(xpath)
                row_start_index += 1
                rows.append(data)
            except NoSuchElementException:
                break
            except TimeoutException:
                break

        while True:
            try:
                data = self.read_text(col_labels_xpath.format(col_start_index))
                col_start_index += 1
                cols.append(data)
            except NoSuchElementException:
                break
            except TimeoutException:
                break

        return rows, cols
