def sort_v(n):
    for i in range(len(n)-1):
        min_z=n[i]# изначально наименьший эл. в проходе берем за первый эл.
        index_min_z=i
        for j in range(i+1,len(n)):
            if n[j]<min_z:#поиск меньшего эл. 
                min_z=n[j]
                index_min_z=j
        n[i],n[index_min_z]=n[index_min_z],n[i]#поменять миньший эл. в проходе с первым(тоже в проходе)
    return n


if __name__=="__main__":# тесты 
    n=[9, 3, 3, 6, 8, 5, 4, 6, 3, 7]
    print(sort_v(n))

# сложность O(n^2) так как есть вложенный цикл.       