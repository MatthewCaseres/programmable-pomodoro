import asyncio
from programmable_pomodoro import Pomodoro
from datetime import timedelta

task = "Programming in Python"
workInterval = timedelta(minutes=32)
breakInterval = timedelta(minutes=8)
goal = timedelta(hours=2)

pom = Pomodoro(task, workInterval, breakInterval, goal)

logs = asyncio.run(pom.work())

# You can do whatever you want with the logs
print(logs)