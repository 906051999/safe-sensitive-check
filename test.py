import random
from faker import Faker

# Step 1: Read words from words.txt
with open('sensitive_data/text/words.txt', 'r', encoding='utf-8') as file:
    words = file.read().splitlines()

fake = Faker('zh_CN')  # Create a Faker instance for Chinese


def insert_word(sentence, words):
    word = random.choice(words)  # Choose a random word from the list
    sentence_list = sentence.split()  # Split the sentence into words
    position = random.randint(0, len(sentence_list))  # Choose a random position
    sentence_list.insert(position, word)  # Insert the word
    return ' '.join(sentence_list)  # Join the words back into a sentence


sentences = []  # Create a list to store the sentences

for _ in range(50):  # Generate 50 sentences
    sentence = fake.sentence()
    sentence = insert_word(sentence, words)
    sentences.append(sentence)  # Store the sentence in the list

# Generate a filename with the current timestamp
filename = 'test.txt'

# Open the file in write mode
with open('input/' + filename, 'w', encoding='utf-8') as file:
    file.write('\n'.join(sentences))  # Join all sentences into a single string
