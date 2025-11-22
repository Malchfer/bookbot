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

def sort_on(list):
    return list["num"]

def dict_sort(dict):
    dict_list = []

    for character in dict:
        char_dict = {}
        char_dict["char"] = character
        char_dict["num"] = dict[character]
        dict_list.append(char_dict)

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list