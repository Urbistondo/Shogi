from Board import Board
from Exceptions.CoordinatesOutOfBoundsError import CoordinatesOutOfBoundError
from Exceptions.DestinationSquareOccupiedError import DestinationSquareOccupiedError
from Exceptions.InvalidCoordinateFormatError import InvalidCoordinateFormat
from Game import Game
from MoveController import MoveController
from Pieces.Piece import Color
from Pieces.PieceFactory import PieceFactory


def prompt_move(board, turn, player, move_controller):
    next_color = 'Black' if player == Color.BLACK else 'White'
    print('Turn ' + str(turn) + ' - ' + next_color)

    while True:
        origin_coordinates = input('From (row col):\n')
        try:
            move_controller.validate_coordinates(board, origin_coordinates)
        except (InvalidCoordinateFormat, CoordinatesOutOfBoundError) as e:
            print(e)
            continue

        break

    while True:
        destination_coordinates = input('To (row col):\n')
        try:
            move_controller.validate_coordinates(board, destination_coordinates)
        except (InvalidCoordinateFormat, CoordinatesOutOfBoundError) as e:
            print(e)
            continue

        break

    return (int(origin_coordinates[0]), int(origin_coordinates[1])),\
           (int(destination_coordinates[0]), int(destination_coordinates[1]))


board = Board(9, 9)
piece_factory = PieceFactory()
move_controller = MoveController()
game = Game(board, piece_factory)
game.start_game()

while not game.is_finished():
    game.to_string()
    color = game.get_current_player()
    captured = None

    while True:
        try:
            origin_coordinates, destination_coordinates = prompt_move(board, game.get_turn(), color, move_controller)
            captured = move_controller.move(
                board,
                origin_coordinates, destination_coordinates,
                color
            )
        except (CoordinatesOutOfBoundError, DestinationSquareOccupiedError, InvalidCoordinateFormat) as e:
            print(e)
            continue

        break

    if captured:
        game.add_captured(color, captured)

    game.next_turn()

