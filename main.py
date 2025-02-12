def main():
    with open("books/frankenstein.txt") as f:   # opens specified path and reads the contents of the .txt file
        file_contents = f.read()
    # print(file_contents)    
    print(count_words(file_contents))
    

def count_words(file_contents):
    count = 0
    words = file_contents.split()   # splits file_contents into individual words
    for word in words:  # iterates through each word and adds 1 to total count 
        count += 1

    return count

main()

