def recite(start, take=1):

    number_words = {
        10: "Ten",
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One",
        0: "no",
    }

    # first=f"{number_words[start]} green bottles hanging on the wall,"
    # second=f"And if one green bottle should accidentally fall,"
    # third=f"There'll be {number_words[start - 1].lower()} green bottles hanging on the wall."
    
    # first2=f"{number_words[start]} green bottles hanging on the wall,"
    # second2=f"And if one green bottle should accidentally fall,"
    # third2=f"There'll be {number_words[start - 1].lower()} green bottle hanging on the wall."

    # first1=f"{number_words[start]} green bottle hanging on the wall,"
    # second1=f"And if one green bottle should accidentally fall,"
    # third1=f"There'll be {number_words[start - 1].lower()} green bottles hanging on the wall."
        
    # text = (
    #     f"{number_words[start]} green bottles hanging on the wall,\n"
    #     f"{number_words[start]} green bottles hanging on the wall,\n"
    #     f"And if one green bottle should accidentally fall,\n"
    #     f"There'll be {number_words[start - 1]} green bottles hanging on the wall."
    # )
    text=[]
    while take>0:
        first=f"{number_words[start]} green bottles hanging on the wall,"
        second=f"And if one green bottle should accidentally fall,"
        third=f"There'll be {number_words[start - 1].lower()} green bottles hanging on the wall."
        
        first2=f"{number_words[start]} green bottles hanging on the wall,"
        second2=f"And if one green bottle should accidentally fall,"
        third2=f"There'll be {number_words[start - 1].lower()} green bottle hanging on the wall."

        first1=f"{number_words[start]} green bottle hanging on the wall,"
        second1=f"And if one green bottle should accidentally fall,"
        third1=f"There'll be {number_words[start - 1].lower()} green bottles hanging on the wall."
            
        if start == 2 :
            third=third2    
        if start == 1:
            first=first1

        text.extend([
            first,
            first,
            second,
            third,
        ])
        if take > 1:
            text.append("")

        start-=1
        take-=1
    return text
    pass
