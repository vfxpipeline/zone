"""
Name: 
Author :  Rajiv Sharma
Developer Website : www.technicaldirector.in
Developer Email   : rajiv@technicaldirector.in
Date Started :  13 Oct 2016
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

from PyQt4 import QtGui
from ui import render_submit
from lib.sysInfo import *

__author__ = 'Rajiv Sharma'


class RenderboxSubmissionClass(QtGui.QMainWindow, render_submit.Ui_MainWindow):
    def __init__(self, parent=None):
        super(RenderboxSubmissionClass, self).__init__(parent)
        self.setupUi(self)
        self.submit_PB.clicked.connect(self.create_job)
        self.projectdir_browse.clicked.connect(self.project_browser)
        self.filepath_browse.clicked.connect(self.file_browser)
        self.dependency_browse.clicked.connect(self.dependency_browser)
        self.outputpath_browse.clicked.connect(self.output_browser)

        # self.application_CB.addItem('')

    def project_browser(self):
        dialog = QtGui.QFileDialog()
        project_name = dialog.getExistingDirectory()
        self.project_dir_LE.setText(project_name)

    def file_browser(self):
        dialog = QtGui.QFileDialog()
        file_name, filter_name = dialog.getOpenFileNameAndFilter()
        self.filepath_LE.setText(file_name)

    def dependency_browser(self):
        dialog = QtGui.QFileDialog()
        dependency_name = dialog.getOpenFileNames()
        self.dependency_LE.setText(';'.join(str(name) for name in dependency_name))

    def output_browser(self):
        dialog = QtGui.QFileDialog()
        output_dir_name = dialog.getExistingDirectory()
        self.outputpath_LE.setText(output_dir_name)

    def create_job(self):
        """
        this function will create job
        :return:
        """
        file_path = str(self.filepath_LE.text())
        if not os.path.isfile(file_path):
            QtGui.QMessageBox.about(self, 'invalid file', 'selected file name is invalid')
            return
        start_frame = self.start_frame_SB.value()
        end_frame = self.end_frame_SB.value()
        status = 0
        if self.submit_as_suspended_TB.isChecked():
            status = 5
        job = {
            'status': status,  # JOB STATUS
            'submit_time': datetime.datetime.now(),  # SUBMISSION TIME
            'start_time': datetime.datetime.now(),  # JOB START TIME
            'end_time': datetime.datetime.now(),  # JOB FINISH TIME
            'start_frame': start_frame,  # JOB START FRAME
            'end_frame': end_frame,  # JOB END FRAME
            'chunk_size': self.chunk_size_SB.value(),  # FRAME SPLIT CHUNK SIZE
            'job_category': 'maya',  # JOB CATEGORY
            'render_app': 'maya2015',  # Render application with version
            'render_plugin': 'mentalray',  # Render Plugin
            'submit_pc': host_name(),  # SUBMISSION PC NAME
            'submit_user': user(),  # SUBMIT BY USER
            'submit_ip': ip_address(),  # SUBMISSION PC IP ADDRESS
            'name': str(self.job_name_LE.text()),  # JOB NAME
            'comment': str(self.comment_LE.text()),  # JOB COMMENT
            'department': str(self.department_LE.text()),  # JOB DEPARTMENT
            'assign_clients': [],  # ASSIGN CLIENTS COMPUTER ID
            'pool': str(self.pool_CB.currentText()),  # ASSIGN POOL ID
            'group': str(self.group_CB.currentText()),  # ASSIGN GROUP ID
            'priority': self.priority_SB.value(),  # JOB PRIORITY 1 TO 100
            'on_job_complete': str(self.on_job_complete_CB.currentText()),  # TASK AFTER JOB COMPLETION
            'project_path': str(self.project_dir_LE.text()),  # JOB FILE PATH
            'file_path': file_path,  # JOB FILE PATH
            'file_size': file_size(file_path),  # JOB FILE SIZE
            'dependency': str(self.dependency_LE.text()),  # JOB FILE DEPENDENCY
            'output_path': str(self.outputpath_LE.text())  # JOB OUTPUT PATH
        }
        job_id = self.db.write('jobs', data_dict=job, mode='add')
        self.create_tasks(job_id, range(start_frame, end_frame + 1))
        self.create_log(job_id)
        QtGui.QMessageBox.about(self, 'Job Submitted', "Job is successfully submit to renderbox\n"
                                                       "JOB ID : %s" % job_id)

    def create_log(self, job_id):
        """
        this function will create a log database entry for new created job
        :param job_id:
        :return:
        """
        task = {
            'output': '',
            'error': '',
            'debug': '',
        }
        self.db.write('logs', document_name=job_id, data_dict=task, mode='add')

    def create_tasks(self, job_id, frames, chunk_size=10):
        """
        this function will create task from job
        :param job_id:
        :param frames:
        :param chunk_size:
        :return:
        """
        for task_id, frames_list in enumerate(self.split_frame_list(frames, chunk_size)):
            task = {
                'status': 0,
                'job_id': job_id,
                'task_id': task_id,
                'client_id': '',  # if status is wip than add client id
                'start_frame': frames_list[0],
                'end_frame': frames_list[-1],
                'wip_frame': 0,
                'start_time': '',
                'end_time': '',
                'queued_frames': frames_list,  # total queued task list
                'complete_frames': [],  # add completed frames
                'error_frames': [],  # add error frames here
                'process_id': 0,  # render.exe process id
                'task_progress': 0.0,  # the progress of task
                'log': ''  # the progress of task
            }
            doc_name = '{}_{}'.format(job_id, task_id)
            self.db.write('tasks', document_name=doc_name, data_dict=task, mode='add')

    @staticmethod
    def split_frame_list(frame_list, chunk_size):
        """
        this function will create frames chunks
        :param frame_list:
        :param chunk_size:
        :return:
        """
        for i in range(0, len(frame_list), chunk_size):
            yield frame_list[i:i + chunk_size]


if __name__ == '__main__':
    import sys
    submit_app = QtGui.QApplication(sys.argv)
    submit = RenderboxSubmissionClass()
    submit.show()
    sys.exit(submit_app.exec_())
