from operator import attrgetter

f = open('Prob08in.txt', 'r')
numTests = int(f.readline())


class Song(object):
    def __init__(self, fullLine):
        self.fullTitle = fullLine.strip('\n')
        self.arrayNames = fullLine.split(' - ')
        self.title = self.arrayNames[0]
        self.artist = ((self.arrayNames[1]).replace('The ','')).lower()
        ##print(repr((self.fullTitle, self.title, self.artist)))
    def __repr__(self):
        return repr((self.fullTitle, self.title, self.artist))

for i in range(numTests): 
    songs = []
    numSongs = int(f.readline())
    for k in range(numSongs):
        songs.append(Song(f.readline()))
    songs.sort(key=attrgetter('artist', 'title'))
    for song in songs:
        print(song.fullTitle)
    
        
f.close()
