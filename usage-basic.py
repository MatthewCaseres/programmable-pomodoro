import asyncio
from programmable_pomodoro import Pomodoro
from datetime import timedelta

pom = Pomodoro(
    task="Python Programming", 
    workInterval=timedelta(minutes=32), 
    breakInterval=timedelta(minutes=8), 
    goal=timedelta(hours=2))

logs = asyncio.run(pom.work())

print(logs)