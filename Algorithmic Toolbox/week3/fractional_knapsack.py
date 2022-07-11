import sys


def get_optimal_value(capacity, weights, values):
    temp_dict ={}
    
    
    for i,key in enumerate(values):
      temp_dict[key] = weights[i]
    sorted_by_value = dict(sorted(temp_dict.items(), key=lambda item: item[0]/item[1], reverse = True))
    value = 0
    temp = 0
    for i,(loot,weight) in enumerate(sorted_by_value.items()):
          if float(capacity/weight*loot) > temp:
            if capacity >= weight:
              
              value += float(loot)
              capacity -= weight
            else:
              if len(temp_dict) == 1:
                return float(capacity/weight *loot)
              else:
                temp = float(capacity/weight*loot)

                if i == len(temp_dict)-1:
                  value+=float(temp)
          else:
            value+=temp
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
