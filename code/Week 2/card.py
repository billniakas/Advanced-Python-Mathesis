class Card:
    '''κλάση φύλλων τράπουλας'''
    gr_names = {'s': 'Σπαθί ♣', 'c': 'Μπαστουνι ♠', 'h': 'Κούπα ♥', 'd': 'Καρό ♦',
                'A': 'Άσσος', '2': 'Δύο', '3':'Τρία', '4':'Τέσσερα', '5':'Πέντε', '6':'Έξι', '7':'Επτά', '8':'Οκτώ',
                '9': 'Εννιά', 'T': 'Δέκα', 'J': 'Βαλές', 'Q':'Ντάμα', 'K': 'Ρήγας'}
    the_cards = []
    def __init__(self, value, symbol):
        self.value = value.upper().strip()
        self.symbol = symbol.lower().strip()
        Card.the_cards.append(self)

    def __str__(self):
        return self.value+self.symbol
    def detailed_info(self):
        if self.value in Card.gr_names and self.symbol in Card.gr_names:
            return Card.gr_names[self.value]+ ' ' + Card.gr_names[self.symbol]
        else: return ''
# main program
if __name__ == '__main__':
    while True:
        card = input('δώσε φύλλο (αξία, σύμβολο):')
        if card =='': break
        if card.count(',') == 1 and card.split(',')[0].upper() in 'A123456789TJQK' and card.split(',')[1].lower() in 'cshd':
            Card(*card.split(','))
            for c in Card.the_cards:
                print(c, c.detailed_info())