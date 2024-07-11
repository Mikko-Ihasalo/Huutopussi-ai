from . import game_mechanic_classes as gmc


def return_legal_cards(player: gmc.Player, active_trump: int | None, starter_card: gmc.Card | None):
    """
    Checks which cards are playable and returns them.

    Parameters
    ----------
    player : gmc.Player
        The player whose cards are to be checked.
    active_trump : int|None
        The trump suit of the current round.
    starter_card : gmc.Card|None
        The first card of the round.
    """

    if starter_card == None:
        return list(player.hand.cards.keys())

    playable_cards = [
        card for card in player.hand.cards if card[0] == starter_card.value[0]]

    if len(playable_cards) > 0:
        playable_cards_higher_rank = [
            card for card in playable_cards if card[1] > starter_card.value[1]]

        if len(playable_cards_higher_rank) > 0:
            return playable_cards_higher_rank

        else:
            return playable_cards

    elif active_trump != None and len(playable_cards) == 0:
        playable_cards = [
            card for card in player.hand.cards if card[0] == active_trump]

        if len(playable_cards) > 0:
            return playable_cards

    else:
        return list(player.hand.cards.keys())
