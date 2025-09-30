#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools, shelltools, get

WorkDir="."
def setup():
    shelltools.system("unzip uyap-pardus-5-4-14-amd6403-06-20251-41-pm.zip")
    shelltools.system("ar xvf uyap_pardus_5_4_14_amd64/uyapeditor_5.4.14_amd64.deb")
    shelltools.system("tar xvf data.tar.xz")

def install():
    pisitools.insinto("/usr", "%s/usr/*" % get.workDIR())

    #fixed the authentication problem.
    shelltools.system("chmod -R 0755 %s/usr/share/UYAPEditor/*" % get.installDIR())
