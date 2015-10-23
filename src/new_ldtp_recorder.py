#!/usr/bin/env python
"""
new-ldtp-recorder

@author: Wang Yang <wywincl@gmail.com>
@copyright: Copyright (c) 2015-2016 Wang Yang
@license: GPLv3

See 'LICENSE' in the source distribution for more information.
"""

import sys

import gui
import recorder


if __name__ == '__main__':
    if 'gui' in sys.argv:
        gui.Gui()
    else:
        rec = recorder.EventRecorder()
        rec.capture = False
        rec.daemon = False
        try:
            rec.start()
        except KeyboardInterrupt:
            rec.stop()
