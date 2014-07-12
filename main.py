#!/usr/bin/python

import wx

class MainFrame(wx.Frame):

	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, 'UCfE - Ultimate Compiler for Everything' , size = (500,500))
		self.Center()
		
		mainpanel = wx.Panel(self)
		mainpanel.SetBackgroundColour('white')
		
		#edit-panels creation{
		input_text = wx.TextCtrl(mainpanel, pos = (10,45), size=(480,200), style=wx.TE_MULTILINE)
		output_text = wx.TextCtrl(mainpanel, pos = (10,290), size=(480,200), style=wx.TE_MULTILINE)
		output_text.SetEditable(False)
		#edit-panels creation}
		
		#submit_btn creation{
		logoImageFile = 'submit_button.png'
		logoImage_make = wx.Image(logoImageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		logoImage = wx.BitmapButton(mainpanel, id=-1, bitmap=logoImage_make, pos=(229, 246), size = (logoImage_make.GetWidth()+7, logoImage_make.GetHeight()+7), style = wx.NO_BORDER)
		#self.Bind(wx.EVT_BUTTON, self.compile, logoImage)
		#submit_btn creation}
		
		#dropdownbox creation{
		parse_options = ['Morse-Code','Binary-Code (n/a)', 'Leetspeak (n/a)']
		wx.ComboBox(mainpanel, -1, pos=(10, 10), size=(150, 25), choices=parse_options, style=wx.CB_READONLY)
		#dropdownbox creation}
		
#run-it
if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = MainFrame(parent=None, id=-1)
	frame.Show()
	app.MainLoop()
