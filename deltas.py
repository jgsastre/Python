import win32clipboard
import pandas as pd
import win32com.client

def getTable():
    table = pd.read_clipboard(header = None, sep=r"[\[\]\t,\(\)]")
    max1 = table.ix[:, 1].max() + 1
    max2 = table.ix[:, 2].max() + 1
    max3 = table.ix[:, 3].max() + 1

    table = table.ix[:, 5].reshape((max1, max2, max3))
    
    return table
    
def quantsTransform(deltas):
    result = zeros((max3, max1, max2))
    for timeStep in range(max3):
        for x in range(max1):
            for y in range(max2):
                result[timeStep, x, y] = table[x, y, timeStep]
                
    return result

def getClipBoard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    print(data)
    win32clipboard.CloseClipboard()
    
    return data


def sendToTextBox(firstWait, innerWait):
    time.sleep(firstWait)
    shell = win32com.client.Dispatch("WScript.Shell")    
    rawTest = getClipBoard()
    for item in rawTest.splitlines():
        shell.SendKeys(item) 
        shell.SendKeys("{TAB}")
        time.sleep(innerWait/1000.0)