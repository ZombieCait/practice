def dispatch_dict(operator, x, y):
    dict_val =  {
        'add': x + y,
        'sub': x - y,
        'mul': x * y,
        'div': x / y,
    }
    return dict_val.get(operator, 'None')

print(dispatch_dict('unknown', 2, 8))
print(dispatch_dict('mul', 2, 8))