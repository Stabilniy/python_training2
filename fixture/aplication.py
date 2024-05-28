from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from useless.method import Random
from model.article import Article
import time
import os
from fixture.session import SessionHelper
from fixture.article_creation import Article_Creation


class Aplication:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.article_creation = Article_Creation(self)

    def destroy(self):
        self.wd.quit()