def my_file(f_name):# f_name is the name of the file
    with open(f_name, 'r') as file:
        return file.read()
text = my_file('sample.txt')
print(text[:100])  



def line_count(text):
    return len(text.split('\n'))
number_lines = line_count(text)
print(f" Total number of line are: {number_lines}")



def word_count(text):
    return len(text.split())
word = word_count(text)
print(f"Total number of words are: {word}")



from collections import Counter
def common_words(text):
    words = text.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]
common_word, count = common_words(text)
print(f"Most common word: '{common_word}' (appears {count} times)")



def average_length_of_word(text):
    words = text.split()
    all_length = sum(len(word) for word in words)
    return all_length / len(words)
avg_length = average_length_of_word(text)
print(f"Average word length: {avg_length:.2f} characters")



def analyze_text(f_name):
    text = my_file(f_name)
    number_lines = line_count(text)
    word = word_count(text)
    common_word, count = common_words(text)
    avg_length = average_length_of_word(text)
    
    print(f"File: {f_name}")
    print(f"total lines: {number_lines}")
    print(f"total words: {word}")
    print(f"repeated word: '{common_word}' (appears {count} times)")
    print(f"Avg length of words: {avg_length:.2f} characters")


analyze_text('sample.txt')
