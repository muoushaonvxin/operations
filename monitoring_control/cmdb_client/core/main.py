# -*- coding: utf8 -*-

from core.client import ClientHandler
import sys


class CmdbClientHandler(object):

    def __init__(self, sys_argv):
        self.sys_argv = sys_argv
        if len(sys_argv) < 2:
            sys.exit(u"""Please input start or stop:

                        start:          argument start is start the monitor client. 
                        stop:           argument stop is stop the monitor client.
                        collect_data:   argument stop is stop the monitor client.
                        report_asset:   reporting data.
                """)
        else:
            self.entry_command()


    def entry_command(self):
        if hasattr(self, self.sys_argv[1]):
            func = getattr(self, self.sys_argv[1])
            return func()
        else:
            print(u"请输入正确的命令!")


    def collect_data(self):
        client = ClientHandler(['start', 'collect_data'])
        data = client.collect_data()
        print(data)


    def report_asset(self):
        client = ClientHandler(['start', 'report_asset'])
        client.report_asset()


    def start(self):
        client = ClinetHandler()


    def stop(self):
        pass
