# python3
import sys


def compute_min_refills(distance, tank, stops):
    if distance < tank:
      return 0
    last_stop = 0
    total_stops = 0
    gas = tank
    curr_stop = 0
    stops_distance = stops
    stops_distance.append(distance)
    while gas < distance: 
      if curr_stop >= len(stops) or stops[curr_stop] > gas:
        return - 1
      while curr_stop < len(stops)-1 and stops[curr_stop+1] <= gas:
        curr_stop += 1
      total_stops += 1
      gas = stops[curr_stop] + tank
      curr_stop += 1
      
    return total_stops
      
      
    return total_stops

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
