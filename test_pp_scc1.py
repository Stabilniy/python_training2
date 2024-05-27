# -*- coding: utf-8 -*-
from selenium import webdriver
import pytest
import time
import os

from aplication import Aplication
import pytest

@pytest.fixture
def app(request):
    fixture = Aplication()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_app_dynamics_job(app):
        app.open_homepage()
        app.login(nickname='scc@adyax.net', password='YU8gH(Xq$AS%rmRf')
        app.article_creation()
        time.sleep(10)

