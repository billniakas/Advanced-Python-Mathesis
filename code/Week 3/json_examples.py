# Απλό παράδειγμα με JSON

import json
data = [{'a': 'A', 'b': (10, 20.0), 'c': 3.0}]
print('DATA:', repr(data))

j_data = json.dumps(data) # από λίστα python σε json
print('JSON:', j_data)

from_json = json.loads(j_data) # από json σε δεδομένα python
print('DECODED:', from_json)

print('ORIGINAL:', type(data[0]['b']))
print('DECODED :', type(from_json[0]['b']))
Άσκηση

import json
data = {'a': 'A', 'b': (10, 20.0)}
from_json = json.loads(json.dumps(data))

## ποιο θα είναι το αποτέλεσμα;

print(type(data['a']) == type(from_json['a']))
print(type(data['b']) == type(from_json['b']))

# Παράδειγμα με κλειδιά λεξικού μη αλφαριθμητικά

data = [{'a': 'A', 'b': (10, 20.0), ('d',): 'D tuple'}]

print('παράδειγμα με κλειδί λεξικού')
try:
    print(json.dumps(data))
except TypeError as err:
    print('ERROR:', err)

print('παράλειψη μη αλφαριθμητικών κλειδιών')
print(json.dumps(data, skipkeys=True))

# αποθήκευση της δομής json σε αρχείο
with open('file.json', 'w', encoding="utf8") as f:
    json.dump(data, f, skipkeys=True) # προσοχή παράλειψη μη-αλφα κλειδιών

# ανάκτηση από αρχείο
with open('file.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
print(data)