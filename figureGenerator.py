# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 15:58:46 2021

@author: qizhe
"""

import os, os.path, time
import calendar
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rcParams
import qizhenkangpylib
# 字体设置
rcParams['font.family'] = 'Times New Roman'

if __name__ == '__main__':
    # myfunc = myFunction()
    # Statistics
    # hourslist, yearsDict = myfunc.statistics('./code/')
    hourslist = [4, 0, 0, 0, 0, 0, 0, 0, 0, 3, 22, 10, 5, 8, 10, 11, 7, 16, 1, 13, 16, 4, 2, 4]
    yearsDict = {2020: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18], 2021: [0, 0, 0, 0, 0, 0, 0, 12, 68, 38, 0, 0]}
    
    totalProblems = sum(hourslist)
    
    plt.style.use('dark_background')
    githubColor = [13/255,17/255,23/255] # 匹配github色彩
    fig_hours, ax = plt.subplots(figsize=(8, 4),facecolor=githubColor) # ,facecolor='black'
    hours = [str(i) for i in range(24)]
    hourslist_percent = [ i / totalProblems * 100  for i in hourslist]
    hourscmap = plt.cm.get_cmap('tab20c')
    hoursColor = hourscmap([ i/24 * 4 / 5 for i in range(24)])
    ax.bar(hours, hourslist_percent, width=0.5, label="Working Hours", color = hoursColor)
    ax.set_facecolor(githubColor)
    for label in ax.xaxis.get_ticklabels()[1::2]:
        label.set_visible(False)
    
    
    # 设置字号
    fontSize = 10
    myDPI = 150
    plt.xticks(size=fontSize)
    plt.yticks(size=fontSize)
    plt.xlabel('Time / hour',fontsize=fontSize+3)
    plt.ylabel('The percentage of problems / %',fontsize=fontSize+3)
    plt.title("Hourly Distribution of Zhenkang's Study Time", fontsize=fontSize+5) # 设置标题
    plt.savefig('.//figure//HourlyDistribution.jpg', dpi=myDPI,facecolor=githubColor)
    
    # plt.xticks(fontsize = 30)
    
    fig_months, ax = plt.subplots(figsize=(8, 4),facecolor=githubColor)
    months = [calendar.month_abbr[i] for i in range(1,13)]
    monthscmap = plt.cm.get_cmap('tab20c')
    totalProblems2021 = sum(yearsDict[2021])
    monthslist_percent = [i / totalProblems2021 * 100 for i in yearsDict[2021]]
    monthsColor = hourscmap([ i/12 * 4 / 5 for i in range(12)])
    ax.bar(months, monthslist_percent, width=0.5, label="Product_1", color=monthsColor)
    ax.set_facecolor(githubColor)
    fig_months.set_facecolor(githubColor)
    # plt.plot(hourslist)
    print(hourslist)
    print(yearsDict)
    
    # 设置字号
    # fontSize = 15
    plt.xticks(size=fontSize)
    plt.yticks(size=fontSize)
    plt.xlabel('Time / month',fontsize=fontSize+3)
    plt.ylabel('The percentage of problems / %',fontsize=fontSize+3)
    plt.title("Monthly Distribution of Zhenkang's Study Time", fontsize=fontSize+5) # 设置标题
    plt.savefig('.//figure//MonthlyDistribution.jpg', dpi=myDPI,facecolor=githubColor)
    # plt.xticks(fontsize = 30)
    
    
    # Name2MarkdownList
    # strlist = myfunc.Name2MarkdownList('E:\\Python_Projects\\LeetCode\\')
    # for s in strlist:
    #     print(s)
    
    # Rename
    # myfunc.rename('E:\\Python_Projects\\LeetCode\\')
