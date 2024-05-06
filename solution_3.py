import time
import datetime


class Track:
    '''
    Models a single track in an album.

    Attributes:
    - name (str): The name of the track.
    - duration (int): The duration of the track in seconds.
    - artist (str): The artist who performed the track.
    - year (int): The year the track was released.
    - album (str): The album the track is part of.
    - is_playing (bool): Indicates whether the track is currently playing.
    - start_time (float): The time at which the track started playing (in seconds since the epoch).
    - pause_time (float): The time at which the track was paused (in seconds since the epoch).
    - pause_duration (int): The total amount of time the track has been paused (in seconds).
    - stop_time (int): The total amount of time the track has been stopped (in seconds).

    Methods:
    - play(): Starts playing the track.
    - pause(): Pauses the track.
    - stop(): Stops the track.
    - resume(): Resumes playing the track.
    - is_over(): Checks if the track has finished playing.
    - __str__(): Returns a string representation of the track.
    '''
    def __init__(self, name, duration, artist, year, album):
        '''
        Initializes a Track object.

        Parameters:
        name (str): The name of the track.
        duration (int): The duration of the track in seconds.
        artist (str): The artist of the track.
        year (int): The year the track was released.
        album (str): The name of the album to which the track belongs.
        '''
        self.name = name
        self.duration = duration
        self.artist = artist
        self.year = year
        self.album = album
        self.is_playing = False
        self.start_time = None
        self.pause_time = None
        self.pause_duration = 0
        self.stop_time = 0

    def play(self):
        '''
        Starts playing the track.
        '''
        if not self.is_playing:
            self.is_playing = True
            self.start_time = time.time() - self.stop_time
            print(f'▶️ : {self.name}, длительность трека {self._format_time(self.duration)}')


    def pause(self):
        '''
        Pauses the track.
        '''
        if self.is_playing and not self.is_over():
            self.is_playing = False
            self.pause_time = time.time()
            self.pause_duration += (self.pause_time - self.start_time)
            self.stop_time = self.pause_time - self.start_time
            print(f'⏸ : {self.name} на {self._format_time(self.stop_time)}')
        else:
            print(f"Трек '{self.name}' не воспроизводится.")

    def stop(self):
        '''
        Stops playing the track.
        '''
        if self.is_playing or self.pause_duration > 0:
            self.is_playing = False
            self.pause_duration = 0
            self.stop_time = 0
            print(f'⏹ : Трек {self.name}')

    def resume(self):
        '''
        Resumes playing the track after a pause.
        '''
        if self.pause_duration > 0 and not self.is_over():
            self.is_playing = True
            self.start_time = time.time() - self.pause_duration
            print(f'▶️ : {self.name} перезапущен с {self._format_time(self.stop_time)}')

                  
    def is_over(self):
        '''
        Checks if the track has finished playing.

        Returns:
        bool: True if the track is over, False otherwise.
        '''
        if self.is_playing:
            current_time = time.time()
            elapsed_time = current_time - self.start_time - self.pause_duration
            if elapsed_time >= self.duration:
                self.stop()
                print(f'Трек {self.name} закончен')
                return True
        return False
    
    def _format_time(self, seconds):
        return time.strftime('%M:%S', time.gmtime(seconds))
    
    def __str__(self):
        '''
        Returns a string representation of information about the track.

        Parameters:
        None

        Returns:
        A string representing the track.
        '''
        return f'Название {self.name}, {self.duration}, {self.artist}, {self.album}'


class Album:
    '''
    Models an album of music.

    Attributes:
    - name (str): The name of the album.
    - year (int): The year the album was released.
    - artist (str): The artist who performed the album.
    - tracks (list of Track): The tracks on the album.

    Methods:
    - add_track(track): Adds a track to the album.
    - play_track(track_name): Starts playing the specified track on the album.
    - pause_track(track_name): Pauses the specified track on the album.
    - stop_track(track_name): Stops the specified track on the album.
    - resume_track(track_name): Resumes playing the specified track on the album.
    '''
    def __init__(self, name, year, artist):
        '''
        Initializes an Album object.

        Parameters:
        name (str): The name of the album.
        year (int): The year the album was released.
        artist (str): The artist of the album.
        '''
        self.name = name
        self.year = year
        self.artist = artist
        self.tracks = []

    def add_track(self, track):
        '''
        Adds a track to the album.

        Parameters:
        track (Track): The track object to add.
        '''
        self.tracks.append(track)

    def play_track(self, track_name):
        '''
        Starts playing a specific track from the album.

        Parameters:
        track_name (str): The name of the track to play.
        '''
        for track in self.tracks:
            if track.name == track_name:
                track.play()
                break

    def pause_track(self, track_name):
        '''
        Pauses a specific track from the album.

        Parameters:
        track_name (str): The name of the track to pause.
        '''
        for track in self.tracks:
            if track.name == track_name:
                track.pause()
                break

    def stop_track(self, track_name):
        '''
        Stops playing a specific track from the album.

        Parameters:
        track_name (str): The name of the track to stop.
        '''
        for track in self.tracks:
            if track.name == track_name:
                track.stop()
                break

    def resume_track(self, track_name):
        '''
        Resumes playing a specific track from the album after a pause.

        Parameters:
        track_name (str): The name of the track to resume.
        '''
        for track in self.tracks:
            if track.name == track_name:
                track.resume()
                break

