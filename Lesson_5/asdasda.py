from collections import namedtuple, Counter
# fruit = namedtuple('fruit', 'number variety color')
# a = fruit(number=2, variety='Honeycrisp', color='Green')
# b = fruit(number=5, variety='Greencrisp', color='Red')

c = Counter(a=5).elements()
print(list(c))

# print(a.variety)
# print(a.color)

# s = 'the lazy dog jumped over another lazy dog'
# words = s.split()
# Counter(words).most_common(3)
# print(Counter(words).most_common())
