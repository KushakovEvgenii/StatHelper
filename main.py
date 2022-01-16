import wx
from GUI.Start import StartWindow

if __name__ == '__main__':
	app = wx.App()
	start_frame = StartWindow(None, title = "StatHelper", size = wx.Size(300,300))
	start_frame.Show()
	app.MainLoop()