def check_connection(net, first, second):
    set_f = set()
    set_s = set()
    set_all = set()
    dict_f = dict()
    dict_s = dict()
    for i in net:
        one,two = i.split("-")
        if first in i:
            if one == first:
                set_f.add(two)
                dict_f[first] = set_f
            else:
                set_f.add(one)
                dict_f[first] = set_f
        if second in i:
            if one == second:
                set_s.add(two)
                dict_s[second] = set_s
            else:
                set_s.add(one)
                dict_s[second] = set_s
    check = len(dict_f[first]) + len(dict_s[second])
    set_all = dict_f[first].union(dict_s[second])
    print(set_all)
    if len(set_all) < check:
        return True
    else:
        return False
            
                
            
            
