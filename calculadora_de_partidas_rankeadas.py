
wins = int(input("Digite seu número de vitórias em partidas rankeadas: "))
loses = int(input("Digite seu número de derrotas em partidas rankeadas: "))

def calc_match_summary(wins, loses):
    ranked_balance = wins - loses
    return ranked_balance

def calc_player_ranking(ranked_balance):
    
    if ranked_balance <= 10:
        print("O ranking do jogador é Ferro")
    elif ranked_balance >= 11 and ranked_balance <= 20:
        print("O ranking do jogador é Bronze")
    elif ranked_balance >= 21 and ranked_balance <= 50:
        print("O ranking do jogador é Prata")
    elif ranked_balance >=51 and ranked_balance <= 80:
        print("O ranking do jogador é Ouro")
    elif ranked_balance >= 81 and ranked_balance <= 90:
        print("O ranking do jogador é Diamante")
    elif ranked_balance >= 91 and ranked_balance <= 100:
        print("O ranking do jogador é Lendário")
    elif ranked_balance >= 101:
        print("O ranking do jogador é Imortal")
    else:
        print("Ranking não identificado")

balance = calc_match_summary(wins, loses)
calc_player_ranking(balance)


