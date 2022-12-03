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

def get_priority_sum(rucksascks_items: list[str]) -> int:
    priority_sum = 0

    for rucksack_item in rucksascks_items:
        first_compartment, second_compartment = get_compartiments(rucksack_item)
        common_item = first_compartment.intersection(second_compartment)
        for item in common_item:
            if item.islower():
                priority_sum += ord(item) - 96
            else:
                priority_sum += ord(item) - 38

    return priority_sum

def main():
    rucksascks_items = get_rucksacks_items()
    priority_sum = get_priority_sum(rucksascks_items)
    print(priority_sum)

if __name__ == "__main__":
    main()
