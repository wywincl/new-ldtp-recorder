#!/usr/bin/env python
"""
new-ldtp-recorder

@author: Wang Yang <wywincl@gmail.com>
@copyright: Copyright (c) 2015-2016 Wang Yang
@license: GPLv3

See 'LICENSE' in the source distribution for more information.
"""
import pyatspi
from constants import *


def _strip(s):
    if s is None:
        return ''
    return s.replace(' ', '')


def get_ldtp_command(action_info):
    """
    @type action_info: ActionInfo
    @rtype: string
    """
    if action_info is None:
        return None

    role = action_info.role
    role_name = role.get_role_name()

    # print type(role_name), role_name
    # print type(ROLE_PUSH_BUTTON), ROLE_PUSH_BUTTON
    # print "role name: ", role_name, type(role_name)

    if role_name == ROLE_CHECK_BOX:
        if role.get_state_set().contains(pyatspi.STATE_CHECKED):
            cmd = 'check'
        else:
            cmd = 'uncheck'

        return "ldtp.%s('%s', '%s')" % (
            cmd,
            _strip(action_info.window_name),
            _strip(action_info.name))

    elif role_name == ROLE_COMBO_BOX:
        return "ldtp.comboselect('%s', '%s', '%s')" % (
            _strip(action_info.window_name),
            _strip(action_info.name),
            _strip(action_info.value))

    elif role_name in [ROLE_COLOR_CHOOSER, ROLE_FILE_CHOOSER, ROLE_FONT_CHOOSER, ROLE_DIALOG, ROLE_FRAME]:
        cmd = 'waittillguiexist'
        return "ldtp.%s('%s')" % (cmd,
                                  _strip(action_info.window_name))

    elif role_name == ROLE_PAGE_TAB:
        return "ldtp.selecttab('%s', '%s', '%s')" % (
            _strip(action_info.window_name),
            _strip(action_info.name),
            _strip(action_info.value))

    elif role_name == ROLE_MENU:
        return "ldtp.selectmenuitem('%s', '%s')" % (
            _strip(action_info.window_name),
            _strip(action_info.name))

    elif role_name == ROLE_PUSH_BUTTON or role_name == ROLE_TOGGLE_BUTTON:
        return "ldtp.click('%s', '%s')" % (
            _strip(action_info.window_name),
            _strip(action_info.name))

    elif role_name == ROLE_SPIN_BUTTON:
        return "ldtp.setvalue('%s', '%s', %s)" % (
            _strip(action_info.window_name),
            _strip(action_info.name),
            _strip(action_info.value))

    elif role_name == ROLE_TEXT:
        return "ldtp.settextvalue('%s', '%s', %s)" % (
            _strip(action_info.window_name),
            _strip(action_info.name),
            _strip(action_info.value))

    elif role_name == ROLE_TABLE_CELL:
        return "ldtp.selectrow('%s', '%s', %s)" % (
            _strip(action_info.window_name),
            _strip(action_info.name),
            _strip(action_info.value))
    else:
        return str(action_info)
