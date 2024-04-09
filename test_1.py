from GoRESTDriver.gorest_driver import GoRESTDriver

TOKEN = '77fc5fa2cc6fa7336bd3db9afb9be6f924cbe322bb5fc438864287c0359bdd08'


driver = GoRESTDriver()
driver.generate_token(token=TOKEN)

driver.get_token_in_headers()
driver.get_token_in_url()
driver.get_via_user_and_password('admin', 'password')