import os
import wx
import pcbnew
import inspect

from .toolbox import get_path


class JunctionPlugin(pcbnew.ActionPlugin):
    """
    Class for implementing the junction plugin.
    """
    def __init__(self):
        pass

    def defaults(self):
        self.name = "Junction"
        self.category = "Layout"
        self.pcbnew_icon_support = hasattr(self, "show_toolbar_button")
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.sep, get_path(), 'toolbox_icons', 'chamfer.png')
        self.description = "Create junction tracks in Pcbnew."

    def Run(self):
        pass
