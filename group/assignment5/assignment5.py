from os.path import commonprefix

dictionary = ['ART', 'RAT', 'CAT', 'CAR']

class AlphabetError(Exception):
    pass

def compute_alphabet(dictionary):
    '''
    Take a pair of adjacent words, find the first mismatching characters in this pair.
    If both characters are absent in the dictinary, append them in the right order.
    If one of the characters is found in the dictionary, insert the not found one
    at the correct position -- before or after the found one.
    If found and inconsistency -- output and error message.
    '''
    alphabet = []
    for first, second in zip(dictionary, dictionary[1:]):
        prefix = commonprefix([first, second])
        first_letter = first[len(prefix)]
        second_letter = second[len(prefix)]
        if first_letter not in alphabet and second_letter not in alphabet:
            alphabet.append(first_letter)
            alphabet.append(second_letter)
        elif first_letter not in alphabet and second_letter in alphabet:
            alphabet.insert(alphabet.index(second_letter), first_letter)
        elif first_letter in alphabet and second_letter not in alphabet:
            alphabet.insert(alphabet.index(first_letter) + 1, second_letter)
        elif first_letter in alphabet and second_letter in alphabet:
            if alphabet.index(first_letter) > alphabet.index(second_letter):
                raise AlphabetError("Inconsistency in the dictionary")
    return alphabet
    
if __name__ == '__main__':
    alphabet = compute_alphabet(dictionary)
    print(alphabet)
