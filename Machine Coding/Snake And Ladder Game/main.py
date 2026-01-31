from abc import ABC, abstractmethod
from collections import deque
import random

# -------------------- Board Entities --------------------

class BoardEntity:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def display(self):
        print(f"{self.__class__.__name__}: {self.start} -> {self.end}")


class Snake(BoardEntity):
    pass


class Ladder(BoardEntity):
    pass


# -------------------- Board --------------------

class Board:
    def __init__(self, size):
        self.size = size
        self.entities = {}

    def add_board_entity(self, entity):
        self.entities[entity.start] = entity

    def get_entity(self, pos):
        return self.entities.get(pos)

    def setup_board(self, strategy):
        strategy.setup_board(self)

    def display(self):
        print(f"Board size: {self.size}")
        for e in self.entities.values():
            e.display()


# -------------------- Setup Strategy --------------------

class SetupStrategy(ABC):
    @abstractmethod
    def setup_board(self, board):
        pass


class StandardSetup(SetupStrategy):
    def setup_board(self, board):
        board.add_board_entity(Snake(14, 7))
        board.add_board_entity(Snake(99, 5))
        board.add_board_entity(Ladder(3, 22))
        board.add_board_entity(Ladder(8, 26))


class RandomSetup(SetupStrategy):
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def setup_board(self, board):
        count = {"Easy": 4, "Medium": 6, "Hard": 8}[self.difficulty]
        for _ in range(count):
            start = random.randint(2, board.size - 1)
            end = random.randint(1, board.size - 2)
            if start > end:
                board.add_board_entity(Snake(start, end))
            else:
                board.add_board_entity(Ladder(start, end))


class CustomSetup(SetupStrategy):
    def __init__(self, snakes, ladders):
        self.snakes = snakes
        self.ladders = ladders

    def setup_board(self, board):
        for s, e in self.snakes:
            board.add_board_entity(Snake(s, e))
        for s, e in self.ladders:
            board.add_board_entity(Ladder(s, e))


# -------------------- Rules --------------------

class Rules(ABC):
    @abstractmethod
    def is_valid_move(self, pos, dice, board_size):
        pass

    @abstractmethod
    def check_win(self, pos, board_size):
        pass

    @abstractmethod
    def calc_new_pos(self, pos, dice, board):
        pass


class StandardRules(Rules):
    def is_valid_move(self, pos, dice, board_size):
        return pos + dice <= board_size

    def check_win(self, pos, board_size):
        return pos == board_size

    def calc_new_pos(self, pos, dice, board):
        new_pos = pos + dice
        entity = board.get_entity(new_pos)
        if entity:
            return entity.end
        return new_pos


# -------------------- Dice --------------------

class Dice:
    def __init__(self, faces=6):
        self.faces = faces

    def roll(self):
        return random.randint(1, self.faces)


# -------------------- Player --------------------

class Player:
    def __init__(self, pid, name):
        self.id = pid
        self.name = name
        self.position = 0


# -------------------- Observer --------------------

class Observer(ABC):
    @abstractmethod
    def update(self, msg):
        pass


class ConsoleNotifier(Observer):
    def update(self, msg):
        print(msg)


# -------------------- Game --------------------

class Game:
    def __init__(self, board, dice, rules):
        self.board = board
        self.dice = dice
        self.rules = rules
        self.players = deque()
        self.observers = []
        self.game_over = False

    def add_player(self, player):
        self.players.append(player)

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, msg):
        for obs in self.observers:
            obs.update(msg)

    def play(self):
        self.notify("Game started!")
        self.board.display()

        while not self.game_over:
            player = self.players.popleft()
            roll = self.dice.roll()
            self.notify(f"{player.name} rolled {roll}")

            if self.rules.is_valid_move(player.position, roll, self.board.size):
                new_pos = self.rules.calc_new_pos(player.position, roll, self.board)
                self.notify(f"{player.name} moves from {player.position} to {new_pos}")
                player.position = new_pos

                if self.rules.check_win(player.position, self.board.size):
                    self.notify(f"{player.name} WON the game!")
                    self.game_over = True
                    break
            else:
                self.notify(f"{player.name} cannot move")

            self.players.append(player)


# -------------------- Example Run --------------------

if __name__ == "__main__":
    board = Board(100)
    setup = StandardSetup()
    board.setup_board(setup)

    dice = Dice()
    rules = StandardRules()

    game = Game(board, dice, rules)
    game.add_observer(ConsoleNotifier())

    game.add_player(Player(1, "Alice"))
    game.add_player(Player(2, "Bob"))

    game.play()
