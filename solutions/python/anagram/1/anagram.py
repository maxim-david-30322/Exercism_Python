def find_anagrams(word, candidates):

    word_letter={}
    match=[]
    for letter in word.lower():
        word_letter[letter]=word_letter.get(letter,0)+1

    for candidate in candidates:
        candidate_letter={}
        if candidate.lower()==word.lower():
            continue
        for letter in candidate.lower():
            candidate_letter[letter]=candidate_letter.get(letter,0)+1
        if word_letter==candidate_letter:
            match.append(candidate)

    return match
    pass