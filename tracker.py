"""
MD FILE:

# START - Project Name - Status:In Progress

## START - Task Name - Status:In Progress

### Time Start - 18/03/2022 - 18:50:30
### Time End - 18/03/2022 - 18:50:30 - Some kind of comment

## END - Task Name

## START - Task Name - Status:Done

### Time Start - 18/03/2022 - 18:50:30
### Time End - 18/03/2022 - 18:50:30 - NONE (When you don't want to comment anything)

## END - Task Name

# END - Project Name
"""

class Time:
  start_date = ''
  end_date = ''
  comment = ''

  def __init__(self, read_start_date, read_end_date, read_comment):
    self.start_date = read_start_date
    self.end_date = read_end_date
    self.comment = read_comment

class Task:
  name = ''
  status = ''
  times = [] #array of objects Time

  def __init__(self, read_name, read_status, read_times):
    self.name = read_name
    self.status = read_status
    self.times = read_times

class Project:
  name = ''
  status = ''
  tasks = [] #array of objects Task

  def __init__(self, read_name, read_status, read_tasks):
    self.name = read_name
    self.status = read_status
    self.tasks = read_tasks



import os

tracker_file_exists = os.path.exists("./tracker.md")
if tracker_file_exists:
  print('read file')
