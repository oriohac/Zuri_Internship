# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}







from os import name


def read_file_content(filename):
    # [assignment] Add your code here 
    with open('./story.txt') as f:
         name = f.read()
    return name
print(read_file_content(name))

# def count_words():
#     text = read_file_content(name)
#     # [assignment] Add your code here
#     d = dict()
#     for line in text:
#         line = line.strip()
#         words = line.split(" ")
#         for word in words:
#             if word in d:
#                 d[word] = d[word] + 1
#             else:
#                 d[word] = 1
#     for key in list(d.keys()):
#      #return {"as": 10, "would": 20}
#       print(key,':',d[key])
# count_words()