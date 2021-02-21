import time

HELP = """
help      - список команд
add       - добавить задачу
showall   - показать все задачи
show      - задачи на конкретную дату
remove    - удалить задачу
exit      - закрыть программу
"""

def checkDate(uDate):
  try:
    time.strptime(uDate, '%d.%m.%Y')
    return True
  except ValueError:
    print('Не правильный формат даты')
    return False

def addTask(uDate, uTask):
  if uDate in todo.keys():
    todo[uDate].append(uTask)
  else:
    todo[uDate] = [uTask]
  print( f"На {uDate} добвалена задача {uTask}" )
  

userUnswer = 0

todo = {}
print("Введите команду")
print("Для вывода списка команд введите help")

while True:
  
  userUnswer = input()

  if userUnswer == "exit":
    print("Досвидания!")
    break
  elif userUnswer == "add":
    uDate = input("Введите дату события в формате дд.мм.гггг\n")
    
    if checkDate(uDate) == False:
      continue
    
    uTask = input("Что нужно сделать?\n")
    addTask(uDate, uTask)

  elif userUnswer == "remove":
    print("событие удалено")
  elif userUnswer == "showall":
    for pDate in sorted( todo.keys() ):
      for pTask in todo[pDate]:
        print(f"[{pDate}]\t{pTask}")
    print()
  elif userUnswer == "show":
    uDate = input("Ведите дату\n")
    if checkDate(uDate) == False:
      continue 
    for pTask in todo[uDate]:
        print(f"[{uDate}]\t{pTask}")

  elif userUnswer == "help":
    print(HELP)
  else:
    print("Не знаю такой команды")
    print("Для вывода списка команд введите help")