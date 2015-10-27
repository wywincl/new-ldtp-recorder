#!/usr/bin/env python
"""
new-ldtp-recorder

@author: Wang Yang <wywincl@gmail.com>
@copyright: Copyright (c) 2015-2016 Wang Yang
@license: GPLv3

See 'LICENSE' in the source distribution for more information.
"""

import pyatspi


def get_role_property(action_info):
    role = action_info.role
    # print dir(role)
    try:
        actions = []
        name = role.name
        role_name = role.get_role_name()
        description = role.get_description()
        focusable = role.getState().contains(pyatspi.STATE_FOCUSABLE)
        sensitive = role.getState().contains(pyatspi.STATE_SENSITIVE)
        visible = role.getState().contains(pyatspi.STATE_VISIBLE)
        checked = role.getState().contains(pyatspi.STATE_CHECKED)
        showing = role.getState().contains(pyatspi.STATE_SHOWING)

        if hasattr(role, 'queryAction'):
            try:
                action = role.queryAction()
                for i in range(action.nActions):
                    actions.append(action.getName(i))
            except NotImplementedError:
                pass

        role_property = {
            'name': name,
            'role_name': role_name,
            'description': description,
            'focusable': focusable,
            'sensitive': sensitive,
            'visible': visible,
            'checked': checked,
            'showing': showing,
            'actions': actions
        }

        return role_property
    except AttributeError:
        raise


def show_get_attributes(role):
    if hasattr(role, 'get_text'):
        print 'get_text ', role.get_text()
    if hasattr(role, 'get_current_value'):
        print 'get_current_value', role.get_current_value()
    if hasattr(role, 'get_value'):
        print 'get_value', role.get_value()
    if hasattr(role, 'get_id'):
        print 'get_id ', role.get_id()
