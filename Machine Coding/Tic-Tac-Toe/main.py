from board import Board
from user import User
from rule.ruleFactory import RuleFactory
from notifier.consoleNotifier import ConsoleNotifier
from game import Game

def main():
    board = Board(3)
    ruleFactory = RuleFactory()
    rowRule = ruleFactory.createRule("row")
    colRule = ruleFactory.createRule("col")
    diagRule = ruleFactory.createRule("diag")
    console = ConsoleNotifier()

    gameRules = [rowRule, colRule, diagRule]

    game = Game(board, gameRules)

    user1 = User(1, "Harsh", "X")
    user2 = User(2, "Rohit", "O")

    game.addUser(user1)
    game.addUser(user2)

    game.addObserver(console)

    game.play()

if __name__ == "__main__":
    main()