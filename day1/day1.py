def get_top_three_elfis(calories: list[int]) -> list[int]:
    top_three_elfis = []

    # TODO: this code is too repetitive
    greatest_calorie = max(calories)
    top_three_elfis.append(greatest_calorie)
    calories.remove(greatest_calorie)

    greatest_calorie = max(calories)
    top_three_elfis.append(greatest_calorie)
    calories.remove(greatest_calorie)

    greatest_calorie = max(calories)
    top_three_elfis.append(greatest_calorie)
    calories.remove(greatest_calorie)

    return top_three_elfis

def get_elf_calories() -> list[int]:
    calories = []

    with open("input.txt") as file:
        calorie_sum = 0
        for current_line in file.readlines():
            if not current_line.isspace():
                current_calorie = int(current_line.strip())
                calorie_sum += current_calorie
            else:
                calories.append(calorie_sum)
                calorie_sum = 0

    return calories

def main():
    calories = get_elf_calories()
    print(max(calories)) # Solution to the first part of the problem
    print(sum(get_top_three_elfis(calories))) # Solution to the second part of the problem

if __name__ == "__main__":
    main()
