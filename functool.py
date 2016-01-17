import functools

def string_cmp(x, y):
    if(x.lower() < y.lower()):
        return -1
    if(x.lower() > y.lower()):
        return 1
    return 0
    

sorted_ignore_case = functools.partial(sorted, cmp = string_cmp)

print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])