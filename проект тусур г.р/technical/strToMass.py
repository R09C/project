def strTOMass(str):# функция преобразовывающая исходные данные
    # пользователя в массив для дальнейшей работы с ним
    mass=[]
    str_list=str.split(sep=',')#разделение чисел по запятой
    for item in str_list:
        mass.append(int(item))
    return mass








if __name__=="__main__":# тесты 
    n='1,3,4,4,4,1'
    print(strTOMass(n))