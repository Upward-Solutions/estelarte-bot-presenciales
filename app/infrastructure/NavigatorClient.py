from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import ByType, By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class NavigatorClient:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 10)

    def visit(self, url: str):
        self.driver.get(url)
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "body")))

    def click(self, by: ByType, value: str):
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def input(self, by: ByType, value: str, input_value: str):
        element = self.wait.until(EC.presence_of_element_located((by, value)))
        element.clear()
        element.send_keys(input_value)

    def find_row_in_table_by_value(self, column: int, value: str):
        rows = self._iterate_table_pages()
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            cell_value = cells[column].text.strip()
            if len(cells) > column and cell_value == value.strip():
                return row
        return None

    def _rows_in_table(self) -> list[WebElement]:
        table = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'table')))
        rows = table.find_elements(By.TAG_NAME, "tr")
        return rows

    def _iterate_table_pages(self) -> list[WebElement]:
        all_rows = []
        page_elements = self.driver.find_elements(By.CLASS_NAME, "page_class")

        for index in range(len(page_elements)):
            page_elements = self.driver.find_elements(By.CLASS_NAME, "page_class")
            page_elements[index].click()
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'table')))
            rows = self._rows_in_table()
            all_rows.extend(rows)
        return all_rows


    def close(self):
        self.driver.quit()
