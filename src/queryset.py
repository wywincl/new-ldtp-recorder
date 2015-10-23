#!/usr/bin/env python
"""
ldtp-recorder

@author: Wang Yang <wywincl@gmail.com>
@copyright: Copyright (c) 2015-2016 Wang Yang
@license: GPLv3

See 'LICENSE' in the source distribution for more information.
"""

import pyatspi


# Judge the point(x,y) is in area.
def _is_in_area(x, y, xx, yy, width, height):
    if xx <= x <= xx + width and yy <= y <= yy + height:
        return True
    return False


# Get the active window object.
def _get_active_window():
    desktop = pyatspi.Registry.getDesktop(0)
    for app in desktop:
        for window in app:
            if window.getState().contains(pyatspi.STATE_ACTIVE) and window.getState().contains(pyatspi.STATE_SHOWING):
                return window


# Get all Component Information.
def _get_all_role_position(root, result):
    coords = root.queryComponent().getExtents(0)
    # print root.get_role_name(), root.name, coords.x, coords.y, coords.width, coords.height
    info = (root, coords.x, coords.y, coords.width, coords.height)
    result.append(info)
    for tree in root:
        _get_all_role_position(tree, result)


# Get All Active Component Information.
def get_active_role_info():
    frame = _get_active_window()
    result = []
    _get_all_role_position(frame, result)
    return result


# Get All Active Components which in the given area position.
def get_in_area_role_info(x, y, result):
    filter_result = []
    for i in result:
        if _is_in_area(x, y, i[1], i[2], i[3], i[4]):
            # print i
            filter_result.append(i)
    return filter_result


def main_test():
    print get_active_role_info()


if __name__ == '__main__':
    main_test()
