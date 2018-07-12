def main():
    get_all_jeeps()
    get_first_model_each_manufacturer()
    get_all_matching_models()
    sort_car_models()


cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """return a comma separated string of jeep models (original order)"""
    print("----")
    print("All jeeps")
    print("----")
    jeep = cars.get('Jeep', None)
    print(jeep)


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    print("----")
    print("First model of each manufacturer")
    print("----")
    for values in cars.values():
        print(values[0])


def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    print("----")
    print("All models containing 'trail'")
    print("----")


def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    print("----")
    print("Sorted car models")
    print("----")
    sorted_cars = [(k, v) for k, v in cars.items()]
    print(sorted_cars)


if __name__ == '__main__':
    main()
