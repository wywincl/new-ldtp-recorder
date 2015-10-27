#!/usr/bin/env python
"""
new-ldtp-recorder

@author: Wang Yang <wywincl@gmail.com>
@copyright: Copyright (c) 2015-2016 Wang Yang
@license: GPLv3

See 'LICENSE' in the source distribution for more information.
"""
import logging

import debug
from pymouse import PyMouseEvent
from queryset import get_active_role_info, get_in_area_role_info
from generator import get_ldtp_command
from actions import get_action_info
from utils import get_role_property


class EventRecorder(PyMouseEvent):
    """
    Mouse Event Listener.
    """
    def __init__(self):
        super(EventRecorder, self).__init__()
        self._callback = None
        logging.basicConfig(filename='/tmp/ldtp.script', level=logging.DEBUG)

    def move(self, x, y):
        pass

    def click(self, x, y, button, press):
        try:
            if button == 1:
                if press:
                    # logging.info('{ "event": "click", "type": "press", "x": "' + str(x) + '", "y": "' + str(y) + '"}')
                    pass
                else:
                    # result = get_in_area_role_info(int(x), int(y), get_active_role_info())
                    # generate_ldtp_script(result)
                    self._on_event(x, y)
            else:
                print 'you stop the ldtp-recorder...'
                self.stop()
        except AttributeError:
            error_message = ' >_< ,something error, will stop the ldtp-recorder...'
            # self.stop()
            print error_message
            logging.debug(error_message)
            # pass

    def _on_event(self, x, y):
        result = get_in_area_role_info(int(x), int(y), get_active_role_info())
        action_info = get_action_info(result)
        # print 'on_event_', action_info
        if action_info:
            cmd = get_ldtp_command(action_info)
            role_property = get_role_property(action_info)
            if self._callback is None:
                print(cmd)
                print(role_property)
                logging.info(cmd)
            else:
                self._callback(cmd)

        if debug.level:
            if debug.level == debug.LVL_ALL_ROLES:
                print result
            elif debug.level == debug.LVL_ALL_EVENTS:
                print action_info

    def set_on_action_callback(self, callback):
        self._callback = callback

