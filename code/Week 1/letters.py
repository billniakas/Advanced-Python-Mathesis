# Άσκηση 1.4
# βρείτε τη συχνότητα εμφάνισης αλφαβητικών χαρακτήρων που βρίσκονται σε κείμενο
# αρχείου που δίνει ο χρήστης
freq = {}
tonoi = {'ά': 'α', 'έ': 'ε', 'ή': 'η', 'ί': 'ι', 'ό': 'ο', 'ύ': 'υ', 'ώ': 'ω',
         'ΐ': 'ι', 'ΰ': 'υ', 'ϊ': 'ι', 'ϋ': 'υ'}
try:
    fname = input('Όνομα αρχείου:')
    with open(fname, 'r', encoding='utf-8') as fin:
        txt = fin.read()
    # print(txt)
    for t in tonoi:
        txt = txt.lower().replace(t, tonoi[t])
    for ch in txt.lower():
        if ord('ώ') >= ord(ch) >= ord('ά'):
            freq[ch] = freq.get(ch, 0) + 1
    for ch in sorted(freq): print(ch, freq[ch])

except FileNotFoundError:
    print('δεν βρέθηκε το αρχείο')