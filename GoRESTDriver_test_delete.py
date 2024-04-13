from GoRESTDriver.gorest_driver import GoRESTDriver

TOKEN = '77fc5fa2cc6fa7336bd3db9afb9be6f924cbe322bb5fc438864287c0359bdd08'


driver = GoRESTDriver()
driver.generate_token(token=TOKEN)
driver.login('admin',  'password')

#
# def test_delete_user_via_user_and_password():
#     response = driver.delete_user_via_user_and_password('test_name', 'male', 'test_emial11311@wp.pl', 'active')
#     assert response['id']


def test_delete_user_via_token_in_url():
    driver.delete_user_via_token_in_url(6837391)


def test_delete_user_token_in_headers():
    driver.delete_user_token_in_headers(6798330)


if __name__ == '__main__':
    test_delete_user_via_token_in_url()
    # test_delete_user_token_in_headers()
    # test_delete_user_via_user_and_password()  # Not Working
