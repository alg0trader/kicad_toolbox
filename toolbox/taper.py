import os
import wx
import pcbnew
import inspect

from .toolbox import get_path


class TaperPlugin(pcbnew.ActionPlugin):
    """
    Class for implementing the taper plugin.
    """
    def __init__(self):
        pass
    
    def defaults(self):
        self.name = "Taper"
        self.category = "Layout"
        self.pcbnew_icon_support = hasattr(self, "show_toolbar_button")
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.sep, get_path(), 'toolbox_icons', 'taper.svg')
        self.description = "Route tapered tracks in Pcbnew."
    
    def Run(self):
        pass
