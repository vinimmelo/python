import code_wars as cw

def test_series_sum():
    assert cw.series_sum(1) == "1.00"
    assert cw.series_sum(2) == "1.25"
    assert cw.series_sum(3) == "1.39"
    assert cw.series_sum(66) == '2.44'
    assert cw.series_sum(69) == '2.45'
    assert cw.series_sum(79) == '2.50'


def test_alphabet_position():
    assert cw.alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
    assert cw.alphabet_position("The narwhal bacons at midnight.") == "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"
    assert cw.alphabet_position("²}}:Po£5aE}Ã¿|¸c$%N¢¿ÍÁ7¾Î5zYµ~ËÇW~m!­knl»¨y=*MÆ£±)tÆy-&KÍ4,iA0MP»¬aÏ¸¦©.Fnl@Á") == "16 15 1 5 3 14 26 25 23 13 11 14 12 25 13 20 25 11 9 1 13 16 1 6 14 12"


def test_pig_it():
    assert cw.pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay'
    assert cw.pig_it('This is my string') =='hisTay siay ymay tringsay'


def test_sort_by_length():
    tests = [
        [["i", "to", "beg", "life"], ["beg", "life", "i", "to"]],
        [["", "pizza", "brains", "moderately"], ["", "moderately", "brains", "pizza"]],
        [["short", "longer", "longest"], ["longer", "longest", "short"]],
        [["a", "of", "dog", "food"], ["dog", "food", "a", "of"]],
        [["", "bees", "eloquent", "dictionary"], ["", "dictionary", "eloquent", "bees"]],
        [["a short sentence", "a longer sentence", "the longest sentence"], ["a longer sentence", "the longest sentence", "a short sentence"]],
    ]
    for exp, inp in tests:
        assert cw.sort_by_length(inp) == exp


def test_first_non_repeating_letter():
    assert cw.first_non_repeating_letter('a') == 'a'
    assert cw.first_non_repeating_letter('stress') == 't'
    assert cw.first_non_repeating_letter('moonmen') == 'e'
    assert cw.first_non_repeating_letter('sTreSS') == 'T'


def test_find_next_square():
    assert cw.find_next_square(121) == 144
    assert cw.find_next_square(625) == 676
    assert cw.find_next_square(122) == -1


def test_diamond():
    expected =  " *\n"
    expected += "***\n"
    expected += " *\n"

    expected2 =  "  *\n"
    expected2 += " ***\n"
    expected2 += "*****\n"
    expected2 += " ***\n"
    expected2 += "  *\n"

    assert cw.diamond(2) == None
    assert cw.diamond(4) == None
    assert cw.diamond(0) == None
    assert cw.diamond(1) == "*"
    assert cw.diamond(3) == expected
    assert cw.diamond(5) == expected2


def test_move_zeros():
    assert cw.move_zeros([False,1,0,1,2,0,1,3,"a"]) == [False,1,1,2,1,3,"a",0,0]
    assert cw.move_zeros([1,2,0,1,0,1,0,3,0,1]) == [ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ]
    assert cw.move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]) == [9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]
    assert cw.move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]) == ["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]
    assert cw.move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]) == ["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0]
    assert cw.move_zeros([0,1,None,2,False,1,0]) == [1,None,2,False,1,0,0]
    assert cw.move_zeros(["a","b"]) == ["a","b"]
    assert cw.move_zeros(["a"]) == ["a"]
    assert cw.move_zeros([0,0]) == [0,0]
    assert cw.move_zeros([0]) == [0]


def test_dictionary():
    words=['cherry', 'peach', 'pineapple', 'melon', 'strawberry', 'raspberry', 'apple', 'coconut', 'banana']
    test_dict = cw.Dictionary(words)
    assert test_dict.find_most_similar('strawbery') =='strawberry'
    assert test_dict.find_most_similar('berry') =='cherry'
    assert test_dict.find_most_similar('aple') =='apple'
