#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr", "/opt"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf softmaker-office-2018_960-01_amd64.deb")
    shelltools.system("tar xf data.tar.xz")

def install():
    pisitools.insinto("/", "usr")
