# -*- coding: utf-8 -*-
import time

from fixture.aplication import Aplication
import pytest

@pytest.fixture
def app(request):
    fixture = Aplication()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_app_dynamics_job(app):
        app.article_creation.open_homepage()
        app.session.login(nickname='scc@adyax.net', password='YU8gH(Xq$AS%rmRf')
        app.article_creation.article_to_create()
        time.sleep(10)

