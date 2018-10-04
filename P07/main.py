#def flatten(x):
    #x = str(x).replace("[","")
    #x = x.replace("]","")
    #x = x.replace(" ","")
    #x = x.split(", ")
    #x = [int(s) for s in x]
    
def flatten(data):
    return [element
            for item in data
            for element in (flatten(item) if hasattr(item, '__iter__') else [item])]