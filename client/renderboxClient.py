"""
Name: RenderBOX Client
Author :  Rajiv Sharma
Developer Website : www.technicaldirector.in
Developer Email   : rajiv@technicaldirector.in
Date Started : 21 April 2018
Date Modified :
Description : 

Download Application from : www.technicaldirector.in/renderbox
Source Code Website : www.github.com/vfxpipeline/zone
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
import json
import thread
from PyQt4 import QtGui
import requests
from ui import client
from lib.sysInfo import *
__author__ = 'Rajiv Sharma'


class RenderboxClientClass(QtGui.QMainWindow, client.Ui_MainWindow):
    def __init__(self, parent=None):
        super(RenderboxClientClass, self).__init__(parent)
        self.setupUi(self)
        self.__server__ = "127.0.0.1:8000"
        movie = QtGui.QMovie(":/icons/images/server.gif")
        movie.start()
        self.server_icon.setMovie(movie)
        self.repo_server_status.setPixmap(QtGui.QPixmap(":/icons/images/green.gif"))
        self.db_server_status.setPixmap(QtGui.QPixmap(":/icons/images/blue.gif"))
        # lets populate system information in gui on separate thread
        thread.start_new_thread(self.populate_client_configurations, ())
        thread.start_new_thread(self.populate_client_specifications, ())

    def closeEvent(self, *args, **kwargs):
        self.deleteLater()

    def populate_client_configurations(self):
        url = "http://{}/api/renderbox/client/".format(self.__server__)
        req = requests.get(url, data={"mac_address": mac_address()})
        client_info = json.loads(req.text)
        self.database_LE.setText(self.__server__)
        self.database_port_LE.setText('3306')
        if os_platform() == 'Windows':
            self.repo_path_LE.setText('windows_repository_path')
        if os_platform() == 'Linux':
            self.repo_path_LE.setText('linux_repository_path')
        self.client_id_LE.setText(str(client_info['id']))
        self.client_status_LE.setText(client_info['status']['name'])
        self.running_time_LE.setText(up_time())
        self.description_LE.setText('description')
        self.comment_LE.setText('comment')

    def populate_client_specifications(self):
        """
        this function will populate client specification info in user interface
        :return:
        """
        self.gpu_card_LE.setText(gpu_card())
        self.os_name_LE.setText(os_name())
        self.cpu_name_LE.setText(processor())
        self.cpu_type_LE.setText(os_arch())
        self.user_LE.setText(user())
        self.ip_address_LE.setText(ip_address())
        self.mac_address_LE.setText(mac_address())
        self.ram_LE.setText(total_ram())
        self.network_speed_LE.setText(network_speed())
        self.l2_cache_LE.setText(l2_cache())
        self.l3_cache_LE.setText(l3_cache())
        self.hostname_LE.setText(host_name())
        self.gpu_memory_LE.setText(gpu_memory())


if __name__ == '__main__':
    import sys
    client_app = QtGui.QApplication(sys.argv)
    client = RenderboxClientClass()
    client.show()
    sys.exit(client_app.exec_())
