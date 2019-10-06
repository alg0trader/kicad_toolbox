import os
import wx
import pcbnew
import inspect

from . import gui_base
from .toolbox import get_path


class SettingsPlugin(pcbnew.ActionPlugin):
    """
    Class for implementing the settings plugin.
    """
    def defaults(self):
        self.name = "Settings"
        self.category = "Layout"
        self.pcbnew_icon_support = hasattr(self, "show_toolbar_button")
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.sep, get_path(), 'toolbox_icons', 'settings.png')
        self.description = "Adjust Toolbox settings."
    
    def Run(self):
        dlg = False
        
        try:
            dlg = SettingsUIDialog()
            if dlg.ShowModal() == wx.ID_OK:
                # Check for active window
                pass
            else:
                # Dialog cancelled
                pass
        finally:
            if dlg: dlg.Destroy()


class SettingsUIDialog(gui_base.SettingsDialogBase):
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
            super(SettingsUIDialog, self).SetSizeHints(sz1, sz2)