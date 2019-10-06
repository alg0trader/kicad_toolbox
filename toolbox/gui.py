import wx
import wx.aui

from . import gui_base


class ChamferTab():
    """
    Class for methods associated with the curve-tab in the settings dialog window.
    """
    def __init__(self):
        pass


class TaperTab():
    """
    Class for methods associated with the taper-tab in the settings dialog window.
    """
    def __init__(self):
        pass


class JunctionTab():
    """
    Class for methods associated with the junction-tab in the settings dialog window.
    """
    def __init__(self):
        pass


class SettingsDialog(gui_base.SettingsDialogBase):
    """
    Class for inheriting dialog base class.
    """
    def __init__(self):
        gui_base.SettingsDialogBase.__init__(self, None)

        self.Centre()
    
    # Hack for new wxFormBuilder generating code incompatible with old wxPython
    # noinspection PyMethodOverriding
    def SetSizeHints(self, sz1, sz2):
        try:
            # wxPython 3
            self.SetSizeHintsSz(sz1, sz2)
        except TypeError:
            # wxPython 4
            super(SettingsDialog, self).SetSizeHints(sz1, sz2)
