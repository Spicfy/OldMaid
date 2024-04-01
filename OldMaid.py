import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print('***********************************************************')
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    x = deck
    random.shuffle(x)
    return x

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]
     getdeck = make_deck()
     getdeck = shuffle_deck(getdeck)

     for i in range(0, 51, 2):
        other.append(getdeck[i])
     for i in range(1, 51, 2):
         dealer.append(getdeck[i])
     
    

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE

     return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''
    del_list = []
    skipposition = []
    new_list = []
    for i in range(len(l)):
        track = 1
        while i + track < len(l):
            if (i not in skipposition) and ((l[i])[0] == (l[i + track])[0]):
                skipposition.append(i)
                skipposition.append(i + track)
                del_list.append(l[i])
                del_list.append(l[i + track])
            track += 1
    for i in range(len(l)):
        if l[i] not in del_list:
            new_list.append(l[i])

        
    random.shuffle(new_list)
    return new_list

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE

    #random.shuffle(no_pairs)
    #return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''
    print(deck)

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
def get_valid_input(response, n):
     '''
     (int, int)-> bool
     Returns an bool depending if response is between [1, n]
     
     Precondition: n>=1 
     '''
     
     return 1 <= response <= n 
def ask_for_card(deck, returner, turn):
     '''
     ([list of strings], int, int) --> 
     '''
     if turn % 2 == 1:
        print('I have ' + str(returner) + ' cards. if 1 stands for my first card and ' + str(returner) + ' stands for my last card whcih of my cards would you like?' )
        response = int(input('Give me an integer between 1 and ' + str(returner) + ': '))
        validity = get_valid_input(response, returner)
        while not validity:
            response = int(input('Invalid number. Please enter integer between 1 and ' + str(returner) + ': '))
            if get_valid_input(response, returner) == True:
                validity = True
            else:
                validity = False
        print('You asked for my ' + str(response) + ' card.\nhere it is. it is ' + deck[response - 1])
     else:
         print('I took your card number: ' + str(returner))
         response = returner

     return deck[response - 1]
     
         
         
     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE

def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     deck = shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)
     turn = 1
     flag = True
     while flag:
        if (turn % 2) == 1:
            print('Your turn')
            print('Your current deck of cards is: ')
            print_deck(human)
            newcard = ask_for_card(dealer, len(dealer), turn)
            human.append(newcard)
            dealer.remove(newcard)
            print('with ' + newcard + ' added, your current deck of cards is:')
            print_deck(human)
            human = remove_pairs(human)
            human = shuffle_deck(human)
            print('And after discarding pairs and shuffling, your deck is: ')
            print_deck(human)
            wait_for_player()
        elif turn%2 == 0:
            print('My turn')
            robo_num = random.randint(1, len(human))
            robo_card = ask_for_card(human, robo_num, turn)
            dealer.append(robo_card)
            human.remove(robo_card)
            dealer = remove_pairs(dealer)
            dealer = shuffle_deck(dealer)
            wait_for_player()

        if len(dealer) == 0 or len(human) == 0:
            if len(human) == 0:
                print('Ups. You do not have any more cards.\nCongratulations! You, Human, win')
            elif len(dealer) == 0:
                print('Ups. I do not have any more cards\nYou lost! I, Robot, win')
            flag = False


            

        turn += 1
            

        
        
        # COMPLETE THE play_game function HERE
        # YOUR CODE GOES HERE
	
	 

# main
play_game()