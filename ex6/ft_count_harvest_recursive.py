def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    ft_recursive(days)
    print("Harvest time!")


def ft_recursive(day):
    if day < 1:
        return
    ft_recursive(day - 1)
    print(f"Day {day}")
