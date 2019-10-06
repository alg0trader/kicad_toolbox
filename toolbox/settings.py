import os
import wx
import pcbnew
import inspect

import gui
from .toolbox import get_path


class SettingsPlugin(pcbnew.ActionPlugin):
    """
    Class for implementing the settings plugin feature.
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
            dlg = gui.SettingsDialog()
            if dlg.ShowModal() == wx.ID_OK:
                # Check for active window
                pass
            else:
                # Dialog cancelled
                pass
        finally:
            if dlg: dlg.Destroy()
