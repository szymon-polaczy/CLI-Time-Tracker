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


def showEverything():
  for project in projects:
    print("Project: {} ({})".format(project.name, project.status))

    for task in project.tasks:
      print("\tTask: {} ({})".format(task.name, task.status))

      for time in task.times:
        print("\t\tTime: {} - {} ({})".format(time.start_date, time.end_date, time.comment))



import os
from pickle import TRUE

projects = []

tracker_file_exists = os.path.exists("./tracker.md")
if tracker_file_exists:
  tracker_file = open('./tracker.md', 'r')
  tracker_file_lines = tracker_file.readlines()

  times = []
  tasks = []

  for line in tracker_file_lines:
    if "START PROJECT" in line:
      line_arr = line.split(" - ")
      project_name = line_arr[1].replace('\n', '')
      project_status = line_arr[2].replace('\n', '')
      tasks = []
    
    if "END PROJECT" in line:
      projects.append(Project(project_name, project_status, tasks))


    if "START TASK" in line:
      line_arr = line.split(" - ")
      task_name = line_arr[1].replace('\n', '')
      task_status = line_arr[2].replace('\n', '')
      times = []

    if "END TASK" in line:
      tasks.append(Task(task_name, task_status, times))


    if "START TIME" in line:
      line_arr = line.split(" - ")
      time_start = line_arr[1].replace('\n', '')

    if 'END TIME' in line:
      line_arr = line.split(" - ")
      time_end = line_arr[1].replace('\n', '')
      comment = line_arr[2].replace('\n', '')
      times.append(Time(time_start, time_end, comment))

running_time = Time('now', '', '') #get date - mm/dd/yyyy hh:mm:ss
while TRUE:
  os.system('clear')

  # show running time
  if running_time.end_date != '':
    print("Timer running: {} - NOW".format(running_time.start_date))

  # get input from the user
  user_input = input(">: ")
  print('')

  #options:
  if user_input == "help" or user_input == "man":
    print('show help')# help 
  elif user_input == "add timer":
    print('add timer')# add timer - you have to end the previous one
  elif user_input == "end timer":
    print('end timer')# end timer - you can add a comment to it
  elif user_input == "change task status":
    print('change task status')#select task - you have to end a timer to do this - planned / in progress / done / backlog / paussed
  elif user_input == "change project status":
    print('change project status')#select project - all of the tasks have to be done - you have to end a timer to do this - planned / in progress / done / backlog / paussed
  elif user_input == "show everything":
    showEverything()
  elif user_input == "exit":
    print('exit the app')#all timers have to be stopped - you save to the file

  print()
  input('Press enter to continue: ')