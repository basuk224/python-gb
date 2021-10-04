from itertools import islice, zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 'Иван', 'Анастасия', 'Петр', 'Сергей', 'Иван', 'Анастасия', 'Петр', 'Сергей',
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
for ind in klasses:
    if len(klasses) > len(tutors):
        klasses.pop()

re = (i for i in zip_longest(tutors, klasses))

print(*islice(re, 100))
