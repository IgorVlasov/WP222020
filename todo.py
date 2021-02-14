HELP ="""
help       - Помощ душевно больным
add        - Добавить 
showall    - Показать события
remove     - Удалить событие 
exit       - Закрыть программу
"""
exit = False
userUnswer = 0
todo = {}
print("Введите команду")
print("Для вывода списка команд введите help")
while exit == False :
  userUnswer = input()
  if userUnswer == "exit":
    exit = True 
    continue
  elif userUnswer == "add":
    print("durak")
    addKey = input()
    print("nu nu")
    addValue = input()
    if addKey in todo.keys:
      tmp = list(todo[addKey])
      tmp += addValue
    else:
      
    todo[addKey] = addValue
  elif userUnswer == "showall":
    print(todo)
  elif userUnswer == "remove":
    print("тупой")
  elif userUnswer == "help":
    print("HELP!!!" + HELP)
  else :
    print("Даун?")