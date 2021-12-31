from duck import MallardDuck, DecoyDuck

if __name__ == '__main__':
    duck = MallardDuck()
    print('Кряква:')
    print(duck.perform_fly())
    print(duck.perform_quack())

    decoy = DecoyDuck()
    print('\nПриманка:')
    print(decoy.perform_fly())
    print(decoy.perform_quack())
