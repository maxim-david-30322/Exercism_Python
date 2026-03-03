def translate(text):

    vouls=('a','e','i','o',"u")
    rule1=('xr','yt')
    cons=enumerate("bcdfghjklmnpqrstvwxyz")
    #rule 1 


    propozitie=text.split()
    final=[]
    for text in propozitie:
            
        while len(final) is not 3:
        
            cons=""
            key=''
            keyy=0
            keyqu=0
            keyq=""
            index_qu=0
            flag=0



            if text.startswith(rule1) or text.startswith(vouls) :
                new=text+'ay'
                flag=1
                final.append(new)
                break

            

                #rule 3 or 4 
            for j,rule34 in enumerate(text):
                if rule34 is "y" and keyy is 0:
                    keyy=j
                if rule34 is "q" or keyq is "q" and keyqu is 0:
                    keyq="q"
                    if rule34 is "u":
                        keyqu=j
                
            if keyqu>keyy:
                
                #rule 3


                if "qu" in text and not text.startswith(vouls):
                    for i,letter in enumerate(text):
                        if letter not in vouls:
                            cons=cons+letter
                            if letter is "q" or key is "q":
                                key="q"
                            else:
                                key=""
                                if letter is  "u" and key is "q":
                                    break

                                    
                        else:
                            break
                    if cons is 'q': #incepe cu qu
                        cons=""
                        replace="qu"
                        new=text.replace(replace,"")+replace+"ay"
                        flag=1
                        final.append(new)
                        break
                    
                    if "q" in cons:
                        replace=cons+"u"
                        new=text.replace(replace,"")+replace+"ay"
                        flag=1
                        final.append(new)
                        break

                    if i<text.index("q"):
                        replace=cons
                        new=text.replace(replace,"")+replace+"ay"
                        flag=1
                        final.append(new)
                        break
                    
                

            if keyqu<keyy:
                #rule 4
                if 'y' in text and not text.startswith(vouls):
                    for i,letter in enumerate(text):
                        if letter not in vouls and letter is not "y":
                            cons=cons+letter
                            if letter is "y":
                                break

                                    
                        else:
                            break
                    if cons is 'y':
                        cons=""
                    # if cons.endswith("y"):
                    #     cons.pop(-1)
                    replace=cons
                    new=text.replace(replace,"")+cons+"ay"  
                    flag=1  
                    final.append(new)
                    break


                        

            #rule 2
            if flag is 0:
                for i,letter in enumerate(text):
                    if letter not in vouls:
                        cons=cons+letter
                    else:
                        break
                
                new=text.replace(cons,"")+cons+"ay"
                final.append(new)
                break

    return ' '.join(final)





    pass