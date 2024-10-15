def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_count(text)
    character_count = count_characters(text)
    char_sorted = sorted_list(character_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    print()
    
    for item in char_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_count(book):
    words = book.split()
    return len(words)

def count_characters(book):
    book = book.lower()
    character_count = {}

    for char in book:
        # If the character is already in the dictionary, increment its count
        # If it is not, add it to the dictionary with a count of 1
        character_count[char] = character_count.get(char, 0) + 1
    return character_count

def sort_on(d):
    return d["num"]

def sorted_list(num_chars):
    sorted =[]
    for char in num_chars:
        sorted.append({"char": char, "num": num_chars[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

main()