# Created on 01 November 2018
# @author vinimmelo
# Code Wars challenges
# Site => https://www.codewars.com

def remove_duplicity(text):
    #return number of duplicity text
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


def filter_list(l):
    # return a new list with the strings filtered out
    return [x for x in l if type(x) is not str]


def descending_order(num):
    #return numbers in descending order
    new_list = sorted([int(x) for x in list(str(num))], reverse=True)
    return ''.join(map(str, new_list))


def digital_root(n):
    #recursive sum of all the digits in a single number.
    if n >= 10:
        x = n //10
        y = digital_root(x) + n % 10
        if(y >= 10):
            return digital_root(y)
        else:
            return y
    else:
        return n


def validate_pin(pin):
    #Accept pins with 4 or 6 digits (only numbers)
    try:
        return (len(pin) == 4 or len(pin) == 6) and int(pin) >= 0 and pin.isdigit()
    except:
        return False


def bool_to_word(bool):
    return "Yes" if bool else "No"


def number(bus_stops):
    sum = 0
    subtrain = 0
    for x in bus_stops:
        sum += x[0]
        subtrain +=x[1]
    return sum - subtrain

def series_sum(n):
    series = [1.0 / (1.0 + (x * 3)) for x in range(100)]
    soma = 0
    for x in range(n):
        soma += series[x]
    return str("%.2f" % (soma))


def alphabet_position(text):
    new_text = [x.lower() for x in text if x.isalpha()]
    word = [str(ord(y) - 96) + ' ' for y in new_text if ord(y) >= 97 and ord(y) <= 122]
    return ''.join(word).strip()


def pig_it(text):
    return ' '.join([i[1:] + i[0] + 'ay' if i.isalpha() else i for i in text.split(' ')])


def sort_by_length(arr):
    return sorted(arr, key=len)


def find_next_square(sq):
    list_squares = [x*x for x in range(2000)]
    return list_squares[list_squares.index(sq) + 1] if sq in list_squares else -1


def first_non_repeating_letter(string):
    for x in string:
        if string.lower().count(x) == 1 or string.upper().count(x) == 1: return x
    return ''


def diamond(n):
    if n <= 0 or n % 2 == 0:
        return None
    middle = (n // 2) + 1
    result = ""
    if n == 1: return "*"
    for i in range(middle):
        result += ("*" * ((i * 2) + 1)).rjust(middle+i)
        result += "\n"
    for i in range(middle-2, -1, -1):
        result += ("*" * ((i * 2) + 1)).rjust(middle+i)
        result += "\n"
    return result


def move_zeros(lista: list):
    zero_indexes = [x for x in lista if x != 0 or x is False]
    for x in range((len(lista)-len(zero_indexes))):
        zero_indexes.append(0)
    return zero_indexes


class Dictionary:
    def __init__(self,words):
        self.words=words
    def find_most_similar(self,term):
        most_similar = 0
        similar_term = self.words[0]
        for x in self.words:
            similarity = 0
            for letter in term:
                if letter in x:
                    similarity += 1
            if abs(len(term) - len(x)) == 2: similarity += 1
            if abs(len(term) - len(x)) == 1: similarity += 2
            if abs(len(term) - len(x)) == 0: similarity += 2
            try:
                for index in range(len(term) -1):
                    if term[index] == x[index]: similarity += 1
            except:
                None
            if similarity > most_similar:
                similar_term = x
                most_similar = similarity
        return similar_term


if __name__ == '__main__':
    print(move_zeros([False,1,0,1,2,0,1,3,"a"]))
