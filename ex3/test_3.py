from music import *


def main():
    name = input('Введите название песни:')
    duration = int(input('Введите длительность пенсни в секундах:'))
    singer = input('Введите исполнителя:')
    date = input('Введите год выпуска:')
    alb = input('Введите название альбома из которого этот трек:')
    track1 = Track(name, duration, singer, date, alb)

    while True:
        time.sleep(1)
        print("Выберите действие:")
        print("1. Воспроизвести трек")
        print("2. Поставить на паузу")
        print("3. Остановить трек")
        print("4. Выйти")

        choice = input("Введите номер действия: ")
        if choice == "1":
            track1.play()
        elif choice == "2":
            track1.pause()
        elif choice == "3":
            track1.stop()
        elif choice == "4":
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()

