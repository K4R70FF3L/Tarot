import random

numbers = ['Ace', '2', '3', '4', '5', '6', '7', '8',
           '9', '10', 'Page', 'Knight', 'Queen', 'King']

group = ['Fool', 'Magician', 'High Priestess', 'Empress', 'Emperor', 'Hierophant', 'Lovers', 'Chariot', 'Strength', 'Hermit',
         'Wheel of Fortune', 'Justice', 'Hanged Man', 'Death', 'Temperance', 'Devil', 'Tower', 'Star', 'Moon', 'Sun', 'Judgement', 'World']
relationship = [number + ' of ' +
                suit for number in numbers for suit in ['Cups', 'Wands']]
location = [number + ' of ' +
            suit for number in numbers for suit in ['Swords', 'Coins']]


def drawCard(stack):
    card = random.choice(stack)
    stack.remove(card)
    return card


def drawCards(stack, amount):
    return [drawCard(stack) for x in range(amount)]


players = {}

print('Enter player names:')
line = input('->')
while line != '':
    players[line] = {'group': drawCards(group, 1), 'relationship': drawCards(
        relationship, 2), 'location': drawCards(location, 2)}
    line = input('->')


print("Draw a 'g'roup, 'r'elationship or 'l'ocation card.")

line = input('->')
while line != '':
    if line == 'g':
        card = random.choice(group)
        print(card + (' - upside down' if random.random()
                      > .5 else ' - right-side up'))
        group.remove(card)
    elif line == 'r':
        card = random.choice(relationship)
        print(card)
        relationship.remove(card)
    elif line == 'l':
        card = random.choice(location)
        print(card)
        location.remove(card)
    else:
        print('Please enter only one of the following characters: g, r, l.')
    line = input('->')
