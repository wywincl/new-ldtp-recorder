from gi.repository import Gtk
from recorder import EventRecorder


class Gui(object):
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file('gui.glade')
        self.event = None
        window = builder.get_object('window1')
        window.connect('delete-event', Gtk.main_quit)
        window.show_all()

        btnStart = builder.get_object('btnStart')
        btnStart.connect('clicked', self.onStartClick)

        btnStop = builder.get_object('btnStop')
        btnStop.connect('clicked', self.onStopClick)

        self.textView = builder.get_object('textview')

        Gtk.main()

    def actionCallback(self, string):
        print 'on action call back'
        print string
        self.textView.get_buffer().insert_at_cursor(string + "\n")

    def onStartClick(self, toolButton):
        self.textView.get_buffer().insert_at_cursor("starting\n")
        self._listener()
        # self.event.join()

    def onStopClick(self, toolButton):
        self.textView.get_buffer().insert_at_cursor("stopping\n")
        self.event.stop()

    def _listener(self):
        self.event = EventRecorder()
        self.event.set_on_action_callback(self.actionCallback)
        self.event.daemon = True
        self.event.start()


if __name__ == '__main__':
    Gui()
