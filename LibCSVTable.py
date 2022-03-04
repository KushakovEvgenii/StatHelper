'''This module is used for creating  table from CSV-file'''

import wx,wx.grid
from LibCSV import CSV
from LibStatistics import Statistics

class CSVImport:
    def __init__(self,path):
        self.csv_module = CSV()
        self.file = self.csv_module.read(path)
    def showfile(self):
        return self.file

class CSVTable(wx.Frame):
    def __init__(self,file):
        self.frame = wx.Frame(None, wx.ID_ANY, 'Table from CSV file', wx.DefaultPosition, wx.Size(640,360))
        self.panel = wx.Panel(self.frame)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.grid = wx.grid.Grid(self.panel,wx.ID_ANY,wx.DefaultPosition,wx.Size(1,1))
        self.grid.CreateGrid(len(file),len(file[0]))
        for i in range(len(file[0])):
            self.grid.SetColLabelValue(i,file[0][i])
        for i in range(len(file)-1):
        	for j in range(len(file[0])):
        		cell_value = file[i+1][j]
        		cell_value = cell_value.strip()
        		self.grid.SetCellValue(i,j,cell_value)
        		self.grid.SetReadOnly(i,j)
        self.grid.AutoSizeColumns()
        self.sizer.Add(self.grid,1,wx.EXPAND+wx.ALL,5)
        self.panel.SetSizer(self.sizer)
        self.frame.Show()