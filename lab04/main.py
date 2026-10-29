import sys
from stats import read_valid, average_by_city, warmest_city


def main():

    lines = [line.rstrip("\n") for line in sys.stdin]


    records = read_valid(lines)

  
    avg_by_city = average_by_city(records)
    
    warmest = warmest_city(records)

    
    for city in sorted(avg_by_city.keys()):
        print(f"{city}: {avg_by_city[city]}")

   
    print(f"Warmest: {warmest}")


if __name__ == "__main__":
    main()

