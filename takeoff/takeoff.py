# TakeOff - Initial run tool for CorvOS
import gi
import time
import os
import threading
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
GObject.threads_init()

# Create Global GTK Object varaibles
builder = Gtk.Builder()
builder.add_from_file("takeoff.glade")
stubutton = builder.get_object("button1")
teachbutton = builder.get_object("button2")
spinner = builder.get_object("spinner1")
mainbox = builder.get_object("box1")
infolabel = builder.get_object("infolabel")
window = builder.get_object("applicationwindow1")

# Complete Button Signal Event
def onComButtonPressed(self, *args):
    Gtk.main_quit()

# Create Complete Button
combutton = Gtk.Button("Complete")
combutton.set_halign(Gtk.Align.CENTER)
combutton.set_property("width-request", 100)
combutton.set_property("height-request", 50) 
mainbox.add(combutton)
combutton.connect("clicked", onComButtonPressed)

# Thread Handler
class StudentThread(threading.Thread):
    def __init__(self, callback):
        threading.Thread.__init__(self)
        self.callback = callback

    def run(self):
        time.sleep(4) # Run the Student Setup Script Here
        GObject.idle_add(self.callback)

class TeacherThread(threading.Thread):
    def __init__(self, callback):
        threading.Thread.__init__(self)
        self.callback = callback

    def run(self):
        time.sleep(4) # Run the Teacher Setup Script Here
        GObject.idle_add(self.callback)


# Main GTK event handler
class Handler:

    def onDestroy(self, *args):
        Gtk.main_quit()

    def onStuButtonPressed(self, button1):
        infolabel.set_text("Getting everything setup...")
        teachbutton.hide()
        stubutton.hide()
        spinner.start()
        thread = StudentThread(self.work_finished_cb)
        thread.start()

    def onTeachButtonPressed(self, button2):
        infolabel.set_text("Getting everything setup...")
        teachbutton.hide()
        stubutton.hide()
        spinner.start()
        thread = TeacherThread(self.work_finished_cb)
        thread.start()



    def work_finished_cb(self):
        spinner.stop()
        infolabel.set_text("Ready to Go!")
        combutton.show()


builder.connect_signals(Handler())
window.show_all()
combutton.hide()
Gtk.main()
