if __name__ == '__main__':
    from time import sleep
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium_driver_updater import DriverUpdater
    import undetected_chromedriver as uc
    import os

    base_dir = os.path.dirname(os.path.abspath(__file__))
    list_drivers = [DriverUpdater.chromedriver]

    drivers = DriverUpdater.install(path=base_dir, driver_name=list_drivers, upgrade=True, check_driver_is_up_to_date=True, old_return=False)
    service = Service(drivers[0])
    options = Options()
    options.headless = False

    driver = uc.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 10)

    email = ""
    password = ""

    def login():
        driver.get('https://google.com/gmail')

        wait.until(EC.element_to_be_clickable((By.ID,'identifierId'))).send_keys(email)
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="identifierNext"]'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input'))).send_keys(password)
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="passwordNext"]'))).click()

    try:
        login()
    finally:
        driver.quit()