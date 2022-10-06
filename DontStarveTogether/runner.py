import logging
import tkinter as tk
import time
from tkinter import filedialog
import wmi # pip install wmi
import subprocess
import os, sys
import datetime
import webbrowser
from win10toast import ToastNotifier

# ~ 35 secunde pana la lansarea Steam completa

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 160)
canvas1.pack()

f = wmi.WMI()

date_now  = datetime.datetime.now().strftime('%d_%m_%Y') 
time_stamp = datetime.datetime.now().strftime('%d-%m-%Y, %H:%M:%S > ')
log_path = f"logs\{date_now}.log"
LOG_FILENAME = log_path

if(os.path.exists(log_path)):
    format_string = '%(levelname)s: %(asctime)s > %(message)s;'
    logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
    logging.info("Verified, log file exists.")
    
    toast = ToastNotifier()
    toast.show_toast(
    f"File exist, abort.",
    f"Log file found for {date_now}",
    duration = 4,
    threaded = True,
    )

    sys.exit()
else:
    fp = open(log_path, 'w+')
    fp.close()
    format_string = '%(levelname)s: %(asctime)s > %(message)s;'
    logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
    logging.info("Verified failed, create log file")

    def LansareJoc():
        
        gamePath = "starveTogether.py"
        steamConfigPath = "configs/steamConfig.txt"
        
        if(os.stat(steamConfigPath).st_size == 0):
            configFile = open(steamConfigPath,"w+")
            toast = ToastNotifier()
            toast.show_toast(
            f"Steam Location",
            f"Select steam.exe",
            duration = 5,
            threaded = True,
            )
            steamExe = filedialog.askopenfilename()
            configFile.write(steamExe)
            configFile.close()
            steamExeLoc = open(steamConfigPath,"r+")
            steamPath = steamExeLoc.readline()
            new_steamPath = steamPath.replace( '/', '\\' )
            configFile = open(steamConfigPath,"w+")
            configFile.write(new_steamPath)
            configFile.close()
            steamLocation = new_steamPath
            format_string = '%(levelname)s: %(asctime)s > %(message)s;'
            logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
            logging.info("Steam Location not found, need to update it")
        else:
            steamExeLoc = open(steamConfigPath,"r+")
            steamPath = steamExeLoc.readline()
            new_steamPath = steamPath.replace( '/', '\\' )
            configFile = open(steamConfigPath,"w+")
            configFile.write(new_steamPath)
            configFile.close()
            steamLocation = new_steamPath
            format_string = '%(levelname)s: %(asctime)s > %(message)s;'
            logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
            logging.info("Steam Location found")
        import psutil
        def checkIfProcessRunning(processName):
            '''
            Check if there is any running process that contains the given name processName.
            '''
            #Iterate over the all the running process
            for proc in psutil.process_iter():
                try:
                    # Check if process name contains the given name string.
                    if processName.lower() in proc.name().lower():
                        return True
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            return False

        if checkIfProcessRunning('steam.exe'):
            canvas1.pack()
            time.sleep(1)

            format_string = '%(levelname)s: %(asctime)s > %(message)s;'
            logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
            logging.info("Steam verified passed, launch script..")

            subprocess.call(["python", gamePath])
            sys.exit()
        else:
            time.sleep(1)
            os.startfile(steamLocation)

            format_string = '%(levelname)s: %(asctime)s > %(message)s;'
            logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
            logging.info("Steam verified failed, locate and launch Steam..")

            time.sleep(12)
            subprocess.call(["python", gamePath])

            format_string = '%(levelname)s: %(asctime)s > %(message)s;'
            logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
            logging.info("Steam verified passed, launch script..")
            
            canvas1.pack()
            sys.exit()
        
    def HelpMe():
        readmeLocation = "readme.txt"
        os.startfile(readmeLocation)
        
    def Habitica():
        webbrowser.open('https://habitica.com/', new=2)

    debugInfo = "(!) Welcome."
    button1 = tk.Button (root, text="1. START",command=LansareJoc,bg='brown',fg='white')
    button2 = tk.Button (root, text="2. HELP",command=HelpMe,bg='grey',fg='black')
    button3 = tk.Button (root, text="3. HABITICA",command=Habitica,bg='purple',fg='white')
    
    canvas1.create_window(150, 30, window=button1) #DontStarveTogether
    canvas1.create_window(150, 70, window=button2) #Help
    canvas1.create_window(150, 110, window=button3) #Habitica
    
    root.resizable(False, False)
    root.mainloop()
    