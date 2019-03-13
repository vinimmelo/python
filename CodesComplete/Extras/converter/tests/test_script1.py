from CodesComplete.Extras.converter.script import dictionary_converter, string_converter

def test_script1_with_dictionary():
    result = dictionary_converter("teste conaz")
    assert result == {'a': 1, ' ': 1, 'c': 1, 'e': 2, 'o': 1, 'n': 1, 's': 1, 't': 2, 'z': 1}


def test_script1_with_unified_string():
    result = string_converter("aaaaabbbbccccccaaaaaaa")
    assert result == "5a4b6c7a"

    result2 = string_converter("dddeeerrriiieeeedddd")
    assert result2 == "3d3e3r3i4e4d"
