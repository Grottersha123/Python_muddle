def word_search(q, s):
    a = []
    for i in s:
        if q.lower() in i.lower():
            a.append(i)
        
    if a != []:
        return a
    return None
