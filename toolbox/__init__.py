import wx
import wx.aui
import pcbnew

from . import junction
from . import chamfer
from . import taper
from . import settings


# Register junction plugin
junctionPlugin = junction.JunctionPlugin()
junctionPlugin.defaults()
junctionPlugin.register()

# Register chamfer plugin
chamferPlugin = chamfer.ChamferPlugin()
chamferPlugin.defaults()
chamferPlugin.register()

# Register taper plugin
taperPlugin = taper.TaperPlugin()
taperPlugin.defaults()
taperPlugin.register()

# Register settings plugin
settingsPlugin = settings.SettingsPlugin()
settingsPlugin.defaults()
settingsPlugin.register()
