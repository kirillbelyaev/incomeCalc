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

import datetime
import sqlite3

db_name = "calc.db"
conn = sqlite3.connect(db_name)
cur = conn.cursor()

def createDb():
    #conn = sqlite3.connect(db_name)
    #cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS income(
       id INT,
       date TEXT,
       sum INT);
    """)
    conn.commit()

def showIncomeTbl():
    cur.execute("SELECT * FROM income;")
    one_result = cur.fetchall()
    print("tbl: ", one_result)

def showMonthlyIncomeTbl():
    today = datetime.date.today()
    current_year = today.year
    current_month = today.strftime("%m")

    cur.execute("SELECT date, sum FROM income WHERE date like '" + current_year.__str__() + "-" + current_month.__str__() + "-%';")
    res = cur.fetchall()

    return res

def showMaySumIncomeTbl():
    today = datetime.date.today()
    current_year = today.year
    cur.execute("SELECT SUM(sum) AS sum FROM income WHERE date like '" + current_year.__str__() + "-05-%';")
    res = cur.fetchone()

    return res

def showMayAvgIncomeTbl():
    today = datetime.date.today()
    current_year = today.year
    cur.execute("SELECT AVG(sum) AS avg FROM income WHERE date like '" + current_year.__str__() + "-05-%';")
    res = cur.fetchone()

    return res

def showMarchSumIncomeTbl():
    today = datetime.date.today()
    current_year = today.year
    cur.execute("SELECT SUM(sum) AS sum FROM income WHERE date like '" + current_year.__str__() + "-03-%';")
    res = cur.fetchone()

    return res

def showMarchAvgIncomeTbl():
    today = datetime.date.today()
    current_year = today.year
    cur.execute("SELECT AVG(sum) AS avg FROM income WHERE date like '" + current_year.__str__() + "-03-%';")
    res = cur.fetchone()

    return res

def showAprilSumIncomeTbl():
    today = datetime.date.today()
    current_year = today.year
    cur.execute("SELECT SUM(sum) AS sum FROM income WHERE date like '" + current_year.__str__() + "-04-%';")
    res = cur.fetchone()

    return res

def showAprilAvgIncomeTbl():
    today = datetime.date.today()
    current_year = today.year
    cur.execute("SELECT AVG(sum) AS avg FROM income WHERE date like '" + current_year.__str__() + "-04-%';")
    res = cur.fetchone()

    return res

def showJuneSumIncomeTbl():
    today = datetime.date.today()
    current_year = today.year
    cur.execute("SELECT SUM(sum) AS sum FROM income WHERE date like '" + current_year.__str__() + "-06-%';")
    res = cur.fetchone()

    return res

def showJuneAvgIncomeTbl():
    today = datetime.date.today()
    current_year = today.year
    cur.execute("SELECT AVG(sum) AS avg FROM income WHERE date like '" + current_year.__str__() + "-06-%';")
    res = cur.fetchone()

    return res

def showJulySumIncomeTbl():
    today = datetime.date.today()
    current_year = today.year
    cur.execute("SELECT SUM(sum) AS sum FROM income WHERE date like '" + current_year.__str__() + "-07-%';")
    res = cur.fetchone()

    return res

def showJulyAvgIncomeTbl():
    today = datetime.date.today()
    current_year = today.year
    cur.execute("SELECT AVG(sum) AS avg FROM income WHERE date like '" + current_year.__str__() + "-07-%';")
    res = cur.fetchone()

    return res

def showAugustSumIncomeTbl():
    today = datetime.date.today()
    current_year = today.year
    cur.execute("SELECT SUM(sum) AS sum FROM income WHERE date like '" + current_year.__str__() + "-08-%';")
    res = cur.fetchone()

    return res

def showAugustAvgIncomeTbl():
    today = datetime.date.today()
    current_year = today.year
    cur.execute("SELECT AVG(sum) AS avg FROM income WHERE date like '" + current_year.__str__() + "-08-%';")
    res = cur.fetchone()

    return res

def showSeptemberSumIncomeTbl():
    today = datetime.date.today()
    current_year = today.year
    cur.execute("SELECT SUM(sum) AS sum FROM income WHERE date like '" + current_year.__str__() + "-09-%';")
    res = cur.fetchone()

    return res

def showSeptemberAvgIncomeTbl():
    today = datetime.date.today()
    current_year = today.year
    cur.execute("SELECT AVG(sum) AS avg FROM income WHERE date like '" + current_year.__str__() + "-09-%';")
    res = cur.fetchone()

    return res


def showMonthlySumIncomeTbl():
    today = datetime.date.today()
    current_year = today.year
    current_month = today.strftime("%m")

    cur.execute("SELECT SUM(sum) AS sum FROM income WHERE date like '" + current_year.__str__() + "-" + current_month.__str__() + "-%';")
    res = cur.fetchone()

    return res

def showMonthlyAvgIncomeTbl():
    today = datetime.date.today()
    current_year = today.year
    current_month = today.strftime("%m")

    cur.execute("SELECT AVG(sum) AS avg FROM income WHERE date like '" + current_year.__str__() + "-" + current_month.__str__() + "-%';")
    res = cur.fetchone()

    return res

def showIncomeTblRecord(dt):
    cur.execute("SELECT sum AS sum FROM income where date = '" + dt + "';")
    one_result = cur.fetchone()
    print("tbl: ", one_result)

def showIncomeTblCurrRecord():
    current_date = datetime.date.today()

    cur.execute("SELECT sum AS sum FROM income where date = '" + current_date.__str__() + "';" )
    res = cur.fetchone()

    return res

def createIncomeTblRecord(sum):
    # get current date
    current_date = datetime.date.today()

    rec = (1, current_date.__str__(), sum)
    cur.execute("INSERT INTO income VALUES(?, ?, ?);", rec)
    conn.commit()
    print("insert committed. ")


def updateIncomeTblRecord(sum):
    # get current date
    current_date = datetime.date.today()
    cur.execute("UPDATE income SET sum = " + sum + " WHERE date = '" + current_date.__str__() + "' ;")
    conn.commit()
    print("update committed. ")


createDb()