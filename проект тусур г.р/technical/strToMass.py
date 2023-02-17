def strTOMass(str):
    mass=[]
    str_list=str.split(sep=',')
    for item in str_list:
        mass.append(int(item))
    return mass








if __name__=="__main__":
    n='1,3,4,4,4,1'
    print(strTOMass(n))