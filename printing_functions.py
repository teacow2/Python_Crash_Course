def car_model(manu, model, **car_info):
	car = {}
	car['manufacturer'] = manu
	car['model'] = model
	for key, value in car_info.items():
		car[key] = value
	return car