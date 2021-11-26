_math = dict()
_inf = dict()
_phys = dict()
str = input()
while(str!=''):
    _str = str.split()
    _math[_str[0]] = int(_str[1])
    str = input()

print(_math)

while(str!=''):
    _str = str.split()
    _inf[_str[0]] = int(_str[1])
    str = input()

print(_inf)

while(str!=''):
    _str = str.split()
    _phys[_str[0]] = int(_str[1])
    str = input()

print(_phys)