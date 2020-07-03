myList = [11,
          'Строка',
          3.1415926535,
          ['с', 'п', 'и', 'с', 'о', 'к'],
          {'и', 'о', 'с', 'п', 'к'},
          {'name':'Roman',
           'age':38},
          False,
          None,
          bin(17),
          oct(17),
          hex(17)]
for i, el in enumerate(myList):
    print(f'Тип данных {i} элемента {el} : {type(el)}')



