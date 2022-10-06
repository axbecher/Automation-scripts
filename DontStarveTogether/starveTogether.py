import subprocess, pyautogui, time, os, sys, datetime, logging, webbrowser
from win10toast import ToastNotifier
# ------------------
#subprocess.run("start steam://run/322330", shell=True)

# Point(x=960, y=555) - Confirm click 1
# Point(x=871, y=728) - Confirm click 2

# Point(x=183, y=870) - QUIT BUTTON
# Point(x=794, y=621) - YES BUTTON
# ------------------

date_now  = datetime.datetime.now().strftime('%d_%m_%Y') 
time_stamp = datetime.datetime.now().strftime('%d-%m-%Y, %H:%M:%S > ')

if(os.path.exists(f'logs\{date_now}.log')):
    print("File exist.")
else:
    fp = open(f'{date_now}.log', 'w+')
    fp.close()
    print("File doesn't exist.")

if(os.path.exists(f'logs\{date_now}.log')):
    LOG_FILENAME = f'logs\{date_now}.log'
    format_string = '%(levelname)s: %(asctime)s > %(message)s;'
    logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
    logging.info("Start running Script")
else:
    print("Close script.")
    sys.exit()

logging.info("Start running Don't Starve Together")
subprocess.run("start steam://run/322330", shell=True)

logging.info("Wait 55 seconds")
time.sleep(55)

logging.info("Finish running Don't Starve Together")

time.sleep(1)
pyautogui.moveTo(960, 555, duration = 1)
logging.info("Move mouse in position x = 960, y = 555 for open first part of the gift")
pyautogui.click(960, 555)
logging.info("Click mouse in position x = 960, y = 555 for open first part of the gift")

time.sleep(3)
pyautogui.moveTo(871, 728, duration = 1)
logging.info("Move mouse in position x = 871, y = 728 for open second part of the gift")
pyautogui.click(871, 728)
logging.info("Click mouse in position x = 871, y = 728 for open first part of the gift")

pyautogui.moveTo(183, 870, duration = 1)
logging.info("Move mouse in position x = 183, y = 870 for QUIT Button")

pyautogui.click(183, 870)
time.sleep(1)
pyautogui.click(183, 870)
logging.info("Click mouse in position x = 183, y = 870 for QUIT Button")

time.sleep(2)
pyautogui.click(794, 621)
logging.info("Click mouse around position x = 794, y = 621 for YES Button")

time.sleep(1)
pyautogui.moveTo(792, 621, duration = 1)
logging.info("Move mouse around position x = 794, y = 621 for YES Button")
pyautogui.click(792, 621)
logging.info("Click mouse in position x = 794, y = 621 for YES Button")

time.sleep(1)
logging.info("Don't Starve Together closed")
toast = ToastNotifier()
toast.show_toast(
f"Everything done",
f"{date_now}",
duration = 2,
threaded = True,
)
webbrowser.open('https://habitica.com/', new=2)
sys.exit()


