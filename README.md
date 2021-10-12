# Python Programmable Pomodoro

## What is this?

If you want to run a pomodoro timer in your terminal and customize it in Python, this might be what you want.

Features include:

* Instantiate a pomodoro timer as a Python class.
  * Customize the `task`, `workInterval`, `breakInterval`, and `goal`. 
* Run an async method of the timer that displays the timer's progress in the terminal.
  * This method will return the datetimes of start/completion of your work/break intervals.
* A bell will ring when the time is up for a work/break interval.
* Completed work/break blocks are colored green in the terminal.

## Installation

```
pip install programmable-pomodoro
```

## Usage

### Code

Here is the most basic example I can think of, this example is in `usage-basic.py` of this repository. Here we aren't doing anything fancy, just run the timer and print what it returns.

```py
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
```

### Transitions

Press enter to transition work->break or break->work

![PP](https://user-images.githubusercontent.com/43053796/137020717-86f509be-873e-4a35-b062-e360daec63af.gif)

Press `q` and then press enter to make the async function return with the logs, ending the timer.

![PP2](https://user-images.githubusercontent.com/43053796/137021101-3db8892f-fe06-41ca-b5a5-e5eb2722d815.gif)

## Advanced Use

Here is how I personally use the timer, as seen in `usage.py`.

```py
import gspread
import asyncio
from programmable_pomodoro import Pomodoro
from datetime import timedelta

# This is like an enum so I can have consistent naming in my log data. 
# The first element of the tuple is the category, the second is the name of the task.
class Tasks:
    ROSALIND = ('work', 'rosalind')
    SCHOOL = ('work', 'school')
    OPEN_SOURCE = ('work', 'open source')
    LIFTING = ('exercise', 'lifting')
    CARDIO = ('exercise', 'cardio')
    NO_INTERNET = ('maintenance', 'no internet')
    
# Configuration for the timer
category, task = Tasks.OPEN_SOURCE
workInterval = timedelta(minutes=30)
breakInterval = timedelta(minutes=6)
goal = timedelta(hours=1)

# Run the timer
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

# Write the logs to a Google Sheet
gc = gspread.service_account()
sh = gc.open("Personal Analytics")
print(sh.sheet1.insert_rows(logs, 2))
```

I hope this example demonstates why I think **programmable** pomodoro timers are cool.

I built a Streamlit dashboard to review my data. You can use it too, just pass in the URL of your Google Sheet and have the first sheet formatted in the same way as mine is.

https://share.streamlit.io/matthewcaseres/productivity-dashboard/main/begin.py
