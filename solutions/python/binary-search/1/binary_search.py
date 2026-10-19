def find(search_list, value):

    search_list.sort()

    lenght=len(search_list)
    mid=lenght//2
    position=0
    while len(search_list) > 0:
        lenght=len(search_list)
        mid=lenght//2
        
        if value==search_list[mid]:
            return position+mid
        if value>search_list[mid]:
                position+=mid+1
                search_list=search_list[mid+1:]
        else:
            search_list=search_list[:mid]

    # if position!=0:
    #      return position+mid       
    raise ValueError("value not in array")
    

    pass
