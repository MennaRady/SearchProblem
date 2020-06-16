from math import radians, sin, cos, asin, sqrt
from cities import  create_city_list
from path import FindNextFlight
from projectknowledge import create_flight_plan

all_tracks=[]
cities = create_city_list()
flight_Plan = create_flight_plan()
# the Track class saves the path taken and its FN and GN from one country to another, the final path is a list of Track objects.
class Track:
    List_of_paths =[]
    FN = 0.00
    Gn=None
    def __init__(self, path,fn,gn):
        self.List_of_paths=path
        self.FN = fn
        self.Gn=gn

# this funnction calculates the distance between 2 cities either for the g(n) or the h(n) as we are working with distance to comapre between flights.
def distance(longitude_countrie1, latitude_countrie1, longitude_countrie2, latitude_countrie2):
    longitude_countrie1, latitude_countrie1, longitude_countrie2, latitude_countrie2 = map(radians, [longitude_countrie1, latitude_countrie1, longitude_countrie2, latitude_countrie2])
    distance_For_longitude = longitude_countrie2 - longitude_countrie1
    distance_For_latitude = latitude_countrie2 - latitude_countrie1
    Area = sin(distance_For_latitude/2)**2 + cos(latitude_countrie1) * cos(latitude_countrie2) * sin(distance_For_longitude/2)**2
    circumference = 2 * asin(sqrt(Area))
    RadiusofEarth = 6371
    distance=circumference * RadiusofEarth
    return distance

# this function uses the distance function to calculate the distance between the 2 cities in the possible flights.
def GN( country1,country2):

    lon1 = get_longitude(country1)
    lon2 = get_longitude(country2)
    lat1 = get_latitude(country1)
    lat2 = get_latitude(country2)
    # G = distance(country1info, country2info)
    G=distance(lon1, lat1, lon2, lat2)
    return G

# this function calculates the F(n) of a city chosen
def FN(country1, country2,Goal,g):
    H = HN(country1, Goal)
    G = g+GN(country1, country2)
    sum = H + G
    return sum,G
# getter for the longitude of a city
def get_longitude(country):
    list = create_city_list()
    len_list = len(list)
    for i in range(len_list):
        if list[i].name == country:
            countryinfo =list[i].longitude
            return countryinfo

# getter for the latitude of a city
def get_latitude(country):
    list = create_city_list()
    len_list = len(list)
    for i in range(len_list):
        if list[i].name == country:
            countryinfo =list[i].latitude
            return countryinfo

# we are working with longitude and latitude so our heuristic function calculates the distance between the city we are currently on
# and the goal city using the distance function. it takes the 2 cities as parameters
def HN(country1, country2):
    lon1 =get_longitude(country1)
    lon2 = get_longitude(country2)
    lat1 = get_latitude(country1)
    lat2 = get_latitude(country2)
    #H = distance(country1info, country2info)
    H=distance(lon1, lat1, lon2, lat2)
    return H

# this function compares the F(n)'s of all the possible cities and chooses the smallest one as the next city to go to.
#listOfDistances is the list of calculated FNs of possible paths
def getSmallestFN(listOfDistances):
    track=listOfDistances[0]
    min = listOfDistances[0].FN
    for distance in listOfDistances:
        if distance.FN < min:
            min = distance.FN
            track=distance
    return track

# this function adds a visited city to the visited list.
def addToVisitedList(flight, Visited):
    Visited.append(flight)
    return Visited

# this function calculates the F(n) for a path/node chosen.
def calculate_path_fn(paths,goal,GN):
    list_track_of_fn = []
    for track in paths:
        fn,gn=FN(track.departure_city,track.arrival_city,goal,GN)
        track1 =Track(track,fn,gn)
        list_track_of_fn.append(track1)
    return list_track_of_fn

# this function says that if a flight is at the end of the day (24.00) time, then the next flight should be in the day after it.
def NextDay(time, day):
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if time >= 24.00:
        for d in days:
            if day == d:
                index = days.index(d)

        if index == 6:
            nextDayIndex = 0
        elif index != 6:
            nextDayIndex = index+1

        nextDay = days[nextDayIndex]
        time = "00:00"
        return nextDay, time
    return day, time

# this function takes a Track object and reverses list and returns the last flight taken to know where to go next.
def returnLastFLight(list):
    list.List_of_paths.reverse()
    return list.List_of_paths[0]

# this function merges ne paths to the previous path so we can calculate the g(n) and the F(n)'s so we can compare them
def merge_track(track_list,optimal):

    for d in track_list:
        w=[d.List_of_paths]
        optimal.List_of_paths.reverse()
        joinedlist=optimal.List_of_paths+w
        track=Track(joinedlist,d.FN,d.Gn)
        all_tracks.append(track)

# this function prints the final result, it calls printPaths function which prints each path in the list of paths taken.
def printFinal(Final_path):
    Final_path.List_of_paths.reverse()
    printPaths(Final_path.List_of_paths)

# prints each path in the list of final paths taken.
def printPaths(p):
    for i in p:
        print(i.departure_city,",",i.arrival_city ,",",i.departure_time,",",i.arrival_time,",",i.flight_number,",",i.date)

#def printFlights(flight):
 #       print(flight.departure_time , " // " , flight.arrival_time , " // " , flight.flight_number , " // " , flight.list_of_days, "\n")

# start function starts the whole program which prompts the user to enter the departure city, destination city, and the list of days.
def start():
    departure_City = input("hello Welcome to our travel agency what is your departure city:")
    for citie in cities:
        if departure_City == citie.name:
            destination = input("Where would you like to go to:")
            for citi in cities:
                if destination == citi.name:
                    List_of_days = input("When would you like to fly:")
                    print List_of_days
                    track = Track([], 0, 0)
                    Astart(departure_City, destination, 0.00, List_of_days, track)
    while True:
        departure_City=input("what is your departure city:")
        for citie in cities:
            if departure_City == citie.name:
                 destination = input("Where would you like to go to:")
                 for citi in cities:
                    if destination ==citi.name:
                        List_of_days = input("When would you like to fly:")
                        print List_of_days
                        track=Track([],0,0)
                        Astart(departure_City, destination,0.00,List_of_days,track)


# this function is for the A star algorithm
def Astart(departure_City, destination,time, List_of_days,previuos_path):

    if departure_City==destination:
        print("This is our recommended flight plan:")
        return printFinal(previuos_path) #(or print)function to print path
    paths=FindNextFlight(flight_Plan, departure_City,time, List_of_days)
    #function to filter according to days
    Fn_list=calculate_path_fn(paths,destination,previuos_path.Gn)# this should be a list of fn and path and gn
    merge_track(Fn_list,previuos_path)# funtion to fix both optimals together(add start and new path)
    optimal=getSmallestFN(all_tracks)
    all_tracks.remove(optimal)
    d=destination
    flights=returnLastFLight(optimal)
    Day,updated_time=NextDay(flights.arrival_time,flights.date)
    Astart(flights.arrival_city,d,updated_time,Day, optimal)



start()


