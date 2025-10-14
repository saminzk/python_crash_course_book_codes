def make_sandwhich(*items):
    print("Summary of sandwhich")
    for item in items: 
        print(item+" is added to the sandwhich")



make_sandwhich('egg')
make_sandwhich('chicken','cheese')
make_sandwhich('chicken','vegetable', 'cheese')
