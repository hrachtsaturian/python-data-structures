def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    dict_of_ltr = {}
    
    for char in phrase: 
        dict_of_ltr[char] = dict_of_ltr.get(char, 0) + 1 

    
    return dict_of_ltr 