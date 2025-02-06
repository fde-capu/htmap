from krita import Extension
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QAction

EXTENSION_ID = 'pykrita_htmap'
MENU_ENTRY = 'HTMap'
ACTION_DESCRIPTION = 'Copy selected coordinates to clipboard (HTMap).'

class Htmap(Extension):

    def __init__(self, parent):
      super().__init__(parent)
      self.action = QAction(ACTION_DESCRIPTION, parent)
      self.action.triggered.connect(self.action_triggered)

    def setup(self):
      pass

    def createActions(self, window):
      action_collection = window.createAction(ACTION_DESCRIPTION, MENU_ENTRY, "tools/scripts")
      action_collection.triggered.connect(self.action_triggered)

    def action_triggered(self):
      doc = Krita.instance().activeDocument()
      if doc is not None:
        map_area = doc.selection()
        if map_area is not None:
          lt_x, lt_y, br_x, br_y = map_area.x(), map_area.y(), map_area.x() + map_area.width(), map_area.y() + map_area.height()
          clipboard = QApplication.clipboard()
          clipboard.setText(f'{lt_x},{lt_y},{br_x},{br_y}')
        else:
          print('Nothing selected.')
      else:
        print('No document.')

Krita.instance().addExtension(Htmap(Krita.instance()))
