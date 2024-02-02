import random
from random import shuffle

class Card:
    suits = ["Espada", "Basto", "Oro", "Copa"]
    values = ["7", "6", "5", "4", "3", "2", "1","12","11","10"]
    
    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __str__(self):
        return f"{self.suit} de {self.value}"
    



class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in Card.suits for value in Card.values]

    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()



class Player:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mazoCartas = []
        self.puntos = 0
        self.victorias = 0

    def agarrarCarta(self, deck):
        self.mazoCartas.append(deck.deal())

    def play_card(self):
        return self.mazoCartas.pop
    
    def mostrarMazo(self):
        for card in self.mazoCartas:
            print(card)


class Truco:
    def __init__(self):
        nombre1 = input("nombre de jugador 1")
        nombre2 = input("nombre de jugador 2")
        self.deck = Deck()
        self.P1 = Player(nombre1)
        self.P2 = Player(nombre2)

    def rondaDePrueba(self):
        self.deck.shuffle()
        for _ in range(3):
            self.P1.agarrarCarta(self.deck)
            self.P2.agarrarCarta(self.deck)
            
        print(f"Mazo de cartas de {self.P1.nombre}:")
        self.P1.mostrarMazo()

        print(f"Mazo de cartas de {self.P2.nombre}:")
        self.P2.mostrarMazo()
    

if __name__ == "__main__":
    juego = Truco()
    juego.rondaDePrueba()
