import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose language")
    parser.addoption('--attach_type', action='store', default=None, help="Choose Attach_type")
    parser.addoption('--file_extension', action='store', default=None, help="Choose Attach_type")

@pytest.fixture
def choose_status(request):
    return request.config.getoption("attach_type")

@pytest.fixture
def choose_extension(request):
    return request.config.getoption("file_extension")

def test_main_page(choose_status):
    MainPage().go_to_login_page(choose_status)
    MainPage().go_to_login_page(choose_extension)




@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if user_language:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)
        yield browser
    else:
        raise pytest.UsageError("--choose your language again")
    browser.quit()

    
    
