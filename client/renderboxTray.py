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
import thread
import requests
from PyQt4 import QtGui
from lib.sysInfo import *

__author__ = 'Rajiv Sharma'


class RenderboxClientTrayClass(object):
    def __init__(self):
        self.__server__ = "127.0.0.1:8000"
        self.tray = QtGui.QSystemTrayIcon()
        self.tray.setIcon(QtGui.QIcon('box.ico'))
        self.tray.show()
        self.tray_menu = QtGui.QMenu()
        server_ip = self.tray_menu.addAction("Server : " + self.__server__)
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
        thread.start_new_thread(self.register_client, ())
        thread.start_new_thread(self.sync_data, ())

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

    def register_client(self):
        data = {
            "description": 'Renderbox client node activated',
            "status": 1,
            "os_platform": os_platform(),
            "os_name": os_name(),
            "os_username": user(),
            "os_arch": os_arch(),
            "host_name": host_name(),
            "idle_time": 0.0,
            "rendering_time": 0.0,
            "up_time": up_time(),
            "cpu_name": processor(),
            "cpu_core": processor_core(),
            "l2_cache": l2_cache(),
            "l3_cache": l3_cache(),
            "cpu_usage": cpu_usage(),
            "total_ram": total_ram(),
            "ram_usage": ram_usage_percent(),
            "available_ram": available_ram(),
            "gpu_card": gpu_card(),
            "gpu_memory": gpu_memory(),
            "network_adapter": 'None',
            "network_speed": network_speed(),
            "ip_address": ip_address(),
            "mac_address": mac_address(),
            "client_register_time": str(datetime.datetime.now())
        }
        url = "http://{}/api/renderbox/client/".format(self.__server__)
        requests.post(url, data=data)

    def sync_data(self):
        """
        this function will sync client computer data with server
        :return:
        """
        url = "http://{}/api/renderbox/client/".format(self.__server__)
        while True:
            data = {
                "up_time": up_time(),
                "cpu_usage": cpu_usage(),
                "ram_usage": ram_usage_percent(),
                "available_ram": available_ram(),
                "gpu_memory": gpu_memory(),
                "network_speed": network_speed(),
                "mac_address": mac_address(),
            }
            req = requests.put(url, data=data)
            print(req.status_code, data)
            time.sleep(2)


if __name__ == '__main__':
    import sys

    client_app = QtGui.QApplication(sys.argv)
    client = RenderboxClientTrayClass()
    sys.exit(client_app.exec_())
