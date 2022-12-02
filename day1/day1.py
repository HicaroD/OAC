def main():
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


    print(max(calories))

if __name__ == "__main__":
    main()
