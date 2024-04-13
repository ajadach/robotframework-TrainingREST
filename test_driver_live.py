from Driver_Live.driver_live import driver_live
import json

DRIVER_LIVE = driver_live()

DRIVER_LIVE.generate_token('admin', 'pwd')
# test 1
# test 2
# test 3

# DRIVER_LIVE.get()
# DRIVER_LIVE.get(6850627)

# file_name = 'user_data_2.json'
# with open(file_name, "r") as file:
#     body = json.load(file)

# DRIVER_LIVE.post(body['name'], body['gender'], body['email'], body['status'])
# DRIVER_LIVE.post(**body)

DRIVER_LIVE.patch(6850727, **{'name': 'arczi'})
res = DRIVER_LIVE.get(6850727)
assert res['name'] == 'arczi'


#DRIVER_LIVE.post('Artur', 'male', 'asd@wp.pl', 'active')

DRIVER_LIVE.delete(6850727)

# DRIVER_LIVE.patch()
# DRIVER_LIVE.delete()
#
#
# DRIVER_LIVE.generate_token('arczi', '1234')
# test 1
# test 2
# test 3
