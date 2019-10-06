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

		_mainbSizer = wx.BoxSizer( wx.VERTICAL )

		self.settingsNotebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self._chamferPanel = wx.Panel( self.settingsNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.settingsNotebook.AddPage( self._chamferPanel, u"Chamfer", False )
		self._taperTrackPanel = wx.Panel( self.settingsNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		_taperPanel = wx.BoxSizer( wx.VERTICAL )

		self.taperPanelwxNotebook = wx.Notebook( self._taperTrackPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.linearTaperPanel = wx.Panel( self.taperPanelwxNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		_linearTaperbSizer = wx.BoxSizer( wx.VERTICAL )

		_linearTaperSettingsbSizer = wx.FlexGridSizer( 0, 4, 0, 0 )
		_linearTaperSettingsbSizer.SetFlexibleDirection( wx.BOTH )
		_linearTaperSettingsbSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self._taperW1StaticText = wx.StaticText( self.linearTaperPanel, wx.ID_ANY, u"W1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._taperW1StaticText.Wrap( -1 )

		_linearTaperSettingsbSizer.Add( self._taperW1StaticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.taperW1SpinCtrlDouble = wx.SpinCtrlDouble( self.linearTaperPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 254, 1.000000, 1 )
		self.taperW1SpinCtrlDouble.SetDigits( 0 )
		_linearTaperSettingsbSizer.Add( self.taperW1SpinCtrlDouble, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		taperW1UnitwxChoiceChoices = [ u"mm", u"mil", u"in" ]
		self.taperW1UnitwxChoice = wx.Choice( self.linearTaperPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, taperW1UnitwxChoiceChoices, 0 )
		self.taperW1UnitwxChoice.SetSelection( 0 )
		_linearTaperSettingsbSizer.Add( self.taperW1UnitwxChoice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.taperW1AutoCheckBox = wx.CheckBox( self.linearTaperPanel, wx.ID_ANY, u"Auto", wx.DefaultPosition, wx.DefaultSize, 0 )
		_linearTaperSettingsbSizer.Add( self.taperW1AutoCheckBox, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )

		self._taperW2StaticText = wx.StaticText( self.linearTaperPanel, wx.ID_ANY, u"W2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._taperW2StaticText.Wrap( -1 )

		_linearTaperSettingsbSizer.Add( self._taperW2StaticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.taperW2SpinCtrlDouble = wx.SpinCtrlDouble( self.linearTaperPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 254, 0, 1 )
		self.taperW2SpinCtrlDouble.SetDigits( 0 )
		_linearTaperSettingsbSizer.Add( self.taperW2SpinCtrlDouble, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		taperW2UnitwxChoiceChoices = [ u"mm", u"mil", u"in" ]
		self.taperW2UnitwxChoice = wx.Choice( self.linearTaperPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, taperW2UnitwxChoiceChoices, 0 )
		self.taperW2UnitwxChoice.SetSelection( 0 )
		_linearTaperSettingsbSizer.Add( self.taperW2UnitwxChoice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.taperW2AutoCheckBox = wx.CheckBox( self.linearTaperPanel, wx.ID_ANY, u"Auto", wx.DefaultPosition, wx.DefaultSize, 0 )
		_linearTaperSettingsbSizer.Add( self.taperW2AutoCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self._taperLStaticText = wx.StaticText( self.linearTaperPanel, wx.ID_ANY, u"L", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._taperLStaticText.Wrap( -1 )

		_linearTaperSettingsbSizer.Add( self._taperLStaticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.taperLSpinCtrlDouble = wx.SpinCtrlDouble( self.linearTaperPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 254, 0, 1 )
		self.taperLSpinCtrlDouble.SetDigits( 0 )
		_linearTaperSettingsbSizer.Add( self.taperLSpinCtrlDouble, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		taperLengthUnitwxChoiceChoices = [ u"mm", u"mil", u"in" ]
		self.taperLengthUnitwxChoice = wx.Choice( self.linearTaperPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, taperLengthUnitwxChoiceChoices, 0 )
		self.taperLengthUnitwxChoice.SetSelection( 0 )
		_linearTaperSettingsbSizer.Add( self.taperLengthUnitwxChoice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.taperLAutoCheckBox = wx.CheckBox( self.linearTaperPanel, wx.ID_ANY, u"Auto", wx.DefaultPosition, wx.DefaultSize, 0 )
		_linearTaperSettingsbSizer.Add( self.taperLAutoCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self._taperVStaticText = wx.StaticText( self.linearTaperPanel, wx.ID_ANY, u"V", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._taperVStaticText.Wrap( -1 )

		_linearTaperSettingsbSizer.Add( self._taperVStaticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.taperVSpinCtrlDouble = wx.SpinCtrlDouble( self.linearTaperPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 254, 0, 1 )
		self.taperVSpinCtrlDouble.SetDigits( 0 )
		_linearTaperSettingsbSizer.Add( self.taperVSpinCtrlDouble, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		taperVUnitwxChoiceChoices = [ u"mm", u"mil", u"in" ]
		self.taperVUnitwxChoice = wx.Choice( self.linearTaperPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, taperVUnitwxChoiceChoices, 0 )
		self.taperVUnitwxChoice.SetSelection( 0 )
		_linearTaperSettingsbSizer.Add( self.taperVUnitwxChoice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.taperVAutoCheckBox = wx.CheckBox( self.linearTaperPanel, wx.ID_ANY, u"Auto", wx.DefaultPosition, wx.DefaultSize, 0 )
		_linearTaperSettingsbSizer.Add( self.taperVAutoCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		_linearTaperbSizer.Add( _linearTaperSettingsbSizer, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		_linearTaperImgbSizer = wx.BoxSizer( wx.VERTICAL )

		self.taperImg = wx.StaticBitmap( self.linearTaperPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 300,144 ), 0 )
		_linearTaperImgbSizer.Add( self.taperImg, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		_linearTaperbSizer.Add( _linearTaperImgbSizer, 1, wx.EXPAND|wx.ALL, 5 )


		self.linearTaperPanel.SetSizer( _linearTaperbSizer )
		self.linearTaperPanel.Layout()
		_linearTaperbSizer.Fit( self.linearTaperPanel )
		self.taperPanelwxNotebook.AddPage( self.linearTaperPanel, u"Linear", True )
		self.exponentialTaperPanel = wx.Panel( self.taperPanelwxNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		_exponentialTaperbSizer = wx.BoxSizer( wx.VERTICAL )


		self.exponentialTaperPanel.SetSizer( _exponentialTaperbSizer )
		self.exponentialTaperPanel.Layout()
		_exponentialTaperbSizer.Fit( self.exponentialTaperPanel )
		self.taperPanelwxNotebook.AddPage( self.exponentialTaperPanel, u"Exponential", False )
		self.klopfensteinTaperPanel = wx.Panel( self.taperPanelwxNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		_klopfensteinTaperbSizer = wx.BoxSizer( wx.VERTICAL )


		self.klopfensteinTaperPanel.SetSizer( _klopfensteinTaperbSizer )
		self.klopfensteinTaperPanel.Layout()
		_klopfensteinTaperbSizer.Fit( self.klopfensteinTaperPanel )
		self.taperPanelwxNotebook.AddPage( self.klopfensteinTaperPanel, u"Klopfenstein", False )

		_taperPanel.Add( self.taperPanelwxNotebook, 1, wx.EXPAND |wx.ALL, 5 )


		self._taperTrackPanel.SetSizer( _taperPanel )
		self._taperTrackPanel.Layout()
		_taperPanel.Fit( self._taperTrackPanel )
		self.settingsNotebook.AddPage( self._taperTrackPanel, u"Taper", True )
		self.junctionTrackPanel = wx.Panel( self.settingsNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.settingsNotebook.AddPage( self.junctionTrackPanel, u"Junction", False )

		_mainbSizer.Add( self.settingsNotebook, 1, wx.EXPAND |wx.ALL, 5 )

		settingsButtonSizer = wx.StdDialogButtonSizer()
		self.settingsButtonSizerOK = wx.Button( self, wx.ID_OK )
		settingsButtonSizer.AddButton( self.settingsButtonSizerOK )
		self.settingsButtonSizerCancel = wx.Button( self, wx.ID_CANCEL )
		settingsButtonSizer.AddButton( self.settingsButtonSizerCancel )
		settingsButtonSizer.Realize();

		_mainbSizer.Add( settingsButtonSizer, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )


		self.SetSizer( _mainbSizer )
		self.Layout()
		_mainbSizer.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.taperW1SpinCtrlDouble.Bind( wx.EVT_SPINCTRLDOUBLE, self.OnTaperW1SpinCtrlDouble )
		self.taperW1UnitwxChoice.Bind( wx.EVT_CHOICE, self.OnTaperW1Unit )
		self.taperW1AutoCheckBox.Bind( wx.EVT_CHECKBOX, self.OnTaperW1Auto )
		self.taperW2SpinCtrlDouble.Bind( wx.EVT_SPINCTRLDOUBLE, self.OnTaperW2SpinCtrlDouble )
		self.taperW2UnitwxChoice.Bind( wx.EVT_CHOICE, self.OnTaperW2Unit )
		self.taperW2AutoCheckBox.Bind( wx.EVT_CHECKBOX, self.OnTaperW2Auto )
		self.taperLSpinCtrlDouble.Bind( wx.EVT_SPINCTRLDOUBLE, self.OnTaperLengthSpinCtrlDouble )
		self.taperLengthUnitwxChoice.Bind( wx.EVT_CHOICE, self.OnTaperLengthUnit )
		self.taperLAutoCheckBox.Bind( wx.EVT_CHECKBOX, self.OnTaperLengthAuto )
		self.taperVSpinCtrlDouble.Bind( wx.EVT_SPINCTRLDOUBLE, self.OnTaperLengthSpinCtrlDouble )
		self.taperVUnitwxChoice.Bind( wx.EVT_CHOICE, self.OnTaperLengthUnit )
		self.taperVAutoCheckBox.Bind( wx.EVT_CHECKBOX, self.OnTaperLengthAuto )
		self.settingsButtonSizerOK.Bind( wx.EVT_BUTTON, self.OnOKSettingsButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnTaperW1SpinCtrlDouble( self, event ):
		event.Skip()

	def OnTaperW1Unit( self, event ):
		event.Skip()

	def OnTaperW1Auto( self, event ):
		event.Skip()

	def OnTaperW2SpinCtrlDouble( self, event ):
		event.Skip()

	def OnTaperW2Unit( self, event ):
		event.Skip()

	def OnTaperW2Auto( self, event ):
		event.Skip()

	def OnTaperLengthSpinCtrlDouble( self, event ):
		event.Skip()

	def OnTaperLengthUnit( self, event ):
		event.Skip()

	def OnTaperLengthAuto( self, event ):
		event.Skip()




	def OnOKSettingsButtonClick( self, event ):
		event.Skip()


