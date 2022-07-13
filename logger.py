import logging as lg
import os
'''This class will be used everywhere to create log files'''


class logger:
    def logfile_creation(self, logfile):
        lg.basicConfig(filename=os.path.basename(logfile)+".log", level=lg.INFO, format="%(asctime)s: %(levelname)s: %(message)s")

    def logfile_info(self, in_msg):
        lg.info(in_msg)

    def logfile_error(self, in_msg):
        lg.error(in_msg)
