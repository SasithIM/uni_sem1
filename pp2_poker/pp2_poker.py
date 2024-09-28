hands = '2H 5H 6H 3H 4H 2C 3S 8S 8D TD'

class Hand:
    def __init__(self, hand):
        self.hand = hand
        self.values = [card[0] for card in hand]
        self.suits = [card[-1] for card in hand]
        for i in range(len(self.values)):
            if self.values[i] == 'T':
                self.values[i] = 10
            elif self.values[i] == 'J':
                self.values[i] = 11
            elif self.values[i] == 'Q':
                self.values[i] = 12
            elif self.values[i] == 'K':
                self.values[i] = 13
            elif self.values[i] == 'A':
                self.values[i] = 14
            else:
                self.values[i] = int(self.values[i])
        
    def is_flush(self):
        return len(set(self.suits)) == 1
    
    def is_straightFlush(self):
        return (sum(self.values) == min(self.values) * 5 + 10) and self.is_flush()
    
    def is_royalFlush(self):
        return self.is_straightFlush() and min(self.values) == 10
    
    def is_fullHouse(self):
        return len(set(self.values)) == 2
    
    def is_threeOfAKind(self):
        return len(set(self.values)) == 3
    
    # def is_highCard(self):
    #     return len(set(self.values)) == 5
    
    def rank(self):
        if self.is_royalFlush():
            return 6
        elif self.is_straightFlush():
            return 5
        elif self.is_fullHouse():
            return 4
        elif self.is_flush():
            return 3
        elif self.is_threeOfAKind():
            return 2
        else:
            return 1

def poker(hands):
    hands = hands.split()
    player1 = Hand(hands[:5])
    player2 = Hand(hands[5:])
    return player1.rank(), player2.rank()

# poker(hands)