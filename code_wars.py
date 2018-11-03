<<<<<<< HEAD
#!/usr/bin/env python3
# Created on 01.11.2018
=======
# Created on 01 November 2018
>>>>>>> 89fe19fd1a4f08c9952f7cb15106cfcb67740bbf
# @author vinimmelo
# Code Wars challenges
# Site => https://www.codewars.com

<<<<<<< HEAD


def remove_duplicity(text):
    # return number of duplicity text
=======
def remove_duplicity(text):
    #return number of duplicity text
>>>>>>> 89fe19fd1a4f08c9952f7cb15106cfcb67740bbf
    counter = 0
    text_list = list(text.lower())
    new_list = text_list[:]
    for i in text:
        if (new_list.count(i) > 1):
            new_list.remove(i)
    for x in new_list:
        if(text_list.count(x) > 1):
            counter += 1
    return counter


<<<<<<< HEAD

def filter_list(l):
    # return a new list with the strings filtered out
    return [x for x in l if type(x) is not str]
=======
def filter_list(l):
    #return a new list with the strings filtered out
    return print([x for x in l if type(x) is not str])
>>>>>>> 89fe19fd1a4f08c9952f7cb15106cfcb67740bbf


def descending_order(num):
    #return numbers in descending order
    new_list = sorted([int(x) for x in list(str(num))], reverse=True)
    return ''.join(map(str, new_list))


if __name__ == '__main__':
<<<<<<< HEAD
    descending_order(15)
    print(descending_order(123456789))
=======
    pass
>>>>>>> 89fe19fd1a4f08c9952f7cb15106cfcb67740bbf
