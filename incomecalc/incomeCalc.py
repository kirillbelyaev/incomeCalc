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
import wx.lib.agw.aquabutton as AB

class IncomeCalc(wx.Frame):

    calcVersion = '0.5'
    num = "";

    def __init__(self, parent, title):
        # ensure the parent's __init__ is called
        super(IncomeCalc, self).__init__(parent, size=(175, 320))

        # create a panel in the frame
        panel = wx.Panel(self)

        #panel.SetBackgroundColour('white')
        panel.SetBackgroundColour('TURQUOISE')

        # # put some text with a larger bold font on it
        topLabelTxt = wx.StaticText(panel, label="Income Calc")
        topLabelTxt.SetOwnForegroundColour('brown')
        font = topLabelTxt.GetFont()
        font.PointSize += 8
        font = font.Bold()
        topLabelTxt.SetFont(font)

        # and create a sizer to manage the layout of child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(topLabelTxt, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 5))
        panel.SetSizer(sizer)

        box = wx.BoxSizer(wx.VERTICAL)
        labelTxt = wx.StaticText(panel, -1, "Day Sum:")
        labelTxt.SetOwnForegroundColour('blue')
        font = labelTxt.GetFont()
        font = font.Bold()
        labelTxt.SetFont(font)

        box.Add(labelTxt, 1, wx.ALIGN_LEFT, 5)
        self.txtBox = wx.TextCtrl(panel)

        box.Add(self.txtBox, 1, wx.ALIGN_LEFT, 5)
        self.txtBox.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        sizer.Add(box)

        #button = wx.Button(panel, wx.ID_ANY, "Add Daily Sum \t", (100,100) )
        button = AB.AquaButton(panel, wx.ID_ANY, None, "Add Day Sum \t\t" )
        button.SetForegroundColour("blue")
        button.SetBestSize()
        #button.SetPulseOnFocus(True)
        #sizer.Add(button, 0, wx.ALIGN_LEFT)
        sizer.Add(button)
        button.Bind(wx.EVT_BUTTON, self.onButtonAddDailySum)

        #buttonDS = wx.Button(panel, wx.ID_ANY, "Show Daily Sum ", (100, 100))
        buttonDS = AB.AquaButton(panel, wx.ID_ANY, None, "Show Day Sum \t")
        buttonDS.SetForegroundColour("blue")
        buttonDS.SetBestSize()
        # sizer.Add(button, 0, wx.ALIGN_LEFT)
        sizer.Add(buttonDS)
        buttonDS.Bind(wx.EVT_BUTTON, self.onButtonShowDailySum)

        #buttonMT = wx.Button(panel, wx.ID_ANY, "Show \n Monthly Total \t", (100, 100))
        buttonMT = AB.AquaButton(panel, wx.ID_ANY, None, "Show Month Ttl\t")
        buttonMT.SetForegroundColour("blue")
        buttonMT.SetBestSize()
        # sizer.Add(button, 0, wx.ALIGN_LEFT)
        sizer.Add(buttonMT)
        buttonMT.Bind(wx.EVT_BUTTON, self.onButtonShowMonthlyTotal)

        #buttonMA = wx.Button(panel, wx.ID_ANY, "Show \n Monthly Avg   \t", (100, 100))
        buttonMA = AB.AquaButton(panel, wx.ID_ANY, None, "Show Month Avg")
        buttonMA.SetForegroundColour("blue")
        buttonMA.SetBestSize()
        # sizer.Add(button, 0, wx.ALIGN_LEFT)
        sizer.Add(buttonMA)
        buttonMA.Bind(wx.EVT_BUTTON, self.onButtonShowMonthlyAvg)

        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to Income Calc")

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
        funcItemCurrRecords = fileMenu.Append(
            -1,
            "Show Current Monthly Records"
        )

        fileMenu.AppendSeparator()

        funcItemMarch = fileMenu.Append(
            -1,
            "Show March Stat Report"
        )

        fileMenu.AppendSeparator()

        funcItemApril = fileMenu.Append(
            -1,
            "Show April Stat Report"
        )

        fileMenu.AppendSeparator()

        funcItemMay = fileMenu.Append(
            -1,
            "Show May Stat Report"
        )

        fileMenu.AppendSeparator()

        funcItemJune = fileMenu.Append(
            -1,
            "Show June Stat Report"
        )

        fileMenu.AppendSeparator()

        funcItemJuly = fileMenu.Append(
            -1,
            "Show July Stat Report"
        )

        fileMenu.AppendSeparator()

        funcItemAugust = fileMenu.Append(
            -1,
            "Show August Stat Report"
        )

        fileMenu.AppendSeparator()

        funcItemSeptember = fileMenu.Append(
            -1,
            "Show September Stat Report"
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
        menuBar.Append(fileMenu, "&Reports")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.showMonthlyReport, funcItemCurrRecords)
        self.Bind(wx.EVT_MENU, self.showStatReportMarch, funcItemMarch)
        self.Bind(wx.EVT_MENU, self.showStatReportApril, funcItemApril)
        self.Bind(wx.EVT_MENU, self.showStatReportMay, funcItemMay)
        self.Bind(wx.EVT_MENU, self.showStatReportJune, funcItemJune)
        self.Bind(wx.EVT_MENU, self.showStatReportJuly, funcItemJuly)
        self.Bind(wx.EVT_MENU, self.showStatReportAugust, funcItemAugust)
        self.Bind(wx.EVT_MENU, self.showStatReportSeptember, funcItemSeptember)
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

    def showStatReportMarch(self, event):
        r = showMarchSumIncomeTbl()
        r1 = showMarchAvgIncomeTbl()

        if r is not None and r1 is not None:
            wx.MessageBox("March Total/Avg: " + str(r[0]) + " / " + str(r1[0]))
        else:
            wx.MessageBox("No data available")

    def showStatReportApril(self, event):
        r = showAprilSumIncomeTbl()
        r1 = showAprilAvgIncomeTbl()

        if r is not None and r1 is not None:
            wx.MessageBox("April Total/Avg: " + str(r[0]) + " / " + str(r1[0]))
        else:
            wx.MessageBox("No data available")

    def showStatReportMay(self, event):
        r = showMaySumIncomeTbl()
        r1 = showMayAvgIncomeTbl()

        if r is not None and r1 is not None:
            wx.MessageBox("May Total/Avg: " + str(r[0]) + " / " + str(r1[0]))
        else:
            wx.MessageBox("No data available")

    def showStatReportJune(self, event):
        r = showJuneSumIncomeTbl()
        r1 = showJuneAvgIncomeTbl()

        if r is not None and r1 is not None:
            wx.MessageBox("June Total/Avg: " + str(r[0]) + " / " + str(r1[0]))
        else:
            wx.MessageBox("No data available")

    def showStatReportJuly(self, event):
        r = showJulySumIncomeTbl()
        r1 = showJulyAvgIncomeTbl()

        if r is not None and r1 is not None:
            wx.MessageBox("July Total/Avg: " + str(r[0]) + " / " + str(r1[0]))
        else:
            wx.MessageBox("No data available")

    def showStatReportAugust(self, event):
        r = showAugustSumIncomeTbl()
        r1 = showAugustAvgIncomeTbl()

        if r is not None and r1 is not None:
            wx.MessageBox("August Total/Avg: " + str(r[0]) + " / " + str(r1[0]))
        else:
            wx.MessageBox("No data available")

    def showStatReportSeptember(self, event):
        r = showSeptemberSumIncomeTbl()
        r1 = showSeptemberAvgIncomeTbl()

        if r is not None and r1 is not None:
            wx.MessageBox("September Total/Avg: " + str(r[0]) + " / " + str(r1[0]))
        else:
            wx.MessageBox("No data available")


    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox(
            "Income Calculator \n"
            "Version " + self.calcVersion,
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
