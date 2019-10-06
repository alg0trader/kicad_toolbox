# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class SettingsDialogBase
###########################################################################

class SettingsDialogBase ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Toolbox Settings", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		mainbSizer = wx.BoxSizer( wx.VERTICAL )

		self.settingsNotebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chamferPanel = wx.Panel( self.settingsNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.settingsNotebook.AddPage( self.chamferPanel, u"Chamfer", True )
		self.taperPanel = wx.Panel( self.settingsNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.settingsNotebook.AddPage( self.taperPanel, u"Taper", False )
		self.junctionPanel = wx.Panel( self.settingsNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.settingsNotebook.AddPage( self.junctionPanel, u"Junction", False )

		mainbSizer.Add( self.settingsNotebook, 1, wx.EXPAND |wx.ALL, 5 )

		settingsButtonSizer = wx.StdDialogButtonSizer()
		self.settingsButtonSizerOK = wx.Button( self, wx.ID_OK )
		settingsButtonSizer.AddButton( self.settingsButtonSizerOK )
		self.settingsButtonSizerCancel = wx.Button( self, wx.ID_CANCEL )
		settingsButtonSizer.AddButton( self.settingsButtonSizerCancel )
		settingsButtonSizer.Realize();

		mainbSizer.Add( settingsButtonSizer, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )


		self.SetSizer( mainbSizer )
		self.Layout()
		mainbSizer.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.settingsButtonSizerOK.Bind( wx.EVT_BUTTON, self.OnOKSettingsButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnOKSettingsButtonClick( self, event ):
		event.Skip()


