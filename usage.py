import gspread
import asyncio
from programmable_pomodoro import Pomodoro
from datetime import timedelta

class Tasks:
    ROSALIND = ('work', 'rosalind')
    SCHOOL = ('work', 'school')
    OPEN_SOURCE = ('work', 'open source')
    LIFTING = ('exercise', 'lifting')
    CARDIO = ('exercise', 'cardio')
    NO_INTERNET = ('maintenance', 'no internet')

category, task = Tasks.OPEN_SOURCE
workInterval = timedelta(minutes=30)
breakInterval = timedelta(minutes=6)
goal = timedelta(hours=1)

pom = Pomodoro(task, workInterval, breakInterval, goal)

# format and add category metadata
logs = asyncio.run(pom.work())
logs = [
    (
        category if task != 'break' else 'break', 
        task,
        start.strftime("%m/%d/%Y %H:%M:%S"),
        finish.strftime("%m/%d/%Y %H:%M:%S"),
        (finish - start).total_seconds()/3600
    )
    for task, start, finish in logs]

gc = gspread.service_account()
sh = gc.open("Personal Analytics")
print(sh.sheet1.insert_rows(logs, 2))
