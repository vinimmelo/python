# Created on 01.11.2018
# @author vinimmelo
# Code Wars challenges
# Site => https://www.codewars.com

#return number of duplicity text
def remove_duplicity(text):
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


 #return a new list with the strings filtered out
def filter_list(l):
    return print([x for x in l if type(x) is not str])


#return numbers in descending order
def descending_order(num):
    new_list = sorted([int(x) for x in list(str(num))], reverse=True)
    return ''.join(map(str, new_list))


if __name__ == '__main__':
    descending_order(15)
    descending_order(123456789)
