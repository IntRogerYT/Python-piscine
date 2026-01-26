def ft_print_days_recursive(n, current):
    if current > n:
        print("Harvest time!")
        return
    print(f"Day {current}")
    ft_print_days_recursive(n, current + 1)


def ft_count_harvest_recursive():
    days_remaining = int(input("Days until harvest: "))

    ft_print_days_recursive(days_remaining, 1)
