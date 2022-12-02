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

def get_strategy_guide() -> list[list[int]]:
    strategy_guide = []

    with open("input.txt") as file:
        for current_line in file.readlines():
            strategy_guide.append(current_line.rstrip().split())

    return strategy_guide

def get_game_total_score(strategy_guide: list[list[int]]) -> int:
    total_score = 0
    # TODO
    return total_score
    

def main():
    strategy_guide = get_strategy_guide()
    print(strategy_guide)

if __name__ == "__main__":
    main()
