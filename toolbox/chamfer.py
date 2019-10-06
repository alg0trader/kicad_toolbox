import os
import wx
import pcbnew
import inspect

from . import gui_base
from .toolbox import get_path


class ChamferPlugin(pcbnew.ActionPlugin):
    """
    Class for implementing the chamfer plugin.
    """
    def __init__(self):
        pass
    
    def defaults(self):
        self.name = "Chamfer"
        self.category = "Layout"
        self.pcbnew_icon_support = hasattr(self, "show_toolbar_button")
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.sep, get_path(), 'toolbox_icons', 'chamfer.svg')
        self.description = "Route chamfered tracks in Pcbnew."
    
    def Run(self):
        pass


class ChamferTabUI(gui_base.SettingsDialogBase):
    """
    Class for applying chamfer UI overrided methods.
    """
    def __init__(self):
        pass