#!/usr/bin/python

import wx, time

class helloworld (wx.Frame):
	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, '-Nerd.Gasum-', size = (500, 500))
		self.Center()
		
		global txtpanel		
		global mrsepanel
		global mainpanel
		
		panel = wx.Panel(self)
		
		mainpanel = wx.Panel( panel )
		mainpanel.SetBackgroundColour('white')

		txtpanel = wx.Panel(panel)
		txtpanel.Hide()
		txtpanel.Raise()
		txtpanel.SetBackgroundColour('white')
		self.Bind(wx.EVT_SIZE, self.onSize)		

		mrsepanel = wx.Panel(panel)
		mrsepanel.SetBackgroundColour('white')

		mrsepanel.Hide()
		mainpanel.Show()
		
###################menubar#######################{
		menubar = wx.MenuBar()
		menubar.SetBackgroundColour('#7EC0EE')
		file_menu = wx.Menu()
		options_menu = wx.Menu()
		mode_menu = wx.Menu()
		
		#file_menu element-definition{
		file_s_a= file_menu.Append(wx.NewId(),"Save as Text")
		file_s_b= file_menu.Append(wx.NewId(),"Save as Morse")
		file_menu.AppendSeparator()#--
		file_l_a= file_menu.Append(wx.NewId(),"Load from Text")
		file_l_b= file_menu.Append(wx.NewId(),"Load from Morse")
		file_menu.AppendSeparator()#--
		file_exit= file_menu.Append(wx.NewId(),"Exit")
		##}
		
		#options_menu element-definition{
		submenu_sound = wx.Menu() 
		submenu_input = wx.Menu() 
		submenu_punc_main = wx.Menu()
		submenu_punc1 = wx.Menu()
		submenu_punc2 = wx.Menu()
		##
		submenu_sound.Append(wx.NewId(), 'On', kind=wx.ITEM_RADIO)
		submenu_sound.Append(wx.NewId(), 'Off', kind=wx.ITEM_RADIO)
		#
		submenu_input.Append(wx.NewId(), 'Keyboard', kind=wx.ITEM_RADIO)
		submenu_input.Append(wx.NewId(), 'Buttons', kind=wx.ITEM_RADIO)
		#
		submenu_punc1.Append(wx.NewId(),'Standard Punctuation',kind=wx.ITEM_RADIO)
		submenu_punc1.Append(wx.NewId(),'Morse Punctuation',kind=wx.ITEM_RADIO )
		
		submenu_punc2.Append(wx.NewId(),'Standard Spaces',kind=wx.ITEM_RADIO )
		submenu_punc2.Append(wx.NewId(),'Spaces as  / ',kind=wx.ITEM_RADIO) 
		
		submenu_punc_main.AppendMenu(wx.NewId(), 'Special Characters', submenu_punc1)
		submenu_punc_main.AppendSeparator()
		submenu_punc_main.AppendMenu(wx.NewId(), 'Spaces', submenu_punc2)
		##
		options_menu.AppendMenu(wx.NewId(), "Use Sound", submenu_sound)
		options_menu.AppendMenu(wx.NewId(), "Morse Input", submenu_input)
		options_menu.AppendMenu(wx.NewId(),"Punctuation", submenu_punc_main)
		##}
		
		#mode_menu element-definition{
		return_home = mode_menu.Append(wx.NewId(), 'Home')
		go_txt = mode_menu.Append(wx.NewId(), "Text - Morse")
		go_mrse = mode_menu.Append(wx.NewId(), "Morse - Text")
		##}
		menubar.Append(file_menu, 'File')
		menubar.Append(options_menu,'Options')
		menubar.Append(mode_menu,'Mode')
		self.SetMenuBar(menubar)
		
		##-->menubinding{
		self.Bind(wx.EVT_MENU, self.quit, file_exit)
		self.Bind(wx.EVT_MENU, self.returntomain, return_home)
		self.Bind(wx.EVT_MENU, self.showtxt2mrse, go_txt)
		self.Bind(wx.EVT_MENU, self.showmrse2txt, go_mrse)
		##<--menubinding}
###################menubar#######################}

###################buttons-main####################{
		logoImageFile = 'yourethedevlogo.jpg'
		logoImage_make = wx.Image(logoImageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		logoImage = wx.BitmapButton(mainpanel, id=-1, bitmap=logoImage_make, pos=(125, 40), size = (logoImage_make.GetWidth(), logoImage_make.GetHeight()), style = wx.NO_BORDER)
		self.Bind(wx.EVT_BUTTON, self.returntomain, logoImage)

		txtmrseButton = wx.Button(mainpanel, label="Text -> Morse", pos=(25, 330), size=(200,125))
		self.Bind(wx.EVT_BUTTON, self.showtxt2mrse, txtmrseButton)
		
		mrsetxtButton = wx.Button(mainpanel, label="Morse -> Text", pos =(275,330), size=(200,125))
		self.Bind(wx.EVT_BUTTON, self.showmrse2txt, mrsetxtButton)
###################buttons-main####################}

###################buttons - text####################{
		logoImageFile = '25x25-2.png'
		logoImage_make = wx.Image(logoImageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		logoImage = wx.BitmapButton(txtpanel, id=-1, bitmap=logoImage_make, pos=(472, 450), size = (logoImage_make.GetWidth()+5, logoImage_make.GetHeight()+5), style = wx.NO_BORDER)
		self.Bind(wx.EVT_BUTTON, self.returntomain, logoImage)	
###################buttons - text####################}

###################buttons-mrse####################{
		logoImageFile = '25x25-2.png'
		logoImage_make = wx.Image(logoImageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		logoImage = wx.BitmapButton(mrsepanel, id=-1, bitmap=logoImage_make, pos=(472, 450), size = (logoImage_make.GetWidth()+5, logoImage_make.GetHeight()+5), style = wx.NO_BORDER)
		self.Bind(wx.EVT_BUTTON, self.returntomain, logoImage)
###################buttons-mrse####################}

	def quit(self, event):
		self.Destroy()
	
	def onSize(self, event):
		event.Skip()
		mainpanel.SetSize(self.GetClientSizeTuple())
		txtpanel.SetSize(self.GetClientSizeTuple())
		mrsepanel.SetSize(self.GetClientSizeTuple())
	
	def returntomain(self, event):
		mainpanel.SetPosition((0,0))
		txtpanel.Hide()
		mrsepanel.Hide()
		mainpanel.Show()
	
	def showtxt2mrse(self, event):
		txtpanel.SetPosition((0,0))
		mainpanel.Hide()
		mrsepanel.Hide()
		txtpanel.Show()
			
	def showmrse2txt(self, event):
		mrsepanel.SetPosition((0,0))
		mainpanel.Hide()
		txtpanel.Hide()
		mrsepanel.Show()		
		
#running the wx.Frame
if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = helloworld(parent=None, id=-1)
	frame.Show()
	app.MainLoop()