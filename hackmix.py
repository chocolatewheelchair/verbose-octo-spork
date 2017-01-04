from tracks import db



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
        for i, v in db.items():
            i_bpm = db[i][0]
            if bpm in range (i_bpm - 3, i_bpm + 3):
                results_bpm.append(i)
# This part is supposed to emulate key change when pitching up the track on a vinyl turntable, it doesn't seem to work tho
            if bpm in range (int(i_bpm * 1.04), int(i_bpm * 1.06)):
                results_bpm_2[i] = v
                for i, v in results_bpm_2.items():
                    if v[1] in range(0,6):
                        v[1] = v[1] + 7
                    if v[1] in range(6,13):
                        v[1] = v[1] - 5

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




