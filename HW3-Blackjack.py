import random

class DeckOfCards:
    """
    A class representing a standard deck of 52 playing cards.
    """
    
    def __init__(self):
        """Initialize the deck with 52 cards."""
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [{'suit': suit, 'rank': rank} for suit in suits for rank in ranks]

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def draw_card(self):
        """Draw a card from the deck.

        Returns:
            dict: The drawn card with 'suit' and 'rank'.
        Raises:
            ValueError: If the deck is empty.
        """
        if len(self.cards) == 0:
            raise ValueError("No cards left in the deck.")
        return self.cards.pop()

    def remaining_cards(self):
        """Get the number of remaining cards in the deck.

        Returns:
            int: Number of cards left in the deck.
        """
        return len(self.cards)

    def reset_deck(self):
        """Reset the deck to its initial state."""
        self.__init__()

if __name__ == "__main__":
    # Example usage of the DeckOfCards class
    deck = DeckOfCards()
    print("Initial deck created.")

    # Shuffle the deck
    print("Shuffling the deck...")
    deck.shuffle()
    print("Deck shuffled.")

    # Draw a few cards
    print("Drawing 5 cards:")
    for _ in range(5):
        card = deck.draw_card()
        print(f"Drawn card: {card['rank']} of {card['suit']}")

    # Remaining cards
    print(f"Cards remaining in the deck: {deck.remaining_cards()}")

    # Reset the deck
    print("Resetting the deck...")
    deck.reset_deck()
    print(f"Deck reset. Cards remaining: {deck.remaining_cards()}")
