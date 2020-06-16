# this class defines the cities and their info which are used in the knowledge base
class Cities:
    name=None
    longitude=None
    latitude=None

    def __init__(self,nameOfCity,LatitudeOfCity,logitudeOfCity,):
        self.name=nameOfCity
        self.longitude=logitudeOfCity
        self.latitude=LatitudeOfCity

# this function creates Cities objects and adds them to a list so we can use them in the knowledge base
def create_city_list():

    city1 = Cities("Alexandria",31.2,29.95)
    city2 = Cities("Aswan", 24.0875,32.8989)
    city3 = Cities("Cairo", 30.05,31.25)
    city4 = Cities("Chicago",41.8373,-87.6862)
    city5 = Cities("Edinburgh",55.9483,-3.2191)
    city6 = Cities("Liverpool",53.416,-2.918)
    city7 = Cities("London",51.5,-0.1167)
    city8 = Cities("Lyon",45.77,4.83)
    city9 = Cities("Manchester",53.5004,-2.248)
    city10 = Cities("Miami",25.7839,-80.2102)
    city11 = Cities("Milan",45.47,9.205)
    city12 = Cities("New York",40.6943,-73.9249)

    city13 = Cities("Nice",43.715,7.265)
    city14 = Cities("Paris",48.8667,2.3333)
    city15 = Cities("Port Said", 31.26,32.29)
    city16 = Cities("Rome",41.896,12.4833)
    city17 = Cities("San Francisco",37.7562,-122.443)
    city18 = Cities("Shanghai",31.2165,121.4365)
    city19 = Cities("Tokyo",35.685,139.7514)
    city20 = Cities("Venice",45.4387,12.335)

    list_of_cities=[]
    list_of_cities.append(city1)
    list_of_cities.append(city2)
    list_of_cities.append(city3)
    list_of_cities.append(city4)
    list_of_cities.append(city5)
    list_of_cities.append(city6)
    list_of_cities.append(city7)
    list_of_cities.append(city8)
    list_of_cities.append(city9)
    list_of_cities.append(city10)
    list_of_cities.append(city11)
    list_of_cities.append(city12)
    list_of_cities.append(city13)
    list_of_cities.append(city14)
    list_of_cities.append(city15)
    list_of_cities.append(city16)
    list_of_cities.append(city17)
    list_of_cities.append(city18)
    list_of_cities.append(city19)
    list_of_cities.append(city20)
    return list_of_cities






