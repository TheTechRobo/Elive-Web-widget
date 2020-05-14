#!/usr/bin/python3
# -*- coding:utf-8 -*-


import inspect
import os
import gi
from signal import signal, SIGINT, SIG_DFL
from subprocess import Popen
from sys import exit
try:
    # python 3
    from urllib.request import urlopen, pathname2url
except ImportError:
    # python 2
    from urllib import urlopen, pathname2url
from webbrowser import open_new_tab
from json import dumps as to_json
gi.require_version('WebKit2', '4.0')
from gi.repository import WebKit2, Gtk
window = Gtk.Window()
webview = WebKit2.WebView()
webview.load_uri("http://wttr.in/?format=v2")
window.set_title("WeatherWidg")
window.set_default_size(800,600)
window.add(webview)
window.show_all()
window.connect("destroy",Gtk.main_quit)
Gtk.main()
