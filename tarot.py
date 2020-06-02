import random

numbers = ['Ace', '2', '3', '4', '5', '6', '7', '8',
           '9', '10', 'Page', 'Knight', 'Queen', 'King']

group = ['Fool', 'Magician', 'High Priestess', 'Empress', 'Emperor', 'Hierophant', 'Lovers', 'Chariot', 'Strength', 'Hermit',
         'Wheel of Fortune', 'Justice', 'Hanged Man', 'Death', 'Temperance', 'Devil', 'Tower', 'Star', 'Moon', 'Sun', 'Judgement', 'World']
relationship = [number + ' of ' +
                suit for number in numbers for suit in ['Cups', 'Wands']]
location = [number + ' of ' +
            suit for number in numbers for suit in ['Swords', 'Coins']]

stacks = {'group': group, 'relationship': relationship, 'location': location}


def drawCard(stack):
    card = random.choice(stack)
    stack.remove(card)
    return card + (' - upside down' if random.random()
                   > .5 else ' - right-side up')


def drawCards(stack, amount):
    return [drawCard(stack) for x in range(amount)]


def askQuestion(player, stack):
    card_number = 1
    if len(player[stack]) > 1:
        print("Which card would you like to reveal? There are " +
              str(len(player[stack])) + " cards left.")
        line = input('->')
        invalid_input = True
        while invalid_input:
            try:
                card_number = int(line)
                if card_number > len(player[stack]) or card_number < 1:
                    print('Please enter a valid number between 1 and ' +
                          str(len(player[stack])) + '.')
                    line = input('->')
                else:
                    invalid_input = False
            except ValueError:
                print('Please enter a valid number between 1 and ' +
                      str(len(player[stack])) + '.')
                line = input('->')

    print(player[stack][card_number - 1])
    del player[stack][card_number - 1]

    # If they don't like the card, draw a new one.
    print("Enter 'a' to ask a different question, or 'c' to continue the game.")
    line = input('->')
    while line != 'c':
        if line == 'a':
            print(drawCard(stacks[stack]))
        else:
            print("Please enter 'a' or 'c'.")
        line = input('->')


def playOneRound(stack):
    player_list = list(players.keys())
    while len(player_list) > 0:
        if len(player_list) == 1:
            line = player_list[0]
            print(line + "'s turn:")
        else:
            print('The current players are: ' + ', '.join(player_list))
            print('Whose turn is it now?')
            line = input('->')
        invalid_input = True
        while invalid_input:
            if line in player_list:
                invalid_input = False
                askQuestion(players[line], stack)
                player_list.remove(line)
            else:
                print("Please enter an actual player who hasn't had his turn yet.")
                line = input('->')


players = {}

print('Enter player names:')
line = input('->')
while line != '':
    players[line] = {'group': drawCards(group, 1), 'relationship': drawCards(
        relationship, 2), 'location': drawCards(location, 2)}
    line = input('->')

gm = {'group': drawCards(group, 5)}

# First round
print('Beginning the first round. This question should be answered by all players after this round is finished:')
askQuestion(gm, 'group')

print('Now the players take turns answering one of their relationship cards.')
playOneRound('relationship')
print('Time for all players to answer the question that was asked at the beginning of the round.')

# Second round
print()
print('Beginning the second round. This question should be answered by all players after this round is finished:')
askQuestion(gm, 'group')

print('Now the players take turns answering one of their location cards.')
playOneRound('location')
print('Time for all players to answer the question that was asked at the beginning of the round.')

# Third round
print()
print('Beginning the third round. This question should be answered by all players after this round is finished:')
askQuestion(gm, 'group')

print('Now the players take turns answering the remaining one of their relationship cards.')
playOneRound('relationship')
print('Time for all players to answer the question that was asked at the beginning of the round.')

# Fourth round
print()
print('Beginning the fourth round. This question should be answered by all players after this round is finished:')
askQuestion(gm, 'group')

print('Now the players take turns answering the remaining one of their location cards.')
playOneRound('location')
print('Time for all players to answer the question that was asked at the beginning of the round.')

# Fifth round
print()
print('Beginning the fourth round. This question should be answered by all players after this round is finished:')
askQuestion(gm, 'group')

print('Now the players take turns answering their group card.')
playOneRound('group')
print('Time for all players to answer the question that was asked at the beginning of the round.')
print()
print()
print()
print()
print()
print('-------------')
print('   THE END')
print('-------------')
