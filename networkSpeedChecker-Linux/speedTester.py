#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:53:46 2015
@author: priyesh
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 14:36:59 2015
This Program can be used to monitor download Speed ...!!!
@author: priyesh
"""
import psutil
import time
import threading
from PyQt4.QtGui import *
from PyQt4.QtCore import * 
import sys
class Main_window(QWidget):
    def __init__(self):
        super(Main_window,self).__init__()
        self.init_ui()
    def init_ui(self):
        self.move(500,300)
        self.resize(200,100)
        self.lab1=QLabel(self)
        self.lab1.move(50,10)
        self.lab1.setText("Download Speed")
        self.lab2=QLabel(self)
        self.lab2.move(50,30)
        self.lab2.setMinimumWidth(100)
        self.connect(self,SIGNAL("mysignal"),self.lab2.setText)
        self.setWindowTitle('Speed Viewer')
        self.show()
    

exit_flag=0
def get_download(ex):
    t0=time.time()
    counter = psutil.net_io_counters(pernic=True)["eth0"]
    d0=counter.bytes_recv
    while True:
        if exit_flag==1:
            exit(0)
        counter = psutil.net_io_counters(pernic=True)["eth0"]
        d1=counter.bytes_recv
        t1=time.time()
        dl=(d1-d0)/(t1-t0)/1000
        d0=d1
        t0=time.time()
        if dl > 1000 :
            dl=dl/1000
            print "%.2f" %dl,"mbps"
        else:
            dl1=str("%.2f" %dl)+"kbps"
            ex.emit(SIGNAL("mysignal"), str(dl1))
        time.sleep(2)
def run_app():
    app = QApplication(sys.argv)
    ex = Main_window()
    global exit_flag
    try:
        t=threading.Thread(target=get_download,args=(ex,))
        t.start()
    except KeyboardInterrupt:
        exit_flag=1
    
    app.exec_()
    exit_flag=1
    print "Exiting"

run_app()