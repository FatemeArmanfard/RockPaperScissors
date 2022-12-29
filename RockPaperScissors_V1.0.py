from typing import List, Union
from random import randint


class GameItem:
    """GameItem Class"""

    def __init__(self, name: str):
        """GameItem Initializer

        :param name: str
            name or your item
        """
        self.name: str = name
        self._gt: List[GameItem] = list()
        self._lt: List[GameItem] = list()

    @property
    def greater_than(self):
        return self._gt

    @greater_than.setter
    def greater_than(self, gt):
        self._gt: List[GameItem] = gt

    @property
    def less_than(self):
        return self._lt

    @less_than.setter
    def less_than(self, lt):
        self._lt: List[GameItem] = lt

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return other in self.less_than

    def __gt__(self, other):
        return other in self.greater_than

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "GameItem(name='{}')".format(self.name)


class Result:
    """Result Class"""

    def __init__(self):
        self.wins: int  = 0
        self.loses: int = 0
        self.ties: int  = 0

    def __repr__(self):
        return "Result(wins='{}', loses='{}', ties='{}')".format(
            self.wins, self.loses, self.ties
        )


def lookup(name: str, objectives: List[GameItem]) -> Union[GameItem, None]:
    for o in objectives:
        if o.name == name:
            return o
    return None


if __name__ == "__main__":
    # define our objectives
    rock = GameItem(name='rock')
    paper = GameItem(name='paper')
    scissors = GameItem(name='scissors')

    # add all objectives into a list
    objectives = [
        rock,
        paper,
        scissors,
    ]

    # add rock features
    rock.greater_than = [scissors]
    rock.less_than = [paper]

    # add paper features
    paper.greater_than = [rock]
    paper.less_than = [scissors]

    # add scissors features
    scissors.greater_than = [paper]
    scissors.less_than = [rock]

    result = Result()

    while True:
        # at first computer select its choice
        computer_choice = objectives[randint(0, len(objectives) - 1)]

        # now you need to choose yours
        user_choice = str(input("Your turn: (choices: {}, exit) ".format(', '.join([i.name for i in objectives]))))

        if user_choice.lower() == 'exit':
            print("Good luck :)")
            print(result)
            break

        # validate user input
        user_objective = lookup(user_choice, objectives)
        if user_objective is None:
            print("Invalid input, valid choices: {}".format(', '.join([i.name for i in objectives])))
            continue

        if user_objective > computer_choice:
            print("You win!")
            result.wins += 1
        elif user_objective < computer_choice:
            print("You lose!")
            result.loses += 1
        else:
            print("Tie!")
            result.ties += 1
