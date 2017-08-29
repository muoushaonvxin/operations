# -*- encoding: utf-8 -*-

from linux import *
from windows import *

def LinuxSysInfo():
    return sysinfo.collect()