import json
import math

results_with_same_bpm = []
results_with_different_bpm = []
results_same_key = []
results_close_key = []
results_weak_key = []
results_same_key_diff_bpm = []
results_close_key_diff_bpm = []
results_weak_key_diff_bpm = []

def hackmix():
# Asks user to input a BPM and root key
    print ("Please enter a BPM between 80 and 160")
    try:
        bpm = int(input('Enter a BPM '))
    except ValueError:
        print ("BPM needs to be a number between 80 and 160")
    

    print ("Please enter a root key as number between 1 and 12")
    try:
        key = int(input('Enter a root key '))
        while int(key) not in range (1,13):
            print ('Root key needs to be a number between 1 and 12')
            key = input('Enter a root key ')
    except ValueError:
        print ("Key needs to be a number between 1 and 12")

    while not 80 <= bpm <= 160:
        if bpm > 160:
            bpm = round(bpm / 2)
        else:
            bpm = round(bpm * 2)

    match(bpm, key)
    match_key(key)
    
    
    strong_matches = set(results_same_key) & set(results_with_same_bpm)
    close_matches = set(results_close_key) & set(results_with_same_bpm)
    weak_matches = set(results_weak_key) & set(results_with_same_bpm)
    strong_matches_diff = set(results_same_key_diff_bpm) & set(results_with_different_bpm)
    close_matches_diff = set(results_close_key_diff_bpm) & set(results_with_different_bpm)
    weak_matches_diff = set(results_weak_key_diff_bpm) & set(results_with_different_bpm)
    #print ('Results with same bpm:', results_with_same_bpm)
    #print ('Results with diff bpm:', results_with_different_bpm)
    #print ('Results with same key:', results_same_key)
    #print ('Results with close key:', results_close_key)
    print ('Strong matches in same tempo ', strong_matches)
    print ('Close matches in same tempo ', close_matches)
    print ('Weak matches in same tempo ', weak_matches)
    #print ('strong key diff', results_same_key_diff_bpm)
    #print ('close key diff', results_close_key_diff_bpm)
    #print ('weak key diff', results_weak_key_diff_bpm)

    print ('Strong matches at a different tempo', strong_matches_diff)
    print ('Close matches at a different tempo ', close_matches_diff)
    print ('Weak matches at a different tempo ', weak_matches_diff)

def match(bpm, key):
    # adds items in the db to list if bpm is the same
        for i, v in db.items():
            item_bpm = db[i][0]
            item_key = db[i][1]
            if bpm == item_bpm:
                results_with_same_bpm.append(i)

            # if bpm is not the same:

            else: 
                # calculates the percentage of change from the two bpms and the semitone changes in pitch
                percent_change = round(((item_bpm - bpm)/bpm)*100)
                semitone_change = round((math.log(bpm/item_bpm)/0.05776227)*100)/100
                if bpm > item_bpm:
                    semitone_change = semitone_change * -1
                else:
                    semitone_change = abs(semitone_change)
                if -10 <= percent_change <= 10:
                    results_with_different_bpm.append(i)

                    change_root_key(item_key,semitone_change)
                    match_key_diff_bpm(i,key, new_key)
                
                    


def match_key(key):
    for i in db:
            item_key = db[i][1]
            if key == item_key:
                results_same_key.append(i)
            if abs(key - item_key) == 1:
                results_close_key.append(i)
            if abs(key - item_key) == 2 or abs(key - item_key) == 6:
                results_weak_key.append(i)

def match_key_diff_bpm(i,key, new_key):
            item_key = new_key
            if key == item_key:
                results_same_key_diff_bpm.append(i)
            if abs(key - item_key) == 1:
                results_close_key_diff_bpm.append(i)
            if abs(key - item_key) == 2 or abs(key - item_key) == 6:
                results_weak_key_diff_bpm.append(i)
        

                



def change_root_key(item_key, semitone_change):
    global new_key
    new_key = item_key
    pitch_change = round(semitone_change)
    if pitch_change == 1:
        if item_key > 5:
            new_key = item_key - 5
        else:
            new_key = item_key + 7
    if pitch_change == 2:
        if item_key > 10:
            new_key = item_key - 10
        else:
            new_key = item_key + 2
    return(new_key)

def open_json():
    with open('dict.json', encoding='utf-8') as data_file:
        global db
        db = json.loads(data_file.read())

    








open_json()
hackmix()





