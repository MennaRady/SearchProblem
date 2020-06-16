# this class defines a path object which defines the eligible flight chosen from the timetable with the eligible dates and days.
class Path:
    departure_city = None
    arrival_city = None
    departure_time = None
    arrival_time = None
    flight_number = None
    date = None
    def __init__(self, departureCity, arrivalCity, departureTime, arrivalTime, flightNumber,day):
        self.departure_city = departureCity
        self.arrival_city = arrivalCity
        self.departure_time = departureTime
        self.arrival_time = arrivalTime
        self.flight_number = flightNumber
        self.date = day


# this function finds the next paths from a certain. could be one next path/node or could be many that is why a list is returned.
# for example if from cairo we can go to 3 different cities then these cities and the information of the flights and all are added as next.
def FindNextFlight(listOfFlights,location,time,days ):
    possible_Flights=[]
    for flight in listOfFlights:
        if  flight.departure_city == location:
            Flight_data = flight.list_of_flights
            for singleflight in Flight_data:
                 if singleflight.departure_time > time:
                     flight_d=singleflight.list_of_days
                     for date in flight_d:
                        if date in days:
                            fl=Path(flight.departure_city,flight. arrival_city,singleflight.departure_time,singleflight.arrival_time,singleflight.flight_number,date)
                            possible_Flights.append(fl)
    return possible_Flights