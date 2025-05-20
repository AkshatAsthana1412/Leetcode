from collections import deque

def word_ladder(begin_word, end_word, word_list):
    word_set = set(word_list)
    if end_word not in word_set:
        return 0  # early exit if end word is unreachable
    
    queue = deque([(begin_word, 1)])
    word_len = len(begin_word)
    
    while queue:
        word, steps = queue.popleft()
        if word == end_word:
            return steps
        
        for i in range(word_len):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in word_set:
                    queue.append((next_word, steps + 1))
                    word_set.remove(next_word)  # mark as visited

    return 0

print(word_ladder('hit', 'cog', ['hot', 'dog', 'dot', 'log', 'lot', 'cog']))