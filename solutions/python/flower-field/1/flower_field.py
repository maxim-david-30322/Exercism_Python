def annotate(garden):
    # --- VALIDATION GUARD ---
    if not garden:
        return []
    
    row_length = len(garden[0])
    for row in garden:
        # Check if all rows are the same length
        if len(row) != row_length:
            raise ValueError("The board is invalid with current input.")
        # Check for invalid characters (anything not a space or a star)
        for char in row:
            if char not in " *":
                raise ValueError("The board is invalid with current input.")

    # --- YOUR ORIGINAL STRUCTURE ---
    index = 0
    while index < len(garden):
        # --- FIRST ROW ---
        if index == 0:
            mid = garden[0]
            bottom = garden[1] if len(garden) > 1 else ""
            new_row = []
            for i, space in enumerate(mid):
                near = 0
                if space == "*":
                    new_row.append("*")
                else:
                    if i > 0: near += mid[i-1].count("*")
                    if i < len(mid) - 1: near += mid[i+1].count("*")
                    if bottom:
                        near += bottom[i].count("*")
                        if i > 0: near += bottom[i-1].count("*")
                        if i < len(bottom) - 1: near += bottom[i+1].count("*")
                    new_row.append(str(near) if near > 0 else " ")
            garden[index] = "".join(new_row)
            index += 1

        # --- LAST ROW ---
        elif index == len(garden) - 1:
            mid = garden[-1]
            top = garden[-2]
            new_row = []
            for i, space in enumerate(mid):
                near = 0
                if space == "*":
                    new_row.append("*")
                else:
                    if i > 0: near += mid[i-1].count("*")
                    if i < len(mid) - 1: near += mid[i+1].count("*")
                    near += top[i].count("*")
                    if i > 0: near += top[i-1].count("*")
                    if i < len(top) - 1: near += top[i+1].count("*")
                    new_row.append(str(near) if near > 0 else " ")
            garden[index] = "".join(new_row)
            index += 1

        # --- MIDDLE ROWS ---
        else:
            top = garden[index - 1]
            mid = garden[index]
            bottom = garden[index + 1]
            new_row = []
            for i, space in enumerate(mid):
                near = 0
                if space == "*":
                    new_row.append("*")
                else:
                    for row_ref in [top, mid, bottom]:
                        for offset in [-1, 0, 1]:
                            col_idx = i + offset
                            if row_ref is mid and offset == 0: continue
                            if 0 <= col_idx < len(row_ref):
                                near += row_ref[col_idx].count("*")
                    new_row.append(str(near) if near > 0 else " ")
            garden[index] = "".join(new_row)
            index += 1

    return garden