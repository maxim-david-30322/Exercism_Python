from collections import deque
handshake_actions = {
    0: "wink",
    1: "double blink",
    2: "close your eyes",
    3: "jump",
}

def commands(binary_str):
    que=[]
   
    for i,nr in enumerate(binary_str[::-1]):
        if nr=="1":
            action=handshake_actions.get(i)
            if action is not None:
                que.append(action)
    if binary_str[0]=="1":
        return que[::-1]
    else:
        return que
