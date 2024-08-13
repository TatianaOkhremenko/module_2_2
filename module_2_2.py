number_first = (int(input('Введите число: ')))
number_second = (int(input('Введите число: ')))
number_thrid = (int(input('Введите число: ')))
if number_first ==number_second==number_thrid:
    print(int(3))
elif number_first==number_second or number_first==number_thrid or number_second==number_thrid:
    print(int(2))
elif number_first != number_second and number_second!=number_thrid and number_first!=number_thrid:
    print(int(0))
