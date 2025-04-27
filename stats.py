def get_word_count(content):
    return len(content.split())

def get_character_appearance(content):
    character_appearances = {}

    for char in content:
        char_lower = char.lower()
        if char_lower in character_appearances:
            character_appearances[char_lower] += 1
        else: 
            character_appearances[char_lower] = 1

    return character_appearances
