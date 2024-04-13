from GoRESTDriver.gorest_driver import GoRESTDriver

TOKEN = '77fc5fa2cc6fa7336bd3db9afb9be6f924cbe322bb5fc438864287c0359bdd08'


driver = GoRESTDriver()
driver.generate_token(token=TOKEN)
driver.login('admin',  'password')

#
# def test_update_user_via_user_and_password():
#     response = driver.update_user_via_user_and_password('test_name', 'male', 'test_emial11311@wp.pl', 'active')
#     assert response['id']


def test_update_user_via_token_in_url():
    response = driver.update_user_via_token_in_url(6798324, 'test_name', 'male', 'test_emial12154343311@wp.pl', 'active')
    assert response['id']


def test_update_user_token_in_headers():
    response = driver.update_user_token_in_headers(6798324, 'test_name', 'male', 'test_3emial514311421@wp.pl', 'active')
    assert response['id']


if __name__ == '__main__':
    # test_update_user_via_token_in_url()
    test_update_user_token_in_headers()
    # test_update_user_via_user_and_password()  # Not Working
