__version__ = '0.1.0'

import data_templates
from data_templates import *
from time_dec import *

if __name__ == '__main__':
    # Защита чтобы ide не убирал импорт
    print(time_dec.time)
    print(data_templates.random_word)
