from music import *


def main():
    name = input('Введите название песни:')
    duration = int(input('Введите длительность пенсни в секундах:'))
    singer = input('Введите исполнителя:')
    date = input('Введите год выпуска:')
    alb = input('Введите название альбома из которого этот трек:')
    track1 = Track(name, duration, singer, date, alb)
    name_of_alb = ""

    while True:
        time.sleep(1)
        print("Выберите действие:")
        print("1. Воспроизвести трек")
        print("2. Поставить на паузу")
        print("3. Остановить трек")
        print("4. Добавить альбом")
        print("5. Добавить трек в альбом")
        print("6. Воспроизвести трек из альбома")
        print("7. Поставить трек в альбоме на паузу")
        print("8. Выйти")

        choice = input("Введите номер действия: ")
        if choice == "1":
            track1.play()
        elif choice == "2":
            track1.pause()
        elif choice == "3":
            track1.stop()
        elif choice == "4":
            name_of_alb = input("Введите название альбома:")
            year = input("Введите год выпуска:")
            artist = input("Введите исполнителя:")
            alb = Album(name_of_alb, year, artist)
            print(f"Был добавлен альбом {name_of_alb}")
        elif choice == "5":
            if name_of_alb:
                name_in_alb = input('Введите название песни:')
                duration_in_alb = int(input('Введите длительность пенсни в секундах:'))
                singer_in_alb = input('Введите исполнителя:')
                date_in_alb = input('Введите год выпуска:')
                track_in_alb = Track(name_in_alb, duration_in_alb, singer_in_alb,\
                                    date_in_alb, name_of_alb)
                alb.add_track(track_in_alb)
                print(f"Трек {name_in_alb} был добавлен в альбом {name_of_alb}")
            else:
                print("Вы не добавили альбом")
        elif choice == "6":
            print(f"Количесвто песен в альбоме: {len(alb.tracks)}")
            try:
                nomber_of_song = input("Выберите номер песни которую хотите включить:")
                alb.tracks[int(nomber_of_song) - 1].play()
            except:
                IndexError 
                print("Такого номера не существует")

        elif choice == "7":
            if name_of_alb and len(alb.tracks) != 0:
                alb.tracks[int(nomber_of_song)].pause()
        

        elif choice == "8":
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()

