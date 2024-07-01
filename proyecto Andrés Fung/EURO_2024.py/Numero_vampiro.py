from itertools import permutations

#Funcion para determinar si un numero es vampiro
def is_vampire_number(number):
    number_str = str(number)
    length = len(number_str)
    # Revisa si el numero es par
    if length % 2 != 0:
        return False
    # Genera todas las posibilidades de colmillos y sus combinanciones para confirmar si alguna es igual al numero original
    length_half = length // 2
    possible_fangs = permutations(number_str, length_half)
    
    fangs_set = set()

    for fangs in possible_fangs:
        fangs_str = ''.join(fangs)
        if fangs_str[0] != '0':
            other_fangs = number_str
            for num in fangs_str:
                other_fangs = other_fangs.replace(num, '', 1)
            if other_fangs[0] != '0':
                fang1, fang2 = int(fangs_str), int(other_fangs)
                if fang1 * fang2 == number:
                    fangs_set.add((fang1, fang2))
    
    return bool(fangs_set)


