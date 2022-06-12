from functools import reduce

name_lang = 'Java, Python, C#, C++'.split(', ')
len_list = [i for i in range(1, len(name_lang)+1)]


def make_list_tuple(len_list, name_lang):
    name_lang = map(lambda lang: lang.upper(), name_lang)
    return list(zip(len_list, name_lang))


def make_number_from_name(my_tuples):
    result = []
    for number, name in my_tuples:
        # print(number)
        # print(name)
        sum_name =sum([ord(n) for n in name])
        # print(sum_name)
        if sum_name % number == 0:
            result.append((sum_name,name))
    return (result)

def sum_element(list_of_tuples):
    list_of_numbers =[number for number, _ in list_of_tuples]
    print(list_of_numbers)
    sum_all = reduce(lambda x,y: x + y, list_of_numbers)
    return(sum_all)

my_tuples = make_list_tuple(len_list, name_lang)
list_of_tuples = make_number_from_name(my_tuples)
print(sum_element(list_of_tuples))