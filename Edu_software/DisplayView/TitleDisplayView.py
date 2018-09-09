from DisplayView.EduDisplayView import EduDisplayView


class TitleDisplayView(EduDisplayView):
    def __init__(self):
        self.count = 0
        super().__init__()

    # for calculation to draw
    def update(self):
        print("Disp_up")
        super().update()

    # actually drawing
    def draw(self):
        print("Disp_dr")
        super().draw()

