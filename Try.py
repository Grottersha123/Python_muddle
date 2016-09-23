a = 'sdf'
def lol(a):
    try:
        int(a)
        return True
    except:
        if float(a):
            return True
        return False
