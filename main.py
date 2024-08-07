import random 
'''
Creating the cards in a diccionary'''
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
values = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, 
          "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}
ranks = ("Two", "Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")


class Card: 
    '''
    Creating a class for a card
    '''
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        

    def __str__(self):
        return self.rank + " of " + self.suit

        
class Deck:
    '''
    Creating a list with a for loop
    '''
    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #creating a card

                created_card = Card(suit,rank)

                self.all_cards.append(created_card)

    
    def shuffle(self):
        '''
        Shuffling the cards
        '''

        random.shuffle(self.all_cards)
        '''
        No need to return ,because the sorted list stays 
        (shuffle does not return nothing )
        '''
        

    def deal_one(self):
        '''
        Dropping the last card of the deck'''
        
        return self.all_cards.pop(-1)
        '''
        Important to return it ,so have the value 
        '''

class Player:
    '''
    Creating the Player class with a name as a parameter  '''

    def __init__(self,name):
            
        self.all_cards = []
        self.name = name 


    def remove_one(self):
        #Dropping the first item in the list
        return self.all_cards.pop(0)
            

        
    def add_cards(self,new_cards):

        if type(new_cards) == type([]):
            #Adding list with another list
            self.all_cards.extend(new_cards)
            #Adding a single object 
        else: self.all_cards.append(new_cards)


    def __str__(self):
        return f"Player  {self.name} has {len(self.all_cards)}"
    


    #Game setup

player_one = Player("player_one")
player_two = Player("player_two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

    #Game starts
round = 0
game_on = True

while game_on:
    #Counting the rounds
    round += 1

    if len(player_one.all_cards) == 0:
        print(f"player one out of cards\n ")
        print("player two has won the game ")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print(f"player two out of cards ")
        print("player one has won the game")
        game_on = False
        break


    #Start a new round

    player_one_cards = []
    '''List for the cards on the table'''
    player_one_cards.append(player_one.remove_one())
    ''' Add the card that is removing from index 0 from player_one list '''
    

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    
    at_war = True 
   
    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            ''' If player 1 card are greater than player two '''
            
            player_one.add_cards(player_two_cards)
            player_one.add_cards(player_one_cards)
            ''' Player one keeps the cards'''
            
            at_war = False
            
            ''' End the loop'''
        
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            
            at_war = False
            
        
        else: 
            print("at war")

            if len(player_one.all_cards) < 5 :
                '''
                The player is not going to continue if doesn't have enough cards
                '''
                print("Player two has won the game")
            
                game_on = False
                break
                

            elif len(player_two.all_cards) < 5 :
                 print("Player one has won the game")
                 
                 game_on = False
                 break
                 

            else:
                
                for card in range(5):
                    '''
                    Adding 5 cards to the list 
                    '''
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())




    

            

            


                









    



    
        













