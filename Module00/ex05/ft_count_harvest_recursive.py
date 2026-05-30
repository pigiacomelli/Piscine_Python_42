def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))

    def run_day(start):
        if start > day:
            print("Harvest time!")
            return
        else:
            print(f"Day {start}")
            run_day(start + 1)
    run_day(1)
