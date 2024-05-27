from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from useless.method import Random
from article import Article
import time
import os


class Aplication:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def article_submit(self, article_obj):
        wd = self.wd
        # __fill title
        #ran1 = Random()
        title = WebDriverWait(wd, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//input[@id='edit-title-0-value']")))
        title[0].send_keys(article_obj.title)
        # __fill type
        select_type = WebDriverWait(wd, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//select[@id='edit-field-type']")))
        select = Select(select_type[0])
        select.select_by_visible_text(article_obj.type)
        # __fill image
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, "test_image2.jpg")
        file_input = WebDriverWait(wd, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//input[@id='edit-field-image-0-upload']")))
        file_input[0].send_keys(file_path)
        # __Apply_button
        modal = WebDriverWait(wd, 10).until(EC.visibility_of_all_elements_located((By.XPATH,"/html[1]/body[1]/div[2]/div[1]/main[1]/div[3]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/details[1]/div[1]/fieldset[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/details[1]/div[1]/div[1]/div[1]/div[1]/div[1]")))[0]
        input_field = modal.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/main[1]/div[3]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/details[1]/div[1]/fieldset[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/details[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
        input_field.click()
        # __Submit
        WebDriverWait(wd, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//input[@id='edit-submit']")))[0].click()

    def article_creation(self):
        wd = self.wd
        self.content_page()
        WebDriverWait(wd, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//body/div[2]/div[1]/main[1]/div[3]/div[1]/ul[1]/li[1]/a[1]/span[1]")))[0].click()
        self.article_submit(Article(title=Random().ran(), type="Actualité"))

    def content_page(self):
        wd = self.wd
        WebDriverWait(wd, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//a[@id='toolbar-item-administration']")))[0].click()
        time.sleep(5)
        WebDriverWait(wd, 10).until(EC.visibility_of_all_elements_located((By.XPATH,"//body/div[@id='toolbar-administration']/nav[@id='toolbar-bar']/div[3]/div[1]/nav[1]/div[1]/ul[1]/li[2]/div[1]/a[1]")))[0].click()
        WebDriverWait(wd, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//body/div[2]/div[1]/main[1]/div[3]/div[1]/ul[1]/li[1]/a[1]")))[0].click()

    def login(self, nickname, password):
        wd = self.wd
        WebDriverWait(wd, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//header/div[1]/nav[1]/div[2]/a[1]')))[0].click()
        time.sleep(2)
        email = WebDriverWait(wd, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//input[@id='user-login']")))
        email[0].send_keys(nickname)
        password_field = WebDriverWait(wd, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//input[@id='user-pass']")))
        password_field[0].send_keys(password)
        WebDriverWait(wd, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//button[@id='login-submit']")))[0].click()
        time.sleep(5)

    def cookie_accepting(self):
        wd = self.wd
        element = WebDriverWait(wd, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@id="popup-buttons"]/button[3]')))
        element[0].click()

    def open_homepage(self):
        wd = self.wd
        wd.get("https://scc:scc2017@preprod.centrale-canine.fr/")
        self.cookie_accepting()

    def destroy(self):
        self.wd.quit()