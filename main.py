# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as f:
        text = " ".join(f.readlines())
    return text
    

def count_words():
    text = read_file_content("./story.txt")
    word_count = {}
    for word in text.split():
        clean_word = "".join(char for char in word if char.isalpha())
        word_count.setdefault(clean_word.lower(), 0)
        word_count[clean_word.lower()] += 1
    return word_count


print(count_words())
