# A primeira coluna é o que o oponente vai jogar e a segunda coluna é o que
# você deve jogar para vencer.
#
# A para Rock, B para Paper e C para Scissor (para o oponente) (primeira coluna)
#
# X para Rock, Y para Paper e Y para Scissor (para você) (segunda coluna)
#
# A pessoa que tiver mais pontos, vence. O seu score total é a soma de todos os
# pontos que você obteve a cada round. O score de cada round é dito pelo formato
# que você escolheu (1 para Rock, 2 para Paper e 3 para Scissor) somado ao resultado
# da rodada (0 se perdeu, 3 se foi empate e 6 se venceu)

RIGHT_MOVES = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}

SCORE_PER_SHAPE = {
     "X": 1,
     "Y": 2,
     "Z": 3,
}

DRAW_SCENARIOS = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

def get_strategy_guide() -> list[list[str]]:
    strategy_guide = []

    with open("input.txt") as file:
        for current_line in file.readlines():
            strategy_guide.append(current_line.rstrip().split())

    return strategy_guide

def is_right_move(oponent_choice: str, my_choice: str):
    return RIGHT_MOVES[oponent_choice] == my_choice

def is_draw_move(oponent_choice: str, my_choice: str):
    return DRAW_SCENARIOS[oponent_choice] == my_choice

def get_game_total_score(strategy_guide: list[list[str]]) -> int:
    total_score = 0

    for (oponent_choice, my_choice) in strategy_guide:
        if is_right_move(oponent_choice, my_choice):
            total_score += SCORE_PER_SHAPE[my_choice] + 6
        elif is_draw_move(oponent_choice, my_choice):
            total_score += SCORE_PER_SHAPE[my_choice] + 3
        else:
            total_score += SCORE_PER_SHAPE[my_choice]

    return total_score

def main():
    strategy_guide = get_strategy_guide()
    total_score = get_game_total_score(strategy_guide)
    print(total_score)

if __name__ == "__main__":
    main()
