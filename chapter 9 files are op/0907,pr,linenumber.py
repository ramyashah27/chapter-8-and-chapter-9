content = True
i=1
with open('log.txt') as f:
    while content:    
        content=f.readline()
    if 'flow start' in content.lower():
        print(content)
        i+=1
    
