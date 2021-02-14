print("Введите команду")
print("Для вывода списка команд введите help")
HELP = """
help - список команд
add - добавить событие
showall - показать все события
remove -удалить событие 
exit - закрыть программу
"""
exit = False
userAnswer = 0

todo = {}

while exit == False:
  
  userAnswer = input()

  if userAnswer == "exit":
    exit = True
    continue
  elif userAnswer == "add":
    print("ВВедите дату события")
    addKey = input()
    print("Что нужно сделать?")
    addValue = input()

    if addKey in todo.keys():
      tmp = [todo[addKey]]
      tmp.append(addValue)
      todo[addKey] = tmp
    else:
      todo[addKey] = addValue

   


    print("событие добавлено")
  elif userAnswer == "remove":
    print("Событие добавлено")
  elif userAnswer == "showall":
    print("Событие добавлено")
  elif userAnswer == "help":
    print(HELP)
  else:
    print("Нeизвестная команда")
    print("Для вывода списка команд введите help")
