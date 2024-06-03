#!/usr/bin/env python

# * Income Calculator
# *
# * Copyright (C) 2024 Kirill A Belyaev
# *
# * E-mail contact:
# * kirillbelyaev@yahoo.com
# *
# * This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
# * To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/ or send
# * a letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.

import wx

from incomecalc.dbmodule import *

class IncomeCalc(wx.Frame):

    num = "";

    def __init__(self, parent, title):
        # ensure the parent's __init__ is called
        super(IncomeCalc, self).__init__(parent, size=(220, 300))

        # create a panel in the frame
        panel = wx.Panel(self)

        # # put some text with a larger bold font on it
        st = wx.StaticText(panel, label="Income Tracker")
        st.SetOwnForegroundColour('brown')
        font = st.GetFont()
        font.PointSize += 8
        font = font.Bold()
        st.SetFont(font)

        # and create a sizer to manage the layout of child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 5))
        panel.SetSizer(sizer)

        box = wx.BoxSizer(wx.VERTICAL)
        labelTxt = wx.StaticText(panel, -1, "Daily Sum:")

        box.Add(labelTxt, 1, wx.ALIGN_LEFT, 5)
        self.txtBox = wx.TextCtrl(panel)

        box.Add(self.txtBox, 1, wx.ALIGN_LEFT, 5)
        self.txtBox.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        sizer.Add(box)

        button = wx.Button(panel, wx.ID_ANY, "Add Daily Sum \t", (100,100) )
        #sizer.Add(button, 0, wx.ALIGN_LEFT)
        sizer.Add(button)
        button.Bind(wx.EVT_BUTTON, self.onButtonAddDailySum)

        buttonR = wx.Button(panel, wx.ID_ANY, "Show Daily Sum ", (100, 100))
        # sizer.Add(button, 0, wx.ALIGN_LEFT)
        sizer.Add(buttonR)
        buttonR.Bind(wx.EVT_BUTTON, self.onButtonShowDailySum)

        buttonMT = wx.Button(panel, wx.ID_ANY, "Show \n Monthly Total \t", (100, 100))
        # sizer.Add(button, 0, wx.ALIGN_LEFT)
        sizer.Add(buttonMT)
        buttonMT.Bind(wx.EVT_BUTTON, self.onButtonShowMonthlyTotal)

        buttonMA = wx.Button(panel, wx.ID_ANY, "Show \n Monthly Avg   \t", (100, 100))
        # sizer.Add(button, 0, wx.ALIGN_LEFT)
        sizer.Add(buttonMA)
        buttonMA.Bind(wx.EVT_BUTTON, self.onButtonShowMonthlyAvg)

        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to Income Tracker")

        self.Centre()
        self.Show()
        self.Fit()

    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        funcItem = fileMenu.Append(
            -1,
            "Show Monthly Records",
            "Show May Stat Report",
        )

        fileMenu.AppendSeparator()

        funcItem1 = fileMenu.Append(
            -1,
            "Show May Stat Report",
        )

        fileMenu.AppendSeparator()

        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&Report")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.showMonthlyReport, funcItem)
        self.Bind(wx.EVT_MENU, self.showStatReportMay, funcItem1)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)

    def showMonthlyReport(self, event):
        r = showMonthlyIncomeTbl()

        if r is not None:
            wx.MessageBox("Monthly list: \n" + r.__str__().strip('[]').replace("),", ")\n"))
        else:
            wx.MessageBox("No data available")

    def showStatReportMay(self, event):
        r = showMaySumIncomeTbl()
        r1 = showMayAvgIncomeTbl()

        if r is not None and r1 is not None:
            wx.MessageBox("May Total/Avg: " + str(r[0]) + " / " + str(r1[0]))
        else:
            wx.MessageBox("No data available")


    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox(
            "Income Calculator \n"
            "Version 0.1",
            "About Income Calculator",
            wx.OK | wx.ICON_INFORMATION,
        )

    def onButtonAddDailySum(self, event):
        if self.num.isnumeric() == False:
            wx.MessageBox("Num Error!")
        else:
            n = showIncomeTblCurrRecord()

            if n is None:
                createIncomeTblRecord(self.num)
            else:
                updateIncomeTblRecord(self.num)

    def onButtonShowDailySum(self, event):
        n = showIncomeTblCurrRecord()

        if n is not None:
            wx.MessageBox("Daily sum: " + str(n[0]))

    def onButtonShowMonthlyTotalMay(self, event):
        n = showMaySumIncomeTbl()

        if n is not None:
            wx.MessageBox("May total: " + str(n[0]))

    def onButtonShowMonthlyTotal(self, event):
        n = showMonthlySumIncomeTbl()

        if n is not None:
            wx.MessageBox("Monthly total: " + str(n[0]))

    def onButtonShowMonthlyAvg(self, event):
        n = showMonthlyAvgIncomeTbl()

        if n is not None:
            wx.MessageBox("Monthly avg: " + str(n[0]))

    def OnKeyTyped(self, event):
        self.num = event.GetString()
        #print (event.GetString() )
        print (self.num)


if __name__ == "__main__":
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    IncomeCalc(None, title="Income Calculator")
    app.MainLoop()
