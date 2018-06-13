class Song(object):

    def __init__(self, lyrics):
        """Constructor, takes string array as an arg"""
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        """Prints the string array to console"""
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sue"])

happy_bday.sing_me_a_song()