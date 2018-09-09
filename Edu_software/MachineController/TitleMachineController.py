from MachineController.EduMachineController import EduMachineController


class TitleMachineController(EduMachineController):
    def __init__(self):
        super().__init__()

    def update(self):
        print("Controller_up")
        super().update()

    def control(self):
        print("Controller_co")
        super().control()
