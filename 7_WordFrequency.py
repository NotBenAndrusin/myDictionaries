# read contents of file (someone.txt)
# create a dict (keys = words, value = occur)
# display the value of each word

# read the contents of the file
filename = 'sometext.txt'
infile = open(filename, 'r')
words = infile.read().replace('.', '').replace(',', '').split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word in word_count:
    print(word + ',', word_count[word])

infile.close()
