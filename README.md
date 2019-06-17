# reinventing the camelot wheel

a python script that reads the bpm and root key from tracks in a json file and then suggests matches that could be [mixed harmonically](https://en.wikipedia.org/wiki/Harmonic_mixing) at a given bpm and root key

root keys expressed as numbers between 1 and 12: 'A': 8, 'A#': 3, 'B': 10,'C': 5,'C#': 12,'D': 7,'D#': 2,'E': 9,'F': 4,'F#': 11,'G': 6,'G#': 1

new entries can be added to json file with a separate script

## Prerequisites



* [Python 3.7](https://www.python.org/downloads/)



## How to run the scripts

In a terminal or elevated cmd prompt, ```cd``` to the directory where the script is located and run the following command


```bash
python hackmix2.py
```

```bash
python add_track.py
```

