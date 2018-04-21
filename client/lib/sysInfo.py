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
import os
import time
import platform
import psutil
import getpass
import datetime
import socket
import subprocess
import uuid
from time import strftime


def host_name():
    return socket.gethostname()


def ip_address():
    return socket.gethostbyname(socket.gethostname())


def mac_address():
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac = ':'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
    return mac


def iso_datetime():
    return datetime.datetime.now()


def full_date_time():
    return strftime("%a, %d %b %Y %H:%M:%S")


def date():
    return strftime("%d %b %Y")


def day_date():
    return strftime("%a, %d %b %Y")


def current_time():
    return strftime("%H:%M:%S")


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    :param num:
    :return:
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def user():
    """
    get user name
    :return:
    """
    return getpass.getuser()


def total_ram():
    """
    get Physical RAM
    :return:
    """
    return convert_bytes(psutil.virtual_memory()[0])


def available_ram():
    return convert_bytes(psutil.virtual_memory()[1])


def ram_usage_percent():
    """
    get Physical RAM
    :return:
    """
    return psutil.virtual_memory()[2]


def used_ram():
    return convert_bytes(psutil.virtual_memory()[3])


def free_ram():
    return convert_bytes(psutil.virtual_memory()[4])


def cpu_usage():
    """
    get Processor information
    :return:
    """
    return psutil.cpu_percent(interval=1)


def boot_time():
    """
    Get system boot time
    :return:
    """
    b_time = psutil.get_boot_time()
    return datetime.datetime.fromtimestamp(b_time).strftime("%Y-%m-%d %H:%M:%S")


def disc_usages():
    """
    get Disk Usages
    :return:
    """
    return psutil.disk_usage('/home/rajiv')


def os_platform():
    """
    This function will return OS Platform
    :return:
    """
    return platform.system()


def os_name():
    if os_platform() == 'Windows':
        import wmi
        import pythoncom
        pythoncom.CoInitialize()
        computer = wmi.WMI()
        os_info = computer.Win32_OperatingSystem()[0]
        return os_info.Name.encode('utf-8').split('|')[0]
    if platform.system() == 'Linux':
        os_name = subprocess.check_output('cat /etc/redhat-release', shell=True)
        return os_name.strip()


def os_arch():
    if os_platform() == 'Windows':
        import wmi
        computer = wmi.WMI()
        os_info = computer.Win32_OperatingSystem()[0]
        return os_info.OSArchitecture
    if platform.system() == 'Linux':
        os_arch = subprocess.check_output('arch', shell=True)
        return os_arch.strip()


def processor():
    """
    this function will return the processor name of system
    :return:
    """
    if os_platform() == 'Windows':
        import wmi
        computer = wmi.WMI()
        proc_info = computer.Win32_Processor()[0]
        return proc_info.Name
    if os_platform() == 'Linux':
        processor_name = subprocess.check_output("lscpu | grep 'Model name'", shell=True)
        return processor_name.split(':')[1].strip()


def processor_core():
    if platform.system() == 'Windows':
        import wmi
        computer = wmi.WMI()
        proc_info = computer.Win32_Processor()[0]
        core = proc_info.NumberOfCores
        return core
    if os_platform() == 'Linux':
        core = subprocess.check_output("lscpu | grep 'Core'", shell=True)
        return core.split(':')[1].strip()


def l2_cache():
    if platform.system() == 'Windows':
        import wmi
        computer = wmi.WMI()
        proc_info = computer.Win32_Processor()[0]
        cache = proc_info.L2CacheSize
        return str(cache)
    if os_platform() == 'Linux':
        cache = subprocess.check_output("lscpu | grep 'L2 cache'", shell=True)
        return str(cache)


def l3_cache():
    if platform.system() == 'Windows':
        import wmi
        computer = wmi.WMI()
        proc_info = computer.Win32_Processor()[0]
        cache = proc_info.L3CacheSize
        return str(cache)
    if os_platform() == 'Linux':
        cache = subprocess.check_output("lscpu | grep 'L3 cache'", shell=True)
        return str(cache)


def gpu_card():
    if platform.system() == 'Windows':
        import wmi
        computer = wmi.WMI()
        gpu_info = computer.Win32_VideoController()[0]
        return str(gpu_info.Name)
    if os_platform() == 'Linux':
        graphics_card = subprocess.check_output("lspci | grep 'VGA'", shell=True)
        return graphics_card.split('compatible controller:')[1].strip()


def gpu_memory():
    if platform.system() == 'Windows':
        import wmi
        import pythoncom
        pythoncom.CoInitialize()
        computer = wmi.WMI()
        gpu_info = computer.Win32_VideoController()[0]
        mem = abs(gpu_info.AdapterRAM)
        return str(convert_bytes(mem))
    if os_platform() == 'Linux':
        graphics_card = subprocess.check_output("lspci | grep 'VGA'", shell=True)
        return graphics_card


def disc_partitions():
    """
    this function will return the all disc partition information
    :return:
    """
    return psutil.disk_partitions()


def up_time():
    """
    this function will return the system uptime
    how long the computer in running
    :return:
    """
    seconds = time.time() - psutil.boot_time()
    return str(datetime.timedelta(seconds=seconds))


def video_card():
    if os_platform() == 'Windows':
        import wmi
        computer = wmi.WMI()
        gpu_info = computer.Win32_VideoController()[0]
        return gpu_info.Name


def network_speed():
        if platform.system() == 'Windows':
            net_info = subprocess.check_output('wmic NIC where NetEnabled=true get speed', shell=True)
            speed = str(net_info).split('Speed')[1]
            speed = speed.strip().split()[0]
            return str(convert_bytes(int(speed))) + '/s'
        if platform.system() == 'Linux':
            return 'xxx'
            # network_interface = subprocess.check_output("route | grep '^default' | grep -o '[^ ]*$'", shell=True)
            # speed = subprocess.check_output("ethtool {}  | grep -i speed".format(network_interface.strip()), shell=True)
            # return str(speed).strip()


def file_size(file_path):
    """
    this function will return the file size
    :param file_path:
    :return:
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)
