import sys
from dicegame.runner import GameRunner


def main(mode="run"):
    print("Add the values of the dice")
    print("It's really that easy")
    print("What are you doing with your life.")
    if mode=="debug":
        import ipdb; ipdb.set_trace()
    GameRunner.run()


if __name__ == "__main__":
    try:
        mode = sys.argv[1]
        main(mode)
    except IndexError:
        main()