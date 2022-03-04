'''This module is used for starting program'''

import wx
from LibChooseCSV import CSVChoose

if __name__ == '__main__':
    app = wx.App()
    frm = CSVChoose(None, title='Import CSV file', size  = wx.Size(640,360))
    app.MainLoop()