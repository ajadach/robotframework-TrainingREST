# -*- coding: utf-8 -*-
from GoRESTDriver.drivers.TokenHeader import TokenHeader
from GoRESTDriver.drivers.TokenURL import TokenURl
from GoRESTDriver.drivers.UserPwd import UserPwd


class GoRESTDriver(TokenURl, TokenHeader, UserPwd):
    """ Driver to support REST API: https://gorest.co.in/public/v2/users"""

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_DOC_FORMAT = 'ROBOT'

