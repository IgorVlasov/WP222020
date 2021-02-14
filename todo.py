HELP ="""
help       - Помощ душевно больным
add        - Добавить 
showall    - Показать события
remove     - Удалить событие 
exit       - Закрыть программу
"""
exit = True
userUnswer = 0
todo = {}
while exit == False :
  print("Введите команду")
  print("Для вывода списка команд введите help")
  userUnswer = input()
  if userUnswer == "exit":
    exit = True 
    continue
  elif userUnswer == "add":
    print("durak")
  elif userUnswer == "showall":
    print("durachok")
  elif userUnswer == "remove":
    print("дегенерат,это ещё в разработке")
  elif userUnswer == "help":
    print("HELP!!!")
  else :
    print("Бредишь ,сеть нейронная?")
