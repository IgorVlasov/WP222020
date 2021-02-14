HELP = """
help - список команд
add - добавить событие
showall - показать все события
remove - удалить событие
exit - закрыть программу
"""
exit = False
todo = {}
while exit == False:
  print("Введите команду")
  print("Для вывода списка команд введите help")
  userUnswer = input()

  if userUnswer == "exit":
    exit = True
    continue
  elif userUnswer == "add":
    print("событие добавленно")
  elif  userUnswer == "remove":
    print("событие удаленно")
  elif  userUnswer == "showall":
    print("событие удаленно")
  elif  userUnswer == "help":
    print(HELP)
  else:
    print("не знаю такой команды")
    print("для вывода списка команд введите help")


