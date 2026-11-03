def field(iter, *args):
    assert len(args) > 0
    if len(args) == 1:
        for elem in iter:
            if elem.get(args[0]) is not None:
                yield elem[args[0]]
    else:
        for elem in iter:
            SelectDict = dict()
            for arg in args:
                if elem.get(arg) is not None:
                    SelectDict[arg] = elem[arg]
            if len(SelectDict) > 0:
                yield str(SelectDict)
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]
print(', '.join(list(field(goods, 'title'))))
print(', '.join(list(field(goods, 'title', 'price'))))
