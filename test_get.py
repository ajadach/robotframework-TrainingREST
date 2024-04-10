from GoRESTDriver.gorest_driver import GoRESTDriver

TOKEN = '77fc5fa2cc6fa7336bd3db9afb9be6f924cbe322bb5fc438864287c0359bdd08'


driver = GoRESTDriver()
driver.generate_token(token=TOKEN)
driver.login('admin',  'password')


def test_token_in_headers():
    response = driver.get_token_in_headers()
    assert response[0]['id']


def test_token_in_url():
    response = driver.get_token_in_url()
    assert response[0]['id']


def test_via_user_pwd():
    response = driver.get_via_user_and_password()
    assert response[0]['id']


if __name__ == '__main__':
    test_token_in_headers()
    test_token_in_url()
    test_via_user_pwd()
