HELP = """
help    - список команд
add     - добавить событие
showall - показать все события
remove  - удалить событие
exit    - закрыть программу
"""

exit = False
userUnswer = 0



todo = {}
print("Введите команду")
print("Для вывода списка команд введите help")





while exit == False:
  
  userUnswer = input()

  if userUnswer == "exit":
    exit = True
    continue
  elif userUnswer == "add":
    print("событие добавлено")
  elif userUnswer == "remove":
    print("событие удалено")
  elif userUnswer == "showall":
    print("событие удалено")
  elif userUnswer == "help":
    print(HELP)
    
  else:
    print("Не знаю такой команды")
    print("Для вывода списка команд введите help")