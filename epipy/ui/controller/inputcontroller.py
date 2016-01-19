from epipy.ui.view.inputgroupbox import InputGroupBox


class InputController(object):
    def __init__(self, parent):
        self.parent = parent
        self.input_group_box = InputGroupBox()
        self.parent.main_view.h_splitter.insertWidget(2, self.input_group_box)
