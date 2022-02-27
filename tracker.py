"""
MD FILE:

# START PROJECT - Project Name - Status:In Progress

## START TASK - Task Name - Status:In Progress

### START TIME - 18/03/2022 - 18:50:30
### END TIME - 18/03/2022 - 18:50:30 - Some kind of comment

## END TASK - Task Name

## START TASK - Task Name - Status:Done

### START TIME - 18/03/2022 - 18:50:30
### END TIME - 18/03/2022 - 18:50:30 - NONE (When you don't want to comment anything)

## END TASK - Task Name

# END PROJECT - Project Name
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

projects = []

tracker_file_exists = os.path.exists("./tracker.md")
if tracker_file_exists:
  tracker_file = open('./tracker.md', 'r')
  tracker_file_lines = tracker_file.readlines()

  times = []
  tasks = []

  for line in tracker_file_lines:
    if "START PROJECT" in line:
      project_name = 'read project name'
      project_status = 'read project status'
      tasks = []
    
    if "END PROJECT" in line:
      projects.append(Project(project_name, project_status, tasks))


    if "START TASK" in line:
      task_name = 'read task name'
      task_status = 'read task status'
      times = []

    if "END TASK" in line:
      tasks.append(Task(task_name, task_status, times))


    if "START TIME" in line:
      time_start = 'read_time_start'

    if 'END TIME' in line:
      time_end = 'read_time_end'
      comment = 'read_comment_or_NONE'
      times.append(Time(time_start, time_end, comment))
