import re

def clean_text(text):
    text_without_date = re.sub('\(\d+\)$', '', text)
    return text_without_date.strip()

movies_list = [
    'Toy Story (1995)',
    'Black Butler: Book of the Atlantic (2017)',
    'No Game No Life: Zero (2017)',
    'Flint (2017)',
    'Bungo Stray Dogs: Dead Apple (2018)',
    'Andrew Dice Clay: Dice Rules (1991)',
]

print(movies_list)
formatted = list(map(clean_text, movies_list))
print(formatted)
