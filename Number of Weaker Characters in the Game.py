def NumberOfWeakCharacters(properties):
    properties.sort(key=lambda x:(-x[0],x[1]))
    print(properties)
    max_defense=0
    weak_count=0

    for a,d in properties:
        if d<max_defense:
            weak_count+=1
        else:
            max_defense=d
    return weak_count

properties=[[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]
print(NumberOfWeakCharacters(properties))
