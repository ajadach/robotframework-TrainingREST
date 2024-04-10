from GoRESTDriver.gorest_driver import GoRESTDriver

TOKEN = '77fc5fa2cc6fa7336bd3db9afb9be6f924cbe322bb5fc438864287c0359bdd08'


driver = GoRESTDriver()
driver.generate_token(token=TOKEN)
driver.login('admin',  'password')


def test_create_user_via_user_and_password():
    response = driver.create_user_via_user_and_password('test_name', 'male', 'test_emial1111@wp.pl', 'active')
    assert response['id']


def test_create_user_via_token_in_url():
    response = driver.create_user_via_token_in_url('test_name', 'male', 'test_emial113311@wp.pl', 'active')
    assert response['id']


def test_create_user_token_in_headers():
    response = driver.create_user_token_in_headers('test_name', 'male', 'test_emial11121@wp.pl', 'active')
    assert response['id']


if __name__ == '__main__':
    test_create_user_via_token_in_url()
    test_create_user_token_in_headers()
    test_create_user_via_user_and_password()  # Not Working
