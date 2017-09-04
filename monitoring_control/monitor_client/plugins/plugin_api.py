from .linux import linux_network
from .windows import windows_network


def GetLinuxCpuStatus():
	pass

def GetNginxStatus():
	pass

def GetLinuxMemStatus():
	pass

def GetLinuxNetworkStatus():
	return linux_network.monitor()

def GetMySQLStatus():
	pass