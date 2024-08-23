def get_player_ranking(vitorias):
    if vitorias <= 10:
        return "Ferro"
    elif vitorias <= 20:
        return "Bronze"
    elif vitorias <= 50:
        return "Prata"
    elif vitorias <= 80:
        return "Ouro"
    elif vitorias <= 90:
        return "Diamante"
    elif vitorias <= 100:
        return "Lendario"
    else:
        return "Imortal"


print("\nBem vindo á calculadora de partidas rankeadas!")

while True:
    print("\nDigite número de vitórias e derrotas do Herói: (deixe vazio para sair)")

    try:
        vitorias = int(input("-Nº de vitórias: "))
        derrotas = int(input("-Nº de derrotas: "))
        saldoVitorias = vitorias - derrotas

        nivel = get_player_ranking(vitorias)
    except (ValueError, EOFError):
        break

    print(
        f"\nO Herói tem de saldo de {saldoVitorias} está no nível de {nivel}"
    )
