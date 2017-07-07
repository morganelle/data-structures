# word_file = open('/usr/share/dict/words')
# word_text = word_file.read().split(' ')
# for i in range(len(word_text)):
#     print(word_text[i])
# word_file.close()
from hash_table import HashTable


def _get_letter_value(char):
    """."""
    try:
        return int(char) + 1
    except ValueError:
        return ord(char) - 54


def _prime_hash(key):
    """Build hash based on prime number and offset."""
    base = 1
    offset = 3
    for char in key:
        base = base * offset + _get_letter_value(char)
    base -= 4
    return base

test_list = ['Aaron', 'Ababdeh', 'abacination', 'abaisance', 'abampere']

def make_dict():
    word_hash = HashTable(36)
    word_file = open('/usr/share/dict/words')
    word_text = word_file.read()
    word_text = str(word_text).strip()
    word_text = word_text.split('\n')
    # iteration = len(word_text)
    print(word_text[-1])
    # for i in range(iteration - 5, iteration):
    #     # if _prime_hash(word_text[i]) % 36 == 34:
    #     # print(word_text[i], _prime_hash(word_text[i]))
    #     # word_hash.set(word_text[i], i)
    word_file.close()
    return word_hash
