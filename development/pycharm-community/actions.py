#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools

WorkDir = "."
NoStrip = ["/"]

def install():
    pisitools.insinto("/opt/pycharm-community", "pycharm-2025.2/*")
    pisitools.dosym("/opt/pycharm-community/bin/pycharm.sh", "/usr/bin/pycharm-community")