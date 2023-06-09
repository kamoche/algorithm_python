def test(s, k):
    lookup = []
    res = []
    print(f'len = {len(s)}')

    for i, v in enumerate(s):
        if k == v:
            lookup.append(i)
    
    print(lookup[-1])
    for x in range(len(s)):
        value = []
        for w in lookup:
            value.append(abs(w - x))
        
        res.append(min(value))
    
    print(f'result {res}')
       
    return lookup


print(test('mkteneetkybe', 'e'))




