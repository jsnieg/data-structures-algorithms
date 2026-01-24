states_needed: set = set(['mt', 'wa', 'or', 'id', 'nv', 'ut'])
stations = {}
stations["kone"] = set(['id', 'nv', 'ut'])
stations["ktwo"] = set(['wa', 'id', 'mt'])
stations["kthree"] = set(['or', 'nnv', 'ca'])
stations["kfour"] = set(['nv', 'ut'])
stations["kfive"] = set(['ca', 'az'])
final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states # find items that show up in both sets (intersection) [set of uncovered states that this station covers]
        if len(covered) > len(states_covered): # check whether this station covers more states than current best_station
            best_station = station # ... if so, new best station it is
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)
print(final_stations)