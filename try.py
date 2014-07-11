import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None)

        panel = wx.Panel(self)

        # create controls
        global cntrlPanel
        cntrlPanel = wx.Panel(panel)
        btn = wx.Button(cntrlPanel, label="Next to 1")
        btn.Bind(wx.EVT_BUTTON, self._onShowHelp)

        #sizer = wx.BoxSizer(wx.VERTICAL)
        #sizer.Add(stc1)
        #sizer.Add(stc2)
        #sizer.Add(btn)
        #cntrlPanel.SetSizer(sizer)


        # create help panel
        global helpPanel
        helpPanel = wx.Panel(panel)
        btn = wx.Button(helpPanel, label="Back to 0")
        btn.Bind(wx.EVT_BUTTON, self._onShowCntrls)
        #sizer = wx.BoxSizer(wx.VERTICAL)
        #sizer.Add(stcHelp)
        #sizer.Add(btn)
        #helpPanel.SetSizer(sizer)
        helpPanel.Hide()
        helpPanel.Raise()
        helpPanel.SetBackgroundColour((240,250,240))
        self.Bind(wx.EVT_SIZE, self._onSize)

        self._onShowCntrls(None)

    def _onShowHelp(self, event):
        helpPanel.SetPosition((0,0))
        helpPanel.Show()
        cntrlPanel.Hide()

    def _onShowCntrls(self, event):
        cntrlPanel.SetPosition((0,0))
        helpPanel.Hide()
        cntrlPanel.Show()

    def _onSize(self, event):
        event.Skip()
        helpPanel.SetSize(self.GetClientSizeTuple())
        cntrlPanel.SetSize(self.GetClientSizeTuple())

app = wx.PySimpleApp()
frame = MyFrame()
frame.Show()
app.SetTopWindow(frame)
app.MainLoop()