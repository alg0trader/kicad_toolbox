# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct  5 2019)
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
		_linearTaperBoxSizer = wx.BoxSizer( wx.VERTICAL )

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


		_linearTaperBoxSizer.Add( _linearTaperSettingsbSizer, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		_linearTaperImgbSizer = wx.BoxSizer( wx.VERTICAL )

		self.taperImg = wx.StaticBitmap( self.linearTaperPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 295,150 ), 0 )
		_linearTaperImgbSizer.Add( self.taperImg, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		_linearTaperBoxSizer.Add( _linearTaperImgbSizer, 1, wx.EXPAND|wx.ALL, 5 )


		self.linearTaperPanel.SetSizer( _linearTaperBoxSizer )
		self.linearTaperPanel.Layout()
		_linearTaperBoxSizer.Fit( self.linearTaperPanel )
		self.taperPanelwxNotebook.AddPage( self.linearTaperPanel, u"Linear", False )
		self.exponentialTaperPanel = wx.Panel( self.taperPanelwxNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		_exponentialTaperbSizer = wx.BoxSizer( wx.VERTICAL )


		self.exponentialTaperPanel.SetSizer( _exponentialTaperbSizer )
		self.exponentialTaperPanel.Layout()
		_exponentialTaperbSizer.Fit( self.exponentialTaperPanel )
		self.taperPanelwxNotebook.AddPage( self.exponentialTaperPanel, u"Exponential", True )
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
		self.settingsNotebook.AddPage( self._taperTrackPanel, u"Taper", False )
		self.junctionTrackPanel = wx.Panel( self.settingsNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		_junctionPanel = wx.BoxSizer( wx.VERTICAL )

		self.junctionPanelwxNotebook = wx.Notebook( self.junctionTrackPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teeJunctionPanel = wx.Panel( self.junctionPanelwxNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		_teeJunctionBoxSizer = wx.BoxSizer( wx.VERTICAL )

		_teeTaperSettingsGridSizer = wx.FlexGridSizer( 0, 4, 0, 0 )
		_teeTaperSettingsGridSizer.SetFlexibleDirection( wx.BOTH )
		_teeTaperSettingsGridSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self._teeW1StaticText = wx.StaticText( self.teeJunctionPanel, wx.ID_ANY, u"W1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._teeW1StaticText.Wrap( -1 )

		_teeTaperSettingsGridSizer.Add( self._teeW1StaticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.teeW1SpinCtrlDouble = wx.SpinCtrlDouble( self.teeJunctionPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 254, 1.000000, 1 )
		self.teeW1SpinCtrlDouble.SetDigits( 0 )
		_teeTaperSettingsGridSizer.Add( self.teeW1SpinCtrlDouble, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		teeW1UnitwxChoiceChoices = [ u"mm", u"mil", u"in" ]
		self.teeW1UnitwxChoice = wx.Choice( self.teeJunctionPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, teeW1UnitwxChoiceChoices, 0 )
		self.teeW1UnitwxChoice.SetSelection( 0 )
		_teeTaperSettingsGridSizer.Add( self.teeW1UnitwxChoice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.teeW1AutoCheckBox = wx.CheckBox( self.teeJunctionPanel, wx.ID_ANY, u"Auto", wx.DefaultPosition, wx.DefaultSize, 0 )
		_teeTaperSettingsGridSizer.Add( self.teeW1AutoCheckBox, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )

		self._teeW2StaticText = wx.StaticText( self.teeJunctionPanel, wx.ID_ANY, u"W2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._teeW2StaticText.Wrap( -1 )

		_teeTaperSettingsGridSizer.Add( self._teeW2StaticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.teeW2SpinCtrlDouble = wx.SpinCtrlDouble( self.teeJunctionPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 254, 0, 1 )
		self.teeW2SpinCtrlDouble.SetDigits( 0 )
		_teeTaperSettingsGridSizer.Add( self.teeW2SpinCtrlDouble, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		teeW2UnitwxChoiceChoices = [ u"mm", u"mil", u"in" ]
		self.teeW2UnitwxChoice = wx.Choice( self.teeJunctionPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, teeW2UnitwxChoiceChoices, 0 )
		self.teeW2UnitwxChoice.SetSelection( 0 )
		_teeTaperSettingsGridSizer.Add( self.teeW2UnitwxChoice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.teeW2AutoCheckBox = wx.CheckBox( self.teeJunctionPanel, wx.ID_ANY, u"Auto", wx.DefaultPosition, wx.DefaultSize, 0 )
		_teeTaperSettingsGridSizer.Add( self.teeW2AutoCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self._teeW3StaticText = wx.StaticText( self.teeJunctionPanel, wx.ID_ANY, u"W3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._teeW3StaticText.Wrap( -1 )

		_teeTaperSettingsGridSizer.Add( self._teeW3StaticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.teeW3SpinCtrlDouble = wx.SpinCtrlDouble( self.teeJunctionPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 254, 0, 1 )
		self.teeW3SpinCtrlDouble.SetDigits( 0 )
		_teeTaperSettingsGridSizer.Add( self.teeW3SpinCtrlDouble, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		teeW3UnitwxChoiceChoices = [ u"mm", u"mil", u"in" ]
		self.teeW3UnitwxChoice = wx.Choice( self.teeJunctionPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, teeW3UnitwxChoiceChoices, 0 )
		self.teeW3UnitwxChoice.SetSelection( 0 )
		_teeTaperSettingsGridSizer.Add( self.teeW3UnitwxChoice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.teeW3AutoCheckBox = wx.CheckBox( self.teeJunctionPanel, wx.ID_ANY, u"Auto", wx.DefaultPosition, wx.DefaultSize, 0 )
		_teeTaperSettingsGridSizer.Add( self.teeW3AutoCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self._teeLStaticText = wx.StaticText( self.teeJunctionPanel, wx.ID_ANY, u"L", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._teeLStaticText.Wrap( -1 )

		_teeTaperSettingsGridSizer.Add( self._teeLStaticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.teeLSpinCtrlDouble = wx.SpinCtrlDouble( self.teeJunctionPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 254, 0, 1 )
		self.teeLSpinCtrlDouble.SetDigits( 0 )
		_teeTaperSettingsGridSizer.Add( self.teeLSpinCtrlDouble, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		teeLengthUnitwxChoiceChoices = [ u"mm", u"mil", u"in" ]
		self.teeLengthUnitwxChoice = wx.Choice( self.teeJunctionPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, teeLengthUnitwxChoiceChoices, 0 )
		self.teeLengthUnitwxChoice.SetSelection( 0 )
		_teeTaperSettingsGridSizer.Add( self.teeLengthUnitwxChoice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.teeLAutoCheckBox = wx.CheckBox( self.teeJunctionPanel, wx.ID_ANY, u"Auto", wx.DefaultPosition, wx.DefaultSize, 0 )
		_teeTaperSettingsGridSizer.Add( self.teeLAutoCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		_teeJunctionBoxSizer.Add( _teeTaperSettingsGridSizer, 1, wx.EXPAND, 5 )


		self.teeJunctionPanel.SetSizer( _teeJunctionBoxSizer )
		self.teeJunctionPanel.Layout()
		_teeJunctionBoxSizer.Fit( self.teeJunctionPanel )
		self.junctionPanelwxNotebook.AddPage( self.teeJunctionPanel, u"Tee", False )

		_junctionPanel.Add( self.junctionPanelwxNotebook, 1, wx.EXPAND |wx.ALL, 5 )


		self.junctionTrackPanel.SetSizer( _junctionPanel )
		self.junctionTrackPanel.Layout()
		_junctionPanel.Fit( self.junctionTrackPanel )
		self.settingsNotebook.AddPage( self.junctionTrackPanel, u"Junction", True )

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
		self.teeW1SpinCtrlDouble.Bind( wx.EVT_SPINCTRLDOUBLE, self.OnTaperW1SpinCtrlDouble )
		self.teeW1UnitwxChoice.Bind( wx.EVT_CHOICE, self.OnTaperW1Unit )
		self.teeW1AutoCheckBox.Bind( wx.EVT_CHECKBOX, self.OnTaperW1Auto )
		self.teeW2SpinCtrlDouble.Bind( wx.EVT_SPINCTRLDOUBLE, self.OnTaperW2SpinCtrlDouble )
		self.teeW2UnitwxChoice.Bind( wx.EVT_CHOICE, self.OnTaperW2Unit )
		self.teeW2AutoCheckBox.Bind( wx.EVT_CHECKBOX, self.OnTaperW2Auto )
		self.teeW3SpinCtrlDouble.Bind( wx.EVT_SPINCTRLDOUBLE, self.OnTaperW2SpinCtrlDouble )
		self.teeW3UnitwxChoice.Bind( wx.EVT_CHOICE, self.OnTaperW2Unit )
		self.teeW3AutoCheckBox.Bind( wx.EVT_CHECKBOX, self.OnTaperW2Auto )
		self.teeLSpinCtrlDouble.Bind( wx.EVT_SPINCTRLDOUBLE, self.OnTaperLengthSpinCtrlDouble )
		self.teeLengthUnitwxChoice.Bind( wx.EVT_CHOICE, self.OnTaperLengthUnit )
		self.teeLAutoCheckBox.Bind( wx.EVT_CHECKBOX, self.OnTaperLengthAuto )
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


