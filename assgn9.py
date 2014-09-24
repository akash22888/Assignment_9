#!/usr/bin/python

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
    return dictionary        


def main():
    dictionary = create_dict("mood_dict.txt")
    print dictionary.items()

if __name__ == '__main__':
    main()
