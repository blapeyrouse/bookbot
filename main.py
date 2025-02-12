def main():
    with open("books/frankenstein.txt") as f:   # opens specified path and reads the contents of the .txt file
        file_contents = f.read()
    # print(file_contents)    
    print(count_words(file_contents))    # prints word count in main
    print(count_characters(file_contents))    # prints dictionary of characters, including spaces and symbols, and the number of times it appears
    print(make_list_of_dicts(file_contents))

def count_words(file_contents):    # function to count words
    count = 0
    words = file_contents.split()   # splits file_contents into a list of individual words
    for word in words:  # iterates through each word and adds 1 to total count 
        count += 1

    return count


def count_characters(file_contents):    # function to count total number of characters and return them as a dictionary 
    character_counts = {} 
    little_words = file_contents.lower()    # lowers the case of the file_contents string
    for character in little_words:    # moves through each character
        if character not in character_counts:    # if the character does not exist as a key in the dictionary, add it and set the value to 1
            character_counts[character] = 1
        else:
            character_counts[character] += 1    # increment the value of the key by 1 for every character we've already seen

    return character_counts


# def sort_on(character_counts):
    return character_counts[character]


def make_list_of_dicts(file_contents):
    letters = []
    character_counts = count_characters(file_contents)
    for k in count_characters(file_contents):
        if k.isalpha():
            dicts_for_letters = {}
            dicts_for_letters[k] = character_counts[k]
            letters.append(dicts_for_letters)
    print("Heres LETTERS")
    print(letters)
    
    return letters



    '''
def make_report(file_contents):
    print("First list print")
    print(letters)
    letters.sort(reverse=True)
    print("Should be sorted")
    print(letters)

    return letters

    '''



main()
