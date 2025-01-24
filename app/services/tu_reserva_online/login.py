from selenium.webdriver.common.by import By

from app.infrastructure.NavigatorClient import NavigatorClient


def login():
    client.visit("https://tureservaonline.app/iniciar-sesion/")
    client.input(By.ID, "bookneticsaas_email", "info@estelarte.com.ar")
    client.input(By.ID, "bookneticsaas_password", "Caladari24")
    client.click(By.CLASS_NAME, "bookneticsaas_login_btn")


if __name__ == "__main__":
    client = NavigatorClient()
    try:
        login()
        client.click(By.XPATH, "//a[span[text()='Servicios']]")
        client.find_row_in_table_by_value(2, "RESINA EPOXI")
    finally:
        client.close()
