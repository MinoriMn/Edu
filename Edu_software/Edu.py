import threading
import time
import atexit

from ContentMaster.EduContentMaster import EduContentMaster
from ContentMaster.TitleContentMaster import TitleContentMaster

from DisplayView.EduDisplayView import EduDisplayView
from DisplayView.TitleDisplayView import TitleDisplayView

from MachineController.EduMachineController import EduMachineController
from MachineController.TitleMachineController import TitleMachineController

import Julius_receiver


# the All master
def EduStartUp():
    global eduDisplayView
    global eduMachineController
    global eduContentMaster

    global contentControlThread

    eduDisplayView = TitleDisplayView()
    eduMachineController = TitleMachineController()
    eduContentMaster = TitleContentMaster(display_view=eduDisplayView, machine_controller=eduMachineController)

    contentControlThread = threading.Thread(target=ContentControl, name='content_control_thread')
    # displayControlThread = threading.Thread(target=DisplayControl, name='display_control_thread')

    # スレッド起動
    _readyThread()

    # julius起動
    Julius_receiver.julius_receiver()


# スレッド起動
def _readyThread():
    contentControlThread.start()
    # displayControlThread.start()


# contentスレッドループ
def ContentControl():
    while contentControlThreadROOP:
        eduContentMaster.update()
        eduDisplayView.update() #
        time.sleep(1)


# displayスレッドループ
def DisplayControl():
    while displayControlThreadROOP:
        eduDisplayView.update()
        time.sleep(1)


def EduExit():
    print("finished")
    exit()


# Edu
eduDisplayView = EduDisplayView()
eduMachineController = EduMachineController()
eduContentMaster = EduContentMaster(display_view=eduDisplayView, machine_controller=eduMachineController)

contentControlThreadROOP = True
displayControlThreadROOP = True

EduStartUp()
atexit.register(EduExit)
