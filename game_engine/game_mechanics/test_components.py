import pytest


from . import game_mechanic_classes as gmc


def test_create_card():
    errors = []
    test_card = gmc.Card(0,0)
    if type(test_card) != gmc.Card:
        errors.append(f"Card is not a card {test_card}")
    if test_card.value != (0,0):
        errors.append(f"Card value is not (0,0) {test_card.value}")
    assert len(errors) == 0

def  test_create_deck():
    errors = []
    test_deck= gmc.Deck()
    popped_card =test_deck.pop_card()
    if type(popped_card) != gmc.Card:
        errors.append(f"Popped card is not a card {popped_card}")
    if len(test_deck) != 35:
        errors.append(f"Deck length is not 35 {len(test_deck)}")
    if len(errors) > 0:
        for error in errors:
            print(error)
    assert len(errors) == 0
    

def  test_create_Hand():

    errors = []
    test_hand = gmc.Hand()
    removed_card =test_hand.remove_card(gmc.Card(0,0))

    if len(test_hand) != 35:
        errors.append(f"Hand length is not 35 {len(test_hand)}")

    if gmc.Card(0,0).value in test_hand.cards.keys():
        errors.append(f"Card was not removed {test_hand.cards[gmc.Card(0,0).value]}")

    if type(removed_card) != gmc.Card:
        errors.append(f"Card is not a card {removed_card}")

    test_hand.cards.clear()

    if len(test_hand) != 0:
        errors.append(f"Hand length is not 0 {len(test_hand)}")

    test_deck = gmc.Deck()

    test_hand.draw(test_deck,10)
    if len(test_hand) != 10:
        errors.append(f"Hand length is not 10 {len(test_hand)}")
    
    if len(errors) > 0:
        for error in errors:
            print(error)
    assert len(errors) == 0

def test_player():
    player = gmc.Player("test")
    errors = []
    if player.name != "test":
        errors.append(f"Player name is not test {player.name}")

    if type(player.hand) != gmc.Hand:
        errors.append(f"Player hand is not a hand {player.hand}")

    if player.points != 0:
        errors.append(f"Player points is not 0 {player.points}")
    
    if type(player.won_cards) != gmc.Hand:
        errors.append(f"Player won cards deck is {player.won_cards}")

    if len(player.won_cards) != 0:
        errors.append(f"Player won cards length is not 0 {len(player.won_cards)}")

    if len(errors) > 0:
        for error in errors:
            print(error)
    assert len(errors) == 0