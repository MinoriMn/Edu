from ContentMaster.EduContentMaster import EduContentMaster


class TitleContentMaster(EduContentMaster):
    def __init__(self, display_view, machine_controller):
        super().__init__(display_view, machine_controller)

    def update(self):
        print("Content_up")
        self.machineController.update()
