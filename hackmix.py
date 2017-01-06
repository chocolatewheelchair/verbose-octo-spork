from tracks import db



# TODO or maybe not
# Converts the user input key into a number in range(1,12) for convenience
# def key_convert(key):
#     keys_dict = {'A': 8, 'A#': 3, 'B': 10,'C': 5,'C#': 12,'D': 7,'D#': 2,'E': 9,'F': 4,'F#': 11,'G': 6,'G#': 1}
#     key = keys_dict.get(key)


# Variables to be used to store info
results = []
results_bpm = []
results_bpm_2 = {}
results_bpm_4 = {}
results_bpm_minus2 = {}
results_bpm_minus4 = {}
results_pitched = {}
pitched_key = []
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
            if bpm in range (int(i_bpm * 0.961), int(i_bpm * 1.039)):
                results_bpm.append(i)
# Puts aside tracks that are still within the possible pitching capabilities of a Technics turntable (-8/+8%)
            if bpm in range (int(i_bpm * 1.04), int(i_bpm * 1.06)):
                results_bpm_2[i] = v
            if bpm in range (int(i_bpm * 1.061), int(i_bpm * 1.08)):
                results_bpm_4[i] = v
            if bpm in range (int(i_bpm * 0.96), int(i_bpm * 0.94)):
                results_bpm_minus2[i] = v
            if bpm in range (int(i_bpm * 0.939), int(i_bpm * 0.92)):
                results_bpm_minus4[i] = v
# Changes the root keys to reflect the pitch change on a turntable               
        for i, v in results_bpm_2.items():
            if v[1] in range(0,6):
                v[1] = v[1] + 7
            if v[1] in range(6,13):
                v[1] = v[1] - 5
        for i, v in results_bpm_4.items():
                v[1] = v[1] + 2
        for i, v in results_bpm_minus2.items():
            if v[1] in range(0,6):
                v[1] = v[1] + 5
            if v[1] in range(6,13):
                v[1] = v[1] - 7
        for i, v in results_bpm_minus4.items():
                v[1] = v[1] - 2
        results_pitched.update(results_bpm_2)
        results_pitched.update(results_bpm_4)
        results_pitched.update(results_bpm_minus2)
        results_pitched.update(results_bpm_minus4)


# Checks in database and in the pitched tracks set aside for key matches
    def key_match_same(key):
        for i in db:
            if key == db[i][1] :
                results_same_key.append(i)
            try:
                if key == results_pitched[i][1] :
                    results_same_key.append(i)
            except KeyError:
                pass
        for i in results_same_key:
            if i in results_bpm:
                same_match.append(i)

    def key_match_strong(key):
        for i in db:
            same_key = db[i][1]
            try:
                pitched_key = results_pitched[i][1]
            except KeyError:
                pass
            if key == same_key + 1 or key == same_key - 1:
                results_strong_key.append(i)
            try:
                if key == pitched_key + 1 or key == pitched_key - 1:
                    results_strong_key.append(i)
            except KeyError:
                pass
            except UnboundLocalError:
                pass
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
print 'Tracks in same key within that BPM range', same_match
print 'Tracks in a strong match key within that BPM range', strong_match
print 'Tracks in a weak match key within that BPM range', weak_match


# stuff to add, known bugs: 
# being able to match tracks that are at, say 81 bpm, with tracks at 159 bpm 
# calculations not taking into account whether the vinyl plays at 33 or 45 rpm
# major/minor keys not differentiated 




