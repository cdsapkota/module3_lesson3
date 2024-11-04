def check_destination(our_route, their_route):
    both_fly_des = our_route.intersection(their_route)
    unique_des = our_route.difference(their_route)
    neither_des = our_route.symmetric_difference(their_route)
    print(f"The destinations that both airlines fly are: {both_fly_des}")
    print(f"The destinations unique to our airline are: {unique_des}")
    print(f"The destinaitons that neither airline share are: {neither_des}")

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
check_destination(our_routes, competitor_routes)