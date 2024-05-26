import xlrd
import pyautogui as pg
import pywhatkit
from datetime import datetime

def get_numbers():
    book = xlrd.open_workbook("database.xls")
    sh = book.sheet_by_index(0) 
    numbers = {}
    for idx in range(1, sh.nrows):
        name = sh.cell_value(idx,0)
        cel = "+52" + str(int(sh.cell_value(idx, 1)))
        numbers[name] = cel
    return numbers


def send_wpp(numbers):
    for name,cel in numbers.items():
        # now = datetime.now()
        pywhatkit.sendwhatmsg_instantly(cel,f"Hola {name}",50,True,10)
        # time.sleep(5)
        width, height = pg.size()
        pg.click(width / 2, height / 2)
        pg.press('enter')
            
nums = get_numbers()
send_wpp(nums)
