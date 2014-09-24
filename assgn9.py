#!/usr/bin/python

import re

# create a dictionary from the file "filename"
def create_dict(filename):
    f = open(filename, mode='rU')
    lst = []
    for line in f:
        lst.append(line)
    f.close()
    i = 0
    dictionary = {}
    emotions = []
    for string in lst:
        words = string.split()
        if len(words) < 1: continue
        if i == 0:
            for word in words:
                emotions.append(word)
        else:
            j = 0
            for word in words:
                dictionary[word] = emotions[j]
                j+=1
        i+=1
    if ':P' in dictionary.keys():
        dictionary[':p']=dictionary[':P']
    dictionary[';);)']='Crook'
    return (emotions, dictionary)


def read_file(dict_file,content_file):
    total = 0
    (moods, dictionary) = create_dict(dict_file)
    f = open(content_file, mode='rU')
    dict2 = {}  # Dictionary to keep track of users' mood
    mood_count={}   # keep track of number of times a mood occurred
    for mood in moods:  # Initialize a dictionary to keep count of each mood
        mood_count[mood]=0
    for line in f:
        user = line[0]
        #print user, (user in dict2.keys())
        if not(user in dict2.keys()):
            dict2[user]={}
            for mm in moods:
                dict2[user][mm]=0
        found = re.findall(r'[\s\.](:[\)\(PpD]|:\-[o/]|:\'\(|B\-\)|x\-\(|;\);\)|;\)|O_O|=_=|>_<)',line);
        for entry in found:
            mood = dictionary[entry]
            dict2[user][mood] = dict2[user][mood]+1
            mood_count[mood]+=1
            total += 1
    f.close()
    f1 = open("output.txt",'w')
#    print mood_count.items()
    for entry in dict2.keys():
        res = sorted(dict2[entry],key=dict2[entry].get,reverse=True) # If two moods have equal max count, we choose one randomly
        f1.write(entry+" : "+res[0]+"\n")
    f1.write("\n"+"-"*20+"\n")
    for entry in mood_count:
        f1.write(entry+" : "+repr(mood_count[entry]/float(total)*100)+" %\n")
#        print dict2[entry]
    f1.close()



def main():
    read_file("mood_dict.txt","content.txt")
#    (moods, dictionary) = create_dict("mood_dict.txt")
#    print dictionary.items()
#    print moods

if __name__ == '__main__':
    main()
