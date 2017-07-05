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
    # word_file = open('/usr/share/dict/words')
    # word_file = word_file.read()
    # word_file = str(word_file).strip()
    # word_text = word_file.split('\n')
    for i in range(len(test_list)):
        if _prime_hash(test_list[i]) % 36 == 34:
            print(test_list[i], _prime_hash(test_list[i]))
        word_hash.set(test_list[i], i)
    # word_file.close()
    return word_hash
