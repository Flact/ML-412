
from collections import Counter

def frequencySort(s: str):
        return ''.join(key * value for key, value in Counter(s).most_common())

print(frequencySort('tree'))

# or

""" from collections import Counter
print(''.join(key * value for key, value in Counter('tree').most_common())) """
