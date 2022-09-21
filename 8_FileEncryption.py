codes = {
    'A' : '%',
    'a' : '9',
    'B' : '@',
    'b' : '#',
    'C' : '-',
    'c' : '{',
    'D' : ']',
    'd' : '}',
    'E' : '[',
    'e' : '\\',
    'F' : '/',
    'f' : '?',
    'G' : ':',
    'g' : '<',
    'H' : ';',
    'h' : '>',
    'I' : '\'',
    'i' : '"',
    'J' : '=',
    'j' : '1',
    'K' : '_',
    'k' : '!',
    'L' : '$',
    'l' : '^',
    'M' : '*',
    'm' : '|',
    'N' : '°',
    'n' : '3',
    'O' : '5',
    'o' : '6',
    'P' : '(',
    'p' : '7',
    'Q' : ')',
    'q' : '8',
    'R' : '2',
    'r' : '4',
    'S' : '7',
    's' : '+',
    'T' : '&',
    't' : '`',
    'U' : '~',
    'u' : '³',
    'V' : '©',
    'v' : '¡',
    'W' : '¥',
    'w' : 'Ø',
    'X' : '‡',
    'x' : '…',
    'Y' : '¿',
    'y' : 'ô',
    'Z' : '±',
    'z' : '™',
    ' ' : ' '
}

filename = 'info_security.txt'
infile = open(filename, 'r')
words = infile.read()
infile.close()

output_string = ""
for letter in words:

    # checks to see if the current letter is in codes, that is,
    #   ignores all punctuation and only encodes letters (a-z or A-Z)
    #   that are in the codes dictionary
    if letter in codes:
        letter = codes[letter]
    output_string += letter
    
outfile = open('encrypted.txt', 'w')
outfile.write(output_string)
outfile.close()