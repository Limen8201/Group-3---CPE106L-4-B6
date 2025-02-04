import unittest
import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __repr__(self):
        return f"Card('{self.suit}', '{self.value}')"


class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if self.cards:
            return self.cards.pop()
        return None 


class TestCard(unittest.TestCase):
    def test_card_creation(self):
        card = Card("Hearts", "Ace")
        self.assertEqual(card.suit, "Hearts")
        self.assertEqual(card.value, "Ace")

    def test_card_string_representation(self):
        card = Card("Diamonds", "King")
        self.assertEqual(str(card), "King of Diamonds")

class TestDeck(unittest.TestCase):
    def setUp(self):  
        self.deck = Deck()

    def test_deck_creation(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_deck_shuffle(self):
        original_deck = list(self.deck.cards) 
        self.deck.shuffle()
        self.assertNotEqual(self.deck.cards, original_deck) 

    def test_deal_card(self):
        card = self.deck.deal_card()
        self.assertIsInstance(card, Card)
        self.assertEqual(len(self.deck.cards), 51)

    def test_deal_card_empty_deck(self):
        for _ in range(52):  
            self.deck.deal_card()
        card = self.deck.deal_card()
        self.assertIsNone(card)  


if __name__ == '__main__':
    unittest.main()