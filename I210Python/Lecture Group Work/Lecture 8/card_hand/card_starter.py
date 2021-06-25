import cards

# this function creates num cards and sorts them into
# alphabetical order (so we can see multiples)
def make_hand(num):
    hand = []
    for i in range(num):
        hand.append(cards.get_card())
        
    return sorted(hand)

# A hand's value is 20 points for a pair (but not 3+ of a kind)
# + 5 points per Jack, Queen, or King,
# + 7 points per Ace.
def hand_value(my_cards):
    total = 0

    for card in my_cards:
        if my_cards.count(card) == 2:
            total += 10
        if card in "JQK":
            total += 5
        elif card == "A":
            total += 7
        

    return total


#main - test code (don't change this!)
my_hand = make_hand(5)
print("The hand:", my_hand)
print("Its value:", hand_value(my_hand))
    
