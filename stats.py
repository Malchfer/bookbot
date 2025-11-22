def count_words(input):
    word_count = len(input.split())
    return word_count

def count_characters(input):
    lower_input = input.lower()
    character_count = {}
    for i in lower_input:
        if i not in character_count:
            character_count[i] = 1
        else: 
            character_count[i] += 1
    return character_count