"""
Name: RenderBOX Client
Author :  Rajiv Sharma
Developer Website : www.technicaldirector.in
Developer Email   : rajiv@technicaldirector.in
Date Started : 17 Sept 2016
Date Modified :
Description : 

Download Application from : www.technicaldirector.in/downloads
Source Code Website : www.github.com/vfxpipeline/renderbox
Free Video Tutorials : www.youtube.com/vfxpipeline

Copyright (c) 2016, RAJIV SHARMA(www.TechnicalDirector.in) . All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.

    * Neither the name of RAJIV SHARMA(www.TechnicalDirector.in) nor the names of any
      other contributors to this software may be used to endorse or
      promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import os
import subprocess
from PyQt4 import QtGui
from lib import sysInfo
__author__ = 'Rajiv Sharma'


class RenderboxClientTrayClass(object):
    def __init__(self):
        self.host_name = sysInfo.host_name()
        self.tray = QtGui.QSystemTrayIcon()
        self.tray.setIcon(QtGui.QIcon('box.ico'))
        self.tray.show()
        self.tray_menu = QtGui.QMenu()
        server_ip = self.tray_menu.addAction("RenderBOX Client ID : 55242")
        server_ip.setIcon(QtGui.QIcon('ui/images/server1.png'))
        self.tray_menu.addSeparator()
        status = self.tray_menu.addAction("Running")
        self.blink_icon_movie = QtGui.QMovie('ui/images/green.gif')
        self.blink_icon_movie.start()
        self.blink_icon_movie.frameChanged.connect(lambda: self.blink_status(status))
        open_console = self.tray_menu.addAction("Open Console")
        open_console.triggered.connect(self.show_console)
        open_console.setIcon(QtGui.QIcon('ui/images/control_panel.png'))

        submit_job = self.tray_menu.addAction("Submit Job")
        submit_job.triggered.connect(self.submit_job)
        submit_job.setIcon(QtGui.QIcon('ui/images/control_panel.png'))

        exit_renderbox = self.tray_menu.addAction("Exit")
        exit_renderbox.triggered.connect(QtGui.QApplication.quit)
        exit_renderbox.setIcon(QtGui.QIcon('ui/images/exit.png'))
        self.tray.setContextMenu(self.tray_menu)

    def blink_status(self, menu):
        """
        this function will indicate the blink status
        :param menu:
        :return:
        """
        icon = QtGui.QIcon()
        icon.addPixmap(self.blink_icon_movie.currentPixmap())
        menu.setIcon(icon)

    def show_console(self):
        """
        this function will open Renderbox Client Console
        :return:
        """
        cmd = 'c:/python27/python.exe %s/renderboxClient.py' % os.path.dirname(__file__)
        subprocess.Popen(cmd, shell=True)


    def submit_job(self):
        """
        this function will open submit job window
        :return:
        """
        cmd = 'c:/python27/python.exe %s/renderboxsubmission.py' % os.path.dirname(__file__)
        subprocess.Popen(cmd, shell=True)


if __name__ == '__main__':
    import sys
    client_app = QtGui.QApplication(sys.argv)
    client = RenderboxClientTrayClass()
    sys.exit(client_app.exec_())

