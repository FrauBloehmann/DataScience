""" Tic Tac Toe """
from random import randint
from classes.player import Player
from classes.board import Board

# other functions than main()
def swap_players(first, one, two):
    """ change the player to next """
    if first == one:
        return two
    else:
        return one

# start the game
def main():
    """ start the game """
    board = Board()
    win = False
    place_ok = True
    runde = 1
    name1 = input("Wie heißt SpielerIn 1? ")
    name2 = input("Wie heißt SpielerIn 2? ")

    player1 = Player(name1, 'X', 1)
    player2 = Player(name2, 'O', 2)

    first_player_no = randint(1,2)

    player = player1 if player1.playernumber == first_player_no else player2

    print("Es beginnt " + player.name)

    board.print_board()

    while not win and runde < 10:

        zeile = input(player.name + ", welche Zeile (1,2,3)? ")
        spalte = input("welche Spalte (1,2,3)? ")

        #check, if input & place is valid
        place_ok = board.place_is_ok(zeile, spalte)

        while not place_ok:
            print("Wähle eine LEERE Position AUF dem Spielfeld!")
            zeile = input(player.name + ", welche Zeile (1,2,3)? ")
            spalte = input("welche Spalte (1,2,3)? ")
            place_ok = board.place_is_ok(zeile, spalte)

        board.set_stone(player.symbol, int(zeile)-1, int(spalte)-1)
        board.print_board()

        #check if player wins
        win = board.is_winning(player.symbol)

        if win:
            print("Du hast gewonnen, " + player.name)
            break

        #swap players
        player = swap_players(player, player1, player2)

        runde += 1

    if not win:
        print("niemand hat gewonnen")

if __name__ == "__main__":
    main()
