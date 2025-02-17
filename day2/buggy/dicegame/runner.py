from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self, n_round=1, wins=0, loses=0):
        self.dice = Die.create_dice(5)
        self.round = n_round
        self.wins = wins
        self.loses = loses

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        c = 0   # Consecutive wins
        runner = cls()

        while True:

            print("Round {}\n".format(runner.round))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
                c += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                c = 0
            print("Wins(consecutive): {} ({}) Loses {}".format(runner.wins, c, runner.loses))
            runner.round += 1

            if c == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt.lower() == 'y' or prompt == '':
                runner = cls(runner.round, runner.wins, runner.loses)
                continue
            else:
                i_just_throw_an_exception()
