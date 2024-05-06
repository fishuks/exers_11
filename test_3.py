from solution_3 import *

track1 = Track("Каждый раз", 10, "Монеточка", 2020, "Расскраски для взрослых")
track2 = Track("Нет монет", 18, "Монеточка", 2019, "Расскраски для взрослых")
album = Album("Расскраски для взрослых", 2020, "Монеточка")

print(track2)
print(track1.artist)
print(track2.album)
print(track1.duration)
album.add_track(track1)
album.add_track(track2)

album.play_track("Каждый раз")
print(track1.is_playing)
time.sleep(15)  

album.pause_track("Каждый раз")
print(track1.is_playing)
time.sleep(2)

album.resume_track("Каждый раз")
print(track1.is_playing)
time.sleep(2)  

album.stop_track("Каждый раз")
print(track1.is_playing)
time.sleep(2) 

album.play_track("Нет монет")
print(track2.is_playing)
time.sleep(3)

album.pause_track("Нет монет")
print(track2.is_playing)
time.sleep(2)

album.resume_track("Нет монет")
print(track2.is_playing)
time.sleep(2)  

album.stop_track("Нет монет")
print(track2.is_playing)
time.sleep(2) 
