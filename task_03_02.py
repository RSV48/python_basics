# ------------------------------ Решение 1 -----------------------------
def str_user_1(**kwargs):
    u_list_1 = []
    for i in kwargs.values():
        u_list_1.append(i)
    return ' '.join(u_list_1)


# ------------------------------ Решение 2 -----------------------------
def str_user_2(**kwargs):
    u_list_2 = [i for i in kwargs.values()]
    return ' '.join(u_list_2)


# ------------------------------ Решение 3 -----------------------------

def str_user_3(name='', surname='', year_birth='', city='', email='', tel=''):
    return ' '.join([name, surname, year_birth, city, email, tel])


dict1 = str_user_1(name='Роман', surname='Васильев', yearBirth='1982', city='Липецк', email='ena@enagent.ru',
                   tel='34343')
dict2 = str_user_2(name='Роман', surname='Васильев', yearBirth='1982', city='Липецк', email='ena@enagent.ru',
                   tel='34343')
dict3 = str_user_3(name='Роман', surname='Васильев', year_birth='1982', city='Липецк', email='ena@enagent.ru')

print (f'Решение 1 : {dict1}')
print (f'Решение 2 : {dict2}')
print (f'Решение 3 : {dict3}')
