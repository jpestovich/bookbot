def count_words(book):
    words = book.split()
    word_count = len(words)
    return word_count

def main():
    book = 'books/frankenstein.txt'
    with open(book) as f:
        file_contents = f.read()
    print(f"book text:`n {file_contents}")
    wc = count_words(file_contents)
    print("-----------------------------------")
    print(f"total number of words in book {wc}")

main()
