def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_count(text)
    print(text)
    print(count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_count(book):
    words = book.split()
    count = 0
    for word in words:
        count += 1
    return count
main()