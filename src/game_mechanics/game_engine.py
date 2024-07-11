from . import game_mechanic_classes as gmc
from . import game_mechanic_functions as gmf
from random import randint


class PlayRound:
    """ 
    Plays a round of the game.

    Parameters
    ----------
    players : list
        The players for the game.
    """

    def __init__(self, players: list):
        self.players = players
        self.starter_index = 0
        self.active_trump = None

    def play_round(self):
        """
        Plays a round of the game."""

        played_cards = []
        for i in range(3):
            if i == 0:
                legal_cards = gmf.return_legal_cards(player=self.players[(
                    self.starter_index+i) % 3], active_trump=self.active_trump, starter_card=None)
                # THIS IS A PLACEHOLDER WITH NO POSSIBLE PLAYER INTERACTION YET. TODO: IMPLEMENT PLAYER INTERACTION
                played_card = legal_cards.pop(randint(0, len(legal_cards)-1))
                self.players[(self.starter_index+i) % 3].hand.remove_card(played_card)
                played_cards.append(played_card)
            else:
                legal_cards = gmf.return_legal_cards(player=self.players[(
                    self.starter_index+i) % 3], active_trump=self.active_trump, starter_card=played_cards[0])
                # THIS IS A PLACEHOLDER WITH NO POSSIBLE PLAYER INTERACTION YET. TODO: IMPLEMENT PLAYER INTERACTION
                played_card = legal_cards.pop(randint(0, len(legal_cards)-1))
                self.players[(self.starter_index+i) %
                             3].hand.remove_card(played_card)
                played_cards.append(played_card)
        return played_cards

    def determine_winner(self, played_cards):
        highest_card_index = max(range(3), key=lambda i: played_cards[i].value[1]+13 if played_cards[i].value[0]
                                 == self.active_trump else played_cards[i].value[1])  # find index of highest card
        self.starter_index = (self.starter_index + highest_card_index) % 3
        self.players[self.starter_index].won_cards.add_cards(played_cards)


class BiddingRound:
    def __init__(self, players: list):
        self.players = players
        self.starter_index = 0
        self.active_bidders = self.players[:]
        self.current_bid = 0


    def play_bidding_round(self):
        while True:

            for i in range(len(self.active_bidders)):
                bid =self.active_bidders[(self.starter_index + i) % 3].bid()
                if bid < self.current_bid:
                    self.active_bidders.pop((self.starter_index + i) % 3)
                else:
                    self.current_bid = bid
            if len(self.active_bidders) == 1:
                return self.active_bidders[0]
            
                



                
                

            
