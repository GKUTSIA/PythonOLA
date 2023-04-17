with open('task_09.txt', 'r') as file:
    contents = file.read()
    word_count = len(contents.split())
    char_count = len(contents)
    line_count = len(contents.splitlines())

print(f"Number of words: {word_count}")
print(f"Number of characters: {char_count}")
print(f"Number of lines: {line_count}")