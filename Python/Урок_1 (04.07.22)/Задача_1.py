name = str(input("Имя "))
date_birthday = int(input("Введите год рождения: "))
day = int(input("Введите текущий год: "))
print("Вы ввели: ",
      "\n Имя: ", name,
      "\n Год рождения: ", date_birthday,
      "\n Ваш возраст: ", day - date_birthday)