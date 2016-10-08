#!/usr/bin/python

from daemon import runner

from pir import *
from subprocess import call
from email_notification import *
import sys
import datetime
import os
import ftplib
import time
from sms_sender import *
import pygame
from settings import *

pir = PassiveInfraredSensor(PIR_PIN)

GPIO.setmode(GPIO.BCM)

notifier = EmailNotification(EMAIL_SERVER, EMAIL_USER, EMAIL_PWD)


class App():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/foo.pid'
        self.pidfile_timeout = 5
        
    def run(self):
        print "Alarm started..."
        last_state = False

        cpt = 5
        while True:

            if (pir.motion_detected() == True):
                # AJOUTER
                
                if (last_state == False):
                    
                    t = datetime.datetime.now().strftime("%A_%d_%m_%Y")
                   
                    img_name = static_folder+"photos/"+ t +"_%d.jpg" % cpt

                   
                    send_sms("Alarme "+t)
                    
                    call(["raspistill", "-o", img_name, "--nopreview"])

                    # video de 5 sec
                    time.sleep(5)
                    call(["raspivid", "-o", static_folder+"photos/vid_%d.h264" % cpt, "-t", "5000", "-fps", "5", "--nopreview"])
                    time.sleep(5)

                    # send email with img
                    notifier.send(img_name)
                   
                    
                    time.sleep(5)
                                
                    #if (cpt > 4):
                        #send_ftp
                        # time.sleep(8)
                        # del_photos("photos")

                    cpt += 1
                    
                    last_state = True
            else:
                if (last_state == True):
                    time.sleep(1)
                    last_state = False;


app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
