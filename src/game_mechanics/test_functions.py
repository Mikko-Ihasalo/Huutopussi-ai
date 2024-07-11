import pytest


from . import game_mechanic_classes as gmc
from . import game_mechanic_functions as gmf

def test_return_legal_cards():
    errors = []
    test_player = gmc.Player("Testaaja")
    test_player.hand.clear_hand()

    test_player.hand.add_card([gmc.Card(0,i) for i in range(5)])
    test_player.hand.add_card([gmc.Card(1,i) for i in range(3)])
    test_player.hand.add_card([gmc.Card(2,0),gmc.Card(0,8)])

    test_cards =gmf.return_legal_cards(player=test_player,active_trump=1,starter_card=gmc.Card(0,1)) # test lower,higher and trump cards

    if len(test_player.hand) != 10:
        errors.append(f"!!!ERROR 1 !!! Player cards length is not 10.{len(test_player.hand)}")

    if len(test_cards) != 4:
        errors.append(f"!!!ERROR 2 !!! Playable cards length is not 4. {len(test_cards)} {test_cards}")

    if gmc.Card(0,0).value in test_cards:
        errors.append(f"!!!ERROR 3 !!! Playable card (0,0) is in playable cards. {test_cards}")
    if gmc.Card(1,1).value in test_cards:
        errors.append(f"!!!ERROR 4 !!! Playable card (1,1) is in playable cards. {test_cards}")

    if not gmc.Card(0,4).value  in test_cards:
        errors.append(f"!!!ERROR 5 !!! Playable card (0,4) is not in playable cards. {test_cards}")
    
    test_player.hand.clear_hand()
    test_player.hand.add_card([gmc.Card(0,0),gmc.Card(0,4)])
    test_player.hand.add_card([gmc.Card(1,i) for i in range(8)])
    test_cards =gmf.return_legal_cards(player=test_player,active_trump=1,starter_card=gmc.Card(0,5)) # test only lower non trump cards

    if len(test_cards) != 2:
        errors.append(f"!!!ERROR 6 !!! Playable cards length is not 2. {len(test_cards)}")

    if not gmc.Card(0,0).value in test_cards:
        errors.append(f"!!!ERROR 7 !!! Playable card (0,0) is not in playable cards. {test_cards}")

    test_cards =gmf.return_legal_cards(player=test_player,active_trump=1,starter_card=gmc.Card(3,5)) # test trump cards

    if len(test_cards) != 8:
        errors.append(f"!!!ERROR 8 !!! Playable cards length is not 8. {len(test_cards)}")

    if not gmc.Card(1,0).value in test_cards:
        errors.append(f"!!!ERROR 9 !!! Playable card (1,0) is not in playable cards. {test_cards}")

    if gmc.Card(3,5).value in test_cards:
        errors.append(f"!!!ERROR 10 !!! Playable card (3,5) is in playable cards. {test_cards}")
    
    if gmc.Card(1,7).value not in test_cards:
        errors.append(f"!!!ERROR 11 !!! Playable card (1,8) is not in playable cards. {test_cards}")
    
    test_cards = gmf.return_legal_cards(player=test_player,active_trump=1,starter_card=None) # test starting player

    if len(test_cards) != 10:
        errors.append(f"!!!ERROR 12 !!! Playable cards length is not 10. {len(test_cards)}")
    
    if test_cards != list(test_player.hand.cards.keys()):
        errors.append(f"!!!ERROR 13 !!! Playable cards is not player hand. {test_cards} {test_player.hand.cards}")

    test_cards = gmf.return_legal_cards(player=test_player,active_trump=None,starter_card=gmc.Card(3,0)) # test starting player

    if len(test_cards) != 10:
        errors.append(f"!!!ERROR 14 !!! Playable cards length is not 10. {len(test_cards)}")

    if test_cards != list(test_player.hand.cards.keys()):
        errors.append(f"!!!ERROR 15 !!! Playable cards is not player hand. {test_cards} {test_player.hand.cards}")



    if len(errors) > 0:
        for error in errors:
            print(error)
        print("\n error count :", len(errors))

    assert len(errors) == 0


    