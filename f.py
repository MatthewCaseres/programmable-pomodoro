from programmable_pomodoro import Pomodoro
from datetime import timedelta
import asyncio

pom = Pomodoro("test", goal=timedelta(minutes=25))
lol = asyncio.run(pom.work())
print(lol)