# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as readfile:
        filename = readfile.read()
    return filename
read_file_content("./story.txt")


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    use_text = text.split()
    
    count = {}
    for i in use_text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
print(count_words())

    #return {"as": 10, "would": 20}