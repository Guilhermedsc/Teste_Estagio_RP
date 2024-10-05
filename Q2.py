import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([char for char in nfkd_form if not unicodedata.combining(char)])

def count_letter_a_with_accents(input_string):
    normalized_string = remove_accents(input_string.lower())
    
    count_a = normalized_string.count('a')
    
    if count_a > 0:
        return f"A letra 'a'/'A' (ou suas variantes) ocorreu {count_a} vezes na string."
    else:
        return "A letra 'a'/'A' (ou suas variantes) não foi encontrada na string."

string = input("Informe uma string: ")
print(count_letter_a_with_accents(string))
