#!/usr/bin/env python
"""
new-ldtp-recorder

@author: Wang Yang <wywincl@gmail.com>
@copyright: Copyright (c) 2015-2016 Wang Yang
@license: GPLv3

See 'LICENSE' in the source distribution for more information.
"""


class ActionInfo(object):
    def __init__(self, name=None, value=None, role=None, window_name=None):
        self.name = name
        self.value = value
        self.role = role
        self.window_name = window_name

    def __str__(self):
        result = ''
        for key in ['name', 'value', 'window_name', 'role']:
            value = getattr(self, key)
            if value:
                result += '%s <%s>' % (key, value)
        return result


def get_action_info(event_source):
    try:
        if 0 != len(event_source):
            top_role = event_source[0][0]
            bottom_role = event_source[-1][0]

            window_name = top_role.name
            name = bottom_role.name
            # value = bottom_role.get_current_value()
            value = ''
            role = bottom_role

            # print 'action info: ', window_name, name, value, role

            action_info = ActionInfo(name=name, value=value, role=role, window_name=window_name)
            return action_info
        else:
            # return '<!> this action has not implemented, opening soon...'
            return None
    except Exception:
        raise
