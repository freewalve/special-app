#Приветствие
SEPARATOR = '------------------------------------------'
print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')


def launches_unit_entry_personal_information():  # блок ввода личной инфы если выбрано 1.1
    name = "Gtnz" #input('Введите имя: ')
    
    while True:# Цикл для определения перменной age
        age = 25 #int(input('Введите возраст: ')) 
        if age <= 0:
            print('Возраст должен быть положительным или не ноль')
        elif age > 0:
          if 11 <= age % 100 <= 19:# проверка на 100+ лет
            years_parameter = 'лет'
          elif age % 10 == 1:
              years_parameter = 'год'
          elif age % 10 in [2, 3, 4]:
              years_parameter = 'года'
          else:
              years_parameter = 'лет'
          break
          
    years =  years_parameter # необязательно   
  
    phone_numbers = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
    phone_number = ""  
    for digit in phone_numbers:
        if digit == '+' or ('0' <= digit <= '9'):
            phone_number += digit
                   
    email = input('Введите адрес электронной почты: ')
    zip_codes = input('Введите индекс: ')
    zip_code = ""  
    for digit in zip_codes:
        if '0' <= digit <= '9':
            zip_code += digit
    additional_information = input('Введите дополнительную информацию:\n')
    print("Информация принята")
    return name, age, years, phone_number, email, zip_code, additional_information


def launches_unit_entry_busines_information():  # блок ввода бизнес инфы если выбрано 1.2
    while True:# Цикл для определения переменной огрнип
        ogrnip = input("Введите ОГРНИП: ")
        if len(ogrnip) >= 15:  #проверяем длину списка
            ogrnip = int(
                ogrnip)  # Преобразуем введенное значение в целое число
            break
        else:
            print("ОГРНИП должен содержать не менее 15 символов")
          
    inn_number = int(input("Ведите ИНН: "))
  
    while True:  # задаем параметр расчетный счет
        checking_account = input("Ведите расчетный счет: ")
        if not checking_account.isdigit():  # Вместо перебора со сравнением
            print("Расчетный счет должен содержать только цифры")
        elif len(checking_account) >= 20:  # проверяем длину списка
            checking_account = int(checking_account)  # Преобразуем введенное значение в целое число
            break
        else:
            print("Расчетный счет должен содержать не менее 20 символов")
    bank_name = input("Введите название банка: ")            
    bank_identifier_code = input("Введите БИК: ")
    correspondent_account = input("Введите кореспондентский счет: ")
    print("Информация принята")
    return ogrnip, inn_number, checking_account, bank_name, bank_identifier_code, correspondent_account
    

def launch_menu_output_information(save_personal_information_, save_business_information_):  # Меню блока вывода информ.  2
  if  (save_personal_information_ is not None) or (save_business_information_ is not None):   
    print(SEPARATOR)
    print('ВЫВЕСТИ ИНФОРМАЦИЮ\n1 - Общая информация\n2 - Вся информация\n0 - Назад')
    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        return
    elif option == 1:
        #print(save_personal_information_)
        displays_general_information(*save_personal_information_)
    elif option == 2:
        displays_general_information(*save_personal_information_)
        displays_all_information(*save_business_information_)
  else:
    print("Данные отсутствуют, введите даные в меню 1")


def displays_general_information(names, ages, years, phone, e_mail, codez, information):  # блока вывода информ.  2.1
    print(SEPARATOR)  
    print(f'Имя:      {names}\nВозвраст: {ages} {years}\nТелефон: {phone}\nE-mail: {e_mail}\nИндекс: {codez}\nАдрес:{information}')
  

def displays_all_information(ogrn, inn, account, bank, bic, correspondent):  #блока вывода  всей информ.  2.2
    print(SEPARATOR)
    print(f'ОГРНИП:  {ogrn}\nИНН: {inn}\nБанковские реквизиты\nP/c: {account}\nБанк: {bank}\nБИК: {bic}\nК/с:{correspondent}')
  
    
flag_personal = False 
flag_business = False

while True: # Главное меню
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию\n2 - Вывести информацию\n0 - Завершить работу')
    save_personal_information = None
    save_business_information = None
   
    option_main_menu = int(input('Введите номер пункта меню: '))
  
    if option_main_menu == 0:
        break
    elif option_main_menu == 1:# меню блока ввода личной и бизнес информ.  1
      print(f'{SEPARATOR}\nВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
      print('1 - Общая информация\n2 - Информация о предпринимателе\n0 - Назад')

      choice_inpyt_block = int(input('Введите номер пункта меню: '))
      if choice_inpyt_block == 0:
        continue  #
      elif choice_inpyt_block == 1:
        flag_personal = True
        new_save_personal_information = launches_unit_entry_personal_information()
      elif choice_inpyt_block == 2:
        flag_business = True
        new_save_business_information = launches_unit_entry_busines_information()
      else:
        print("Некоректный ввод")
        continue
    elif option_main_menu == 2:
        if  flag_personal == True and flag_business == False :
          launch_menu_output_information(new_save_personal_information, save_business_information)
        elif  flag_business == True :
          launch_menu_output_information(new_save_personal_information, new_save_business_information) 
        elif  flag_personal == True and flag_business == True:
          launch_menu_output_information(new_save_personal_information, new_save_business_information)    
        else:
          launch_menu_output_information(save_personal_information, save_business_information)
    else:
        print("Некоректный ввод")
        continue
