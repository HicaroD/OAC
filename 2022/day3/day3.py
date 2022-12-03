# Cada linha do input representa a lista de itens dentro da bolsa
# Um item é representado por uma letra (maiúscula ou minúscula)
#
# Como a bolsa tem dois compartimentos, a primeira metade dos itens vão
# no primeiro compartimento e a segunda metade no segundo compartimento
#
# A ideia é encontrar o item em comum na primeira metade e na segunda metade
# Com isso, eu peguei a prioridade dele e somarei ao total

# a-z tem prioridade de 1 a 26
# A-Z tem prioridade de 27 a 52

def get_rucksacks_items() -> list[str]:
    with open("input.txt") as file:
        return file.readlines()

def get_compartiments(rucksack_items: str) -> tuple[set[str], set[str]]:
    items_length = len(rucksack_items)
    compartment_separator = items_length // 2
    first_compartment = set(rucksack_items[:compartment_separator])
    second_compartment = set(rucksack_items[compartment_separator:])
    return first_compartment, second_compartment

def get_item_priority(item: str):
    return ord(item) - 96 if item.islower() else ord(item) - 38

# Part 1
def get_priority_sum(rucksacks_items: list[str]) -> int:
    priority_sum = 0

    for rucksack_item in rucksacks_items:
        first_compartment, second_compartment = get_compartiments(rucksack_item)
        common_item = first_compartment.intersection(second_compartment)

        for item in common_item:
            priority_sum += get_item_priority(item)

    return priority_sum

# Part 2
def get_priority_sum_for_group_of_three(rucksascks_items: list[str]):
    for rucksack_item in rucksascks_items:
        pass

def main():
    rucksascks_items = get_rucksacks_items()
    priority_sum = get_priority_sum(rucksascks_items)
    priority_sum_for_groups = get_priority_sum_for_group_of_three(rucksascks_items)
    print(priority_sum)
    print(priority_sum_for_groups)

if __name__ == "__main__":
    main()
