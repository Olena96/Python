import pytest
from selenium import webdriver

@pytest.fixture
def chrome():
    driver = webdriver.Chrome(executable_path=r"C:\Users\Olena Filchak\Desktop\Python courses\lesson_17\
    chromedriver.exe")
    yield driver
    driver.quit()