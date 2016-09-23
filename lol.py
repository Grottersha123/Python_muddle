def recur(network, f, l, path=[]):
    path_t = path[:] # копируем путь, чтобы больше ходить в те которые ходили
    if f == l:
        return True
    else:
        path_t.append(f) 
        
        for j in network[f]:
            if j not in path:
                if recur(network, j, l, path_t):
                    return True
        return False


def check_connection(network, first, second):
    net = network[:]
    network = dict()

    for i in net:
        s = i.split('-')
        if s[0] not in network.keys():
            network[s[0]] = set()
        if s[1] not in network.keys():
            network[s[1]] = set()
        network[s[0]].add(s[1])
        network[s[1]].add(s[0])
    return recur(network, first, second)
