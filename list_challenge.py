import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    choice = input("Hit ENTER to pick a card or Q (followed by ENTER)to quit:")
    if choice == "Q":
        print("Goodbye!")
        break    
    draw = random.choice(diamonds)
    hand.append(draw)
    diamonds.remove(draw)
    print(hand)
    print(diamonds)
    if not diamonds:
        print("There are no more cards to pick")