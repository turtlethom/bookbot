def get_word_count(file_text: str) -> int:
    total_words = file_text.split()
    count = 0
    for word in total_words:
        count += 1
    return count

def get_symbol_count(file_text: str) -> dict:
    symbols = {}
    for char in file_text:
        if char.isalpha():
            key = char.lower()
            if not symbols.get(key):
                symbols[key] = 1
            else:
                symbols[key] += 1
    return symbols

def print_report(file_text: str, filename: str) -> None:
    symbols_dict = get_symbol_count(file_text)

    print(f"--- Begin report of book/{filename}.txt")
    print(f"{get_word_count(file_text)} words found in the document\n");
    for key in symbols_dict:
        print(f"The \'{key}\' was found {symbols_dict[key]} times")
    print("--- End report ---")

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print_report(file_contents, "frankenstein.txt")

main()
