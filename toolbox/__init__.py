import wx
import wx.aui
import pcbnew

import chamfer
import taper
import settings


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
