

log = ["AND","OR","XOR"]
def Le(seq,ol):
    l = seq[0]
    for i in range(1,len(seq)):
        if "AND" == ol:
            l = l and seq[i]
        if "OR" == ol:
            l = l or seq[i]
            print(seq[i])
        if "XOR" == ol:
            l = l ^ seq[i]
    return l
    


ani = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
elem = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']


st = "1234567890"
def get_number_from_string(string):
    s = string
    l = ""
    for i in s:
        if i in st:
            l+= i
    print(l)
    return int(l)



