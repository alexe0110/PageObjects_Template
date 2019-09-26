import os
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--server", action="store", default="r", help="Server for test")


@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Firefox()
    yield browser
    browser.quit()
