# -*- encoding: utf-8 -*-
from linux import GetLinuxSysInfo
from windows import GetWindowsSysInfo


def LinuxSysInfo():
    return GetLinuxSysInfo.collect()

def WindowsSysInfo():
    return GetWindowsSysInfo.collect()