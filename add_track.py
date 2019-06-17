import json



def add_entry():

    title = str(input("Enter title "))
    bpm = int(input("Enter bpm "))
    key = int(input("Enter key "))
    new_entry = f',\'{title}\':[{bpm},{key}]}}'


    infile = open("dict.json","r")
    contents = infile.read() # reads entire file into a single string
    json_string = str(json.loads(contents))

    

    json_string = json_string[:-1] + str(new_entry)
    outfile = open("dict.json", "w")
    json.dump(json_string,outfile)


    print(json_string)

    


add_entry()