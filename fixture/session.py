from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, nickname, password):
        wd = self.app.wd
        WebDriverWait(wd, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//header/div[1]/nav[1]/div[2]/a[1]')))[0].click()
        time.sleep(5)
        email = WebDriverWait(wd, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//input[@id='user-login']")))
        email[0].send_keys(nickname)
        password_field = WebDriverWait(wd, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//input[@id='user-pass']")))
        password_field[0].send_keys(password)
        WebDriverWait(wd, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//button[@id='login-submit']")))[0].click()
        time.sleep(5)
