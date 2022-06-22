def digitize(n):
    num = str(n)
    my_list = list(num.strip(" "))
    my_list.reverse()
    print(my_list)
    ans =(int(elem) for elem in my_list)
    answer = list(ans)
    print(answer)
digitize(56789)