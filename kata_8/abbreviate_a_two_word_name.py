def abbrev_name(name):
    first, last = name.upper().split(' ')
    fn = first[0]
    ln = last[0]
    return fn +'.'+ ln