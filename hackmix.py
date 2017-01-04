
# This is the "database" the program looks into, format is: "Artist name - Track title" [BPM, root key #]
db = {
    "Proxima - Trapped" : [140, 4],
    "Commodo - Sleepwave" : [137, 6],
    "Roska - Spearhead" : [140, 3],
    "Loefah - Disko Rekah": [145, 8],
    "Lurka - Full Clip": [90, 4],
    "James Blake - Sparing The Horses": [140, 1],
    "Burial - Unite": [138, 2],
    "Joy Orbison - Hyph Mngo": [140, 2],
    "Dub War - The Funky Deal": [140, 12],
    "Skream - Bahl Fwd": [140, 5],
    "Four Tet - Spirit Fingers": [83, 12],
    "Las - Tic": [140, 1],
    "Mala - Cuba Electronic": [140, 3],
    "Boddika - When I Dip": [137,4],
    "Pinch - The Boxer": [142,5],
    "2562 - Techno Dread": [140, 7],
    "Egoless - I'm From The Balkans": [140, 9],
    "Karma - Cha": [140, 10],
    "Gantz - Spry Sinister": [140,8],
    "Kryptic Minds - Six Degrees": [140, 6],
    "Pinch - Dr Carlson": [142,11],
    "Loefah - Goat Stare": [136, 4]
}
# TODO: LEARN MYSQL OR SOMETHING

# keys_dict = {'A': 8, 'A#': 3, 'B': 10,'C': 5,'C#': 12,'D': 7,'D#': 2,'E': 9,'F': 4,'F#': 11,'G': 6,'G#': 1}
# TODO
# Converts the user input key into a number in range(1,12) for convenience
# def key_convert(key):
#     keys_dict = {'A': 8, 'A#': 3, 'B': 10,'C': 5,'C#': 12,'D': 7,'D#': 2,'E': 9,'F': 4,'F#': 11,'G': 6,'G#': 1}
#     key = keys_dict.get(key)


# Variables to be used to store info
results = []
results_bpm = []
results_bpm_2 = {}
results_same_key = []
results_strong_key = []
results_weak_key = []
same_match = []
strong_match = []
weak_match = []

def hackmix():
# Asks user to input a BPM and root key
    print "Please enter a BPM between 80 and 160"
    try:
        bpm = int(raw_input('Enter a BPM '))
        while int(bpm) < 80 or int(bpm) > 160:
            print 'BPM needs to be a number between 80 and 160'
            bpm = int(raw_input('Enter a BPM '))
    except ValueError:
        print "BPM needs to be a number between 80 and 160"
    

    print "Please enter a root key as number between 1 and 12"
    try:
        key = int(raw_input('Enter a root key '))
        while int(key) not in range (1,13):
            print 'Root key needs to be a number between 1 and 12'
            key = raw_input('Enter a root key ')
    except ValueError:
        print "Key needs to be a number between 1 and 12"
# TODO: BETTER INPUT CHECK/ERROR HANDLING 
    
# Checks in database for BPM matches
    def bpm_match(bpm):
        for i in db:
            i_bpm = db[i][0]
            if bpm in range (i_bpm - 3, i_bpm + 3):
                results_bpm.append(i)
            if bpm in range (int(i_bpm * 1.04), int(i_bpm * 1.06)):
                results_bpm_2[db[i]] = db[i][0,1]
                




# Checks in database for key matches
    def key_match_same(key):
        for i in db:
            if key == db[i][1] :
                results_same_key.append(i)
        for i in results_same_key:
            if i in results_bpm:
                same_match.append(i)

    def key_match_strong(key):
        for i in db:
            same_key = db[i][1]
            if key == same_key + 1 or key == same_key - 1:
                results_strong_key.append(i)
        for i in results_strong_key:
            if i in results_bpm:
                strong_match.append(i)

    def key_match_weak(key):
        for i in db:
            same_key = db[i][1]
            if key == same_key + 2 or key == same_key - 2 or key == same_key - 6 or key == same_key +6:
                results_weak_key.append(i)
        for i in results_weak_key:
            if i in results_bpm:
                weak_match.append(i)
    
    bpm_match(bpm)
    key_match_same(key)
    key_match_strong(key)
    key_match_weak(key)

hackmix()
# print 'Tracks within the BPM range', results_bpm
print 'bpm2',results_bpm_2
print 'Tracks in same key within that BPM range', same_match
print 'Tracks in a strong match key within that BPM range', strong_match
print 'Tracks in a weak match key within that BPM range', weak_match




