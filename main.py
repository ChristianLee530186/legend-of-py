from src import *

def main():
    startUp()

    while True:
        timer.start()

        data = getInputs()

        update(data)

        render()

        timer.delay(60)

if __name__ == '__main__':
    main()
