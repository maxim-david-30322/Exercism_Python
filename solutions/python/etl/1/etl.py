def transform(legacy_data):
    new={}

    for key in legacy_data:  # returneaza key
        lista=legacy_data[key]
        for letter in lista:
            new[letter.lower()]=key   
    
    return new
