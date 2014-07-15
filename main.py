#!/usr/bin/python

import wx

class MainFrame(wx.Frame):

	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, 'UCfE - Ultimate Compiler for Everything' , size = (500,500))
		
		self.initGUI()
		self.Centre()
		self.Show()
		
	def initGUI ( self ):
		
		global mainpanel
		global f_size
		global f_width
		global f_height
		global Image_btn
		global input_text
		global output_text
		global dropdown
		
		mainpanel = wx.Panel(self)
		mainpanel.Show()
		mainpanel.Raise()
		#mainpanel.SetBackgroundColour('skyblue3')
		self.Bind(wx.EVT_SIZE, self.onSize)
		
		vbox = wx.BoxSizer(wx.VERTICAL)
##########Drop-Down########################################################################//-->
		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		parse_options = ['Morse-Code','Binary-Code (n/a)', 'Leetspeak (n/a)']
		dropdown = wx.ComboBox(mainpanel, -1,'-None-', size=(175, 25), choices=parse_options, style=wx.CB_READONLY|wx.TE_PROCESS_ENTER)
		hbox1.Add(dropdown, flag=wx.RIGHT, border=8)
		self.Bind(wx.EVT_COMBOBOX, self.onComboSelection, dropdown)
		self.Bind(wx.EVT_TEXT_ENTER, self.onCompile, dropdown)
		
		vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
##########Input-Text############################################################################//-->		
		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		input_text =  wx.TextCtrl(mainpanel, style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
		hbox2.Add(input_text, proportion=1, flag=wx.EXPAND)
       		vbox.Add(hbox2, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.TOP|wx.EXPAND, border=10)
       		self.Bind(wx.EVT_TEXT_ENTER, self.onCompile, input_text)
       		
       		vbox.Add((-1, 35))
##########Output-Text############################################################################//-->		 
		hbox4 = wx.BoxSizer(wx.HORIZONTAL) 
		output_text =  wx.TextCtrl(mainpanel, style=wx.TE_MULTILINE)
		output_text.SetEditable(False)
		output_text.SetBackgroundColour('#ebebeb')
		hbox4.Add(output_text, proportion=1, flag=wx.EXPAND)
		vbox.Add(hbox4, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, border=10)
		
		mainpanel.SetSizer(vbox)	
##########Submit-Button############################################################################//-->		
		ImageFile = 'submit_button.png'
		Image_make = wx.Image(ImageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		Image_btn = wx.BitmapButton(mainpanel, id=-1, bitmap=Image_make, pos=(0,0), size = ((Image_make.GetWidth()+7), (Image_make.GetHeight()+7)), style = wx.NO_BORDER)
		self.Bind(wx.EVT_BUTTON, self.onCompile, Image_btn)
				
	def onSize(self, event):
		event.Skip()
		mainpanel.SetSize(self.GetClientSizeTuple())
			
		f_size = wx.Window.GetClientSize( self )
		f_width = f_size[0]
		f_height = f_size[1]
		print f_size
		print f_width
		print f_height 		
		
		x = f_width*0.5 - 20 
		y = (f_height*0.5 - 20) + 19
		postuple = (x, y)
		Image_btn.SetPosition( postuple )
		
	def onCompile(self, event):
		in_str = input_text.GetValue()
		print in_str
		current_select = dropdown.GetValue()
		
		compiler(in_str, current_select)
		
#		if current_select == 'Morse-Code':
#			test()
#			#parseMorseCode()
#			output_text.SetForegroundColour('black')
#			out_str = in_str
#			output_text.SetValue( out_str )
#			pass
#			
#		elif current_select == 'Binary-Code (n/a)':
#			#parseBinaryCode()	
#			output_text.SetForegroundColour('black')
#			out_str = in_str
#			output_text.SetValue( out_str )
#			pass
#			
#		elif current_select == 'Leetspeak (n/a)':
#			#parseLeetSpeak()
#			output_text.SetForegroundColour('black')	
#			out_str = in_str
#			output_text.SetValue( out_str )
#			pass
#		
#		else:
#			output_text.SetForegroundColour('Red')
#			out_str = '!-- Please select a Code to Compile to  --!'
#			output_text.SetValue( out_str )	
			
	
	def onComboSelection(self, event):
		current_select = dropdown.GetValue()
		print current_select		
			

def test():
	print 'it works'
		
#run-it
if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = MainFrame(parent=None, id=-1)
	frame.Show()
	app.MainLoop()
