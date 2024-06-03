def main():
    # Get file path for txt file to read
    file_path = 'books/frankenstein.txt'
    with open(file_path) as f:
        file_contents = f.read()
    
    # Define functions for list of words, word count, and character counts
    def words(file):
        words = file.split()
        return words

    def word_count(words):
        return len(words)

    def char_count(words):
        characters = {}
        for word in words:
            lowered_string = word.lower()
            for letter in lowered_string:
                try:
                    characters[letter] += 1
                except:
                    characters[letter] = 1
        return characters

    # Define function to convert dictionary into list of dictionaries
    def convert(dictionary):
        return [{key: value} for key, value in dictionary.items()]
    
    # Get final dictionary of all characters with counts, list of all letters, and final word count
    all_chars = char_count(words(file_contents))
    keys_list = list(all_chars.keys())
    all_chars_list = convert(all_chars)
    res = sorted(keys_list, key = lambda ele: all_chars[ele], reverse=True)
    
    final_chars = []
    for letter in res:
        if letter.isalpha():
            final_chars.append(letter)
    
    fin_word_count = word_count(words(file_contents))
    
    # Generate report of word count, and character count for all letters
    print(f'--- Begin report of {file_path} ---')
    print(f'{fin_word_count} words found in the document')
    print(' ')
    for letter in final_chars:
        print(f"The '{letter}' character was found {all_chars[letter]} times")
    print('--- End report ---')

    


main()