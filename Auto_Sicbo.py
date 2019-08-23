import Sicbo_Simulator as ss
import random
import openpyxl
import time

tries = 200000
money = range(500, 50000)  # change here to bet in different money ranges
choices = ['big', 'small']  # Change here for different betting choices
workbook = 'sicbo results.xlsx' # Remember to change for a correct filename if needed

wb = openpyxl.load_workbook(workbook)
ws = wb.active
result = []

# Gaming section
for t in range(tries):                
    result.append(ss.sicbo(random.choice(choices), random.choice(list(money))))
    print(f'Game {t}: {result[-1]} (Playing section)')
    if t > tries - 1:
        break

wins = 0
money_back = 0
ws['F6'].value = 0

# Marking down results
for a, b, c, d, e in result:
    profit = a - b
    money_back += profit
    add = ws.max_row + 1
    if profit >= 0:
        wins += 1
        ws[f'D{add}'].value = 'yes'
    else:
        ws[f'D{add}'].value = 'no'
    ws[f'A{add}'].value, ws[f'B{add}'].value, ws[f'C{add}'].value = [b, a, profit]
    ws['F6'].value += b
    print('Game', add - 1, ':', ws[f'A{add}'].value, ws[f'B{add}'].value, ws[f'C{add}'].value, '(Marking section)')

ws['E6'].value = len(result)
ws['G6'].value = money_back
ws['H6'].value = wins / len(result)
print(f"Winning rate: {100 * wins / len(result)}%")
if money_back >= 0:
    print(f"Money gain (per play): ${money_back / len(result)}")
else:
    print(f"Money lost (per play): ${-money_back / len(result)}")
wb.save(workbook)
