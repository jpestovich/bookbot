def sort_on(dict):
    return dict["num"]
def count_words(book):
    words = book.split()
    word_count = len(words)
    return word_count

def count_characters(file_contents):
    characters = {
            }
    for character in file_contents:
        character = character.lower()
        characters[character] = characters.get(character, 0) + 1
    print("------------------------")
    print("Character counts below")
    print(characters)

def count_letters(file_contents):
    letters = {}
    for character in file_contents:
        if(character.isalpha()):
            letter = character.lower()
            letters[letter] = letters.get(letter, 0) + 1
    print("------------------------")
    print("Letter counts below")
    letter_list = [{"letter": k, "num": v} for k, v in letters.items()]
    letter_list.sort(reverse=True, key=sort_on)
    for entry in letter_list:
        print(f"The '{entry['letter']}' character was found {entry['num']} times")
    
def main():
    book = 'books/frankenstein.txt'
    with open(book) as f:
        file_contents = f.read()
    print(f"book text:`n {file_contents}")
    wc = count_words(file_contents)
    print("-----------------------------------")
    print(f"total number of words in book {wc}")
    print("-----------------------------------")
    count_characters(file_contents)
    count_letters(file_contents)

main()
