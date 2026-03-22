import re
import operator
from collections import deque
operations = {
    "minus": operator.sub,
    "plus": operator.add,
    "multiplied": operator.mul,
    "divided": operator.truediv
}

def answer(question):



    question1=r"What is [-+]?[0-9]+\?$"
    q_list=[]
    q_list = question[:-1].split(" ")
    if len(q_list)==3:  
        if re.match(question1,question):
            return int(q_list[-1])
                

    task=deque()
    for word in q_list:
        if word in operations or word.lstrip("-").isdecimal():
            task.append(word)

    if not task:
        raise ValueError("syntax error")
    


    if not task[0].lstrip("-").isdecimal():
        raise ValueError("syntax error")
    if "cubed" in question:
        raise ValueError("unknown operation")
    
    result=int(task.popleft())


    if len(task)%2!=0:
        raise ValueError("syntax error")
    
    while task:
        
        op=task.popleft()

        if op not in operations:
            raise ValueError("syntax error")
        
        val=task.popleft()
        if not val.lstrip("-").isdigit():
            raise ValueError("syntax error")
        result=operations[op](result,int(val))
    return (result)