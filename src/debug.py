#!/usr/bin/env python
"""
ldtp-recorder

@author: Wang Yang <wywincl@gmail.com>
@copyright: Copyright (c) 2015-2016 Wang Yang
@license: GPLv3

See 'LICENSE' in the source distribution for more information.
"""

import os

''' export LDTP_RECORDER_DEBUG=LVL '''

''' set LDTP_RECORDER_DEBUG to 5 to see all events' role '''
LVL_ALL_ROLES = 5
''' set LDTP_RECORDER_DEBUG to 9 to see all events (heavy spam) '''
LVL_ALL_EVENTS = 9


try:
    level = int(os.getenv('LDTP_RECORDER_DEBUG'))
except TypeError:
    level = None
except ValueError:
    level = None

