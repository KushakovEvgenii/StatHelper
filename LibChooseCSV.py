'''This module is used for creating  table from CSV-file'''

import wx
from LibCSVTable import CSVImport,CSVTable

class CSVChoose(wx.Frame):
    def __init__(self, *args, **kw):
        super(CSVChoose, self).__init__(*args, **kw)
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.filepickerctrl = wx.FilePickerCtrl(self.panel, wx.ID_ANY, '')
        self.button = wx.Button(self.panel, wx.ID_ANY, 'Click', wx.DefaultPosition, wx.Size(190,21))
        self.button.Bind(wx.EVT_BUTTON, self.PrintPath)
        self.sizer.Add(self.filepickerctrl,0,wx.CENTER+wx.ALL,5)
        self.sizer.Add(self.button,0,wx.CENTER+wx.ALL,5)
        self.panel.SetSizer(self.sizer)
        self.Show()

    def PrintPath(self,event):
    	csvimport = CSVImport(self.filepickerctrl.GetPath())
    	file = csvimport.showfile()
    	self.Close()
    	CSVTable(file)

