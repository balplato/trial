def parse_number(num):
    dict = {}
    dict['odd'] = 0
    dict['even'] = 0
    odd = ['1','3','5','7','9']
    even = ['0','2','4','6','8']
    for i in f'{num}':
        if i in odd:
            dict['odd'] += 1
        elif i in even:
            dict['even'] +=1
        else:
            dict = False
    print(dict)
num = input('number = ')
parse_number(num)
