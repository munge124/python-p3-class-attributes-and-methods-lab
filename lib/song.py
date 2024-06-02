class Song:
    count = 0
    genres = []
    genre_count = {}
    artists = []
    artist_count = {}

    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
    pass

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls,genre):
        if len(cls.genres) == 0:
            cls.genres.append(genre)
            cls.genre_count[genre] = 0
        else:
            if genre not in cls.genres:
                cls.genres.append(genre)
                cls.genre_count[genre] = 0
                
    @classmethod
    def add_to_artists(cls,artist):
        if len(cls.artists) == 0:
            cls.artists.append(artist)
            cls.artist_count[artist] = 0
        else:
            if artist not in cls.artists:
                cls.artists.append(artist)
                cls.artist_count[artist] = 0           

    @classmethod
    def add_to_genre_count(cls,genre):
        cls.genre_count[genre] += 1         

    @classmethod
    def add_to_artist_count(cls,artist):
        cls.artist_count[artist] += 1       
