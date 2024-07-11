# Huutopussi AI
# Ideana tehda koneoppimalli joka pelaa korttipelia huutopussi.
# %%
from random import choice


class Card:
    """Represents a playing card.

    Attributes:
    ----------
    suit : int
        Card suit.
    rank : int
        Card rank.
    value : tuple
        Card value, easy to get unique card 'id'.
    """

    def __init__(self, suit: int, rank: int):

        self.value = (suit, rank)
        self.suit = self.value_mapping(self.value)[0]
        self.rank = self.value_mapping(self.value)[1]

    def value_mapping(self, value: tuple) -> tuple:
        """Maps suit and rank to card name."""

        suit_map = {0: "Spades", 1: "Clubs", 2: "Diamonds", 3: "Hearts"}
        rank_map = {0: "6", 1: "7", 2: "8", 3: "9",
                    4: "J", 5: "Q", 6: "K", 7: "10", 8: "A"}

        return (suit_map[value[0]], rank_map[value[1]])

    def __repr__(self) -> str:
        """Prints card."""
        return f"{self.rank} of {self.suit}"

    # def __lt__(self, other):
    #    return (self.rank, self.suit) < (other.rank, other.suit) # comparison of 2 cards


class Deck:
    """Represents a deck of playing cards.

    Attributes:
    ----------
    cards : list
        A dictionary of cards. Card value is used as a key.
    """

    def __init__(self):
        self.cards = {(suit, rank): Card(suit, rank) for suit in range(4)
                      for rank in range(9)}  # Add cards to deck with suit and rank

    def __str__(self):
        """Prints deck."""

        return ', '.join(str(card) for card in self.cards)

    def __len__(self):
        """Returns deck size."""

        return len(self.cards)

    def add_card(self, cards: list | Card):
        """Adds card or list of cards to deck.

        Parameters
        ----------
        cards : list or a Card.
        """

        if type(cards) == list:
            for card in cards:
                self.cards[card.value] = card
        else:
            self.cards[cards.value] = cards  # add  a card

    def pop_card(self):
        """Pops a random card from deck."""
        key = choice(list(self.cards.keys()))

        return self.cards.pop(key)


class Hand(Deck):
    """Represents a hand of playing cards.
    Inherits attributes from Deck"""

    def draw(self, deck: Deck, n: int):
        """Draws n cards from deck and adds it to hand.

        Parameters
        ----------
        deck : Deck
            A deck of cards.
        n : int
            Number of cards to draw.
        """
        for _ in range(n):
            self.add_card(deck.pop_card())  # draw a card from the deck

    def remove_card(self, card: Card):
        """Removes a specific card from hand.

        Parameters
        ----------
        card : Card
            A card to remove.
        """
        return self.cards.pop(card.value)

    def clear_hand(self):
        """Removes all cards from hand."""
        self.cards.clear()

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)  # print hand


class Player:
    """Represents a player with name and hand.

    Attributes:
    ----------
    name : str
        Player name.
    hand : Hand
        Player hand.
    points : int
        Player points.
    won_cards : Hand
        A hand of cards that player has won. 
    won_own_tick: bool
        If player won their own tick last turn.
    """

    def __init__(self, name: str):  # player with name and empty hand
        self.name = name
        self.hand = Hand()
        self.won_cards = Hand()
        self.won_cards.clear_hand()
        self.points = 0
        self.won_own_tick = False
        self.bidded_points = 0

    def won_own_tick_set_status(self, status: bool):
        self.won_own_tick = status
    
    def  bid(self, amount: int | None):
        self.bidded_points = amount
        return amount


    def __str__(self):
        return f"{self.name} has {self.points} points and their current hand is {self.hand}"

    def __str__(self):
        return f"{self.player} played {self.card}"


class BiddingSystem:
    def __init__(self, bidders: list):
        self.bidders = bidders
        self.current_bidder_index = 0
        self.highest_bid = 0
        self.current_bid = 0

    def place_bid(self, bidder, amount):
        self.current_bid = amount
        self.current_bidder_index = (
            self.current_bidder_index + 1) % len(self.bidders)

    def pass_bid(self, bidder):
        if bidder == self.bidders[self.current_bidder_index]:
            self.active_bidders.remove(bidder)
            self.current_bidder_index = (
                self.current_bidder_index + 1) % len(self.bidders)

    def run_bidding(self):
        while len(self.active_bidders) > 1:
            current_bidder = self.bidders[self.current_bidder_index]
            print(
                f"{current_bidder}, the current bid is {self.current_bid}. Your move.")
            action = input("Enter 'bid' to raise the bid or 'pass' to pass: ")
            if action == "bid":
                amount = int(input("Enter your bid amount: "))
                self.place_bid(current_bidder, amount)
            elif action == "pass":
                self.pass_bid(current_bidder)
            else:
                print("Invalid action. Please enter 'bid' or 'pass'.")

            print("")

        print(
            f"The winner is {list(self.active_bidders)[0]} with a bid of {self.current_bid}.")


class PlayRound:
    def __init__(self, players: list):
        self.players = players
        self.starter_index = 0

    def play_round(self):
        for i in range(3):
            played_cards = []
            self.players[(self.starter_index + i) % 3]


class Game:
    def __init__(self):
        self.deck = Deck()  # Get a deck for the game
        self.players = [Player(input("p1 name ")), Player(
            input("p2 name ")), Player(input("p3 name "))]  # add players
        self.huudot = [0, 0, 0]
        self.dealer = 0

    def restart_game(self):  # Resets all variables important to the game
        for player in self.players:
            player.hand = Hand()
            player.points = 0
        self.deck = Deck()
        self.huudot = [0, 0, 0]
        self.dealer = 0

    def play_tick(self, winner_n):  # Single tick to play
        played_cards = []
        for i in range(3):
            removed_card = self.players[(winner_n + i) % 3].hand.remove_card()
            while True:
                if removed_card is not None:
                    played_cards.append(removed_card)
                    break
                else:
                    removed_card = self.players[(
                        winner_n + i) % 3].hand.remove_card()
                print(f"played {played_cards}")  # print played cards
        # find index of highest card
        highest_card_index = max(range(3), key=lambda i: played_cards[i].rank)
        # print who won
        print(
            f"highest card was {played_cards[highest_card_index]}. Winner is {self.players[highest_card_index]}")
        # get the index of winner
        winner_n = (winner_n + highest_card_index) % 3
        for card in played_cards:
            self.players[winner_n].won_cards.add_card(
                card)  # add cards to winner's hand

    def count_points(self):
        for player in self.players:
            for card in player.won_cards.cards:
                if card.rank == 10 or card.rank == 13:
                    points += 10
                elif card.rank >= 11:
                    points += 5
            player.points += points

    def start_round(self):
        for player in self.players:
            player.hand.draw(self.deck, 10)  # deal cards
            print(player)  # print players hands
        devils_deck = self.deck  # devils deck of the cards not in any players hand
        bidding_system = BiddingSystem(self.players)  # bidding phase
        bidding_system.run_bidding()
        winner_n = bidding_system.current_bidder_index  # Winner of the bid
        winner = self.players[winner_n]

        winner.hand.draw(devils_deck, 6)
        print(winner.hand)  # winner gets devils deck

        while len(winner.hand.cards) > 10:
            winner.hand.remove_card()  # remove cards from winner's hand until at 10 cards

        while len(self.players[0].hand.cards) > 0:
            self.play_tick(winner_n)  # play rounds until no cards left
        self.count_points()
        print(self.players[0].points,
              self.players[1].points, self.players[2].points)
