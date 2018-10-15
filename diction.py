# def get_stems(word):
#     count = []
#     i=1
#     while i <len(word):
        
#         count.append(word[:i])
#         i+=1
        
#     return count

    

def get_stems(word):
    return [word[:i] for i in range(1, len(word))]


def get_stems_for_word_list(wl):
    stems = []
    for word in wl:    
        stems_for_word = get_stems(word)
        stems += stems_for_word
    return set(stems)

print(get_stems("HELLO"))    