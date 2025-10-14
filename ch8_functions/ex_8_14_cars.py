def make_car(brand,model, **features):
    car = {}
    car['brand'] = brand
    car['model'] = model
    for key,value in features.items():
        car[key] = value
    return car


car = make_car('Subaru','Outback',tow_package = True)

print(car)