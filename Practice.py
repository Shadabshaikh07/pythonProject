# First N prime numbers
i = 1
n = int(input("Enter the number:"))
for k in range(1, n+1):
    c = 0
    for j in range(1, i+1):
        a = i % j
        if a == 0:
            c = c + 1

    if c == 2:
        print(i)
    else:
        k = k - 1

    i = i + 1

print('----------------------------------')

# Word Count
import re; import os
def count_word(file_name):
    if file_exists(file_name):
        WORD_COUNT = {}
        with open(file_name) as f:
            lines = f.read().splitlines()
            for line in lines:
                if line:
                    for word in process_text(line).split(' '):
                        if word in WORD_COUNT:
                            WORD_COUNT[word] += 1
                        else:
                            WORD_COUNT[word] = 1
        return WORD_COUNT
    else:
        print("Text file does not exist")

def process_text(input_text):
    lower_processed_text = re.sub(r"[^a-zA-Z0-9 ]", '', input_text.lower())
    return lower_processed_text.strip()

def file_exists(file_name):
    proj_folder = os.path.abspath('')
    file_path = os.path.join(proj_folder,file_name)
    return os.path.exists(file_path)

if __name__ == '__main__':
    FILE_NAME = 'wiki.txt'
    print(count_word(FILE_NAME))