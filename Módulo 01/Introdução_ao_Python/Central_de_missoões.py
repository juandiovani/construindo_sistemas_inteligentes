# Um robô só pode iniciar uma missão se tiver pelo menos 50 pontos de energia e não tiver em manutenção.

nome = input("Nome do robô: ")
energia = int(input("Energia atual (0 a 100): "))
resposta = input("Está em manutenção? (sim/não): ")

print("=== CENTRAL DE MISSÕES ===")
print("Robô:", nome)

if energia < 0 or energia > 100:
    print("Energia inválida. Informe um valor entre 0 e 100.")
elif resposta != "sim" and resposta != "não":
    print("Resposta inválida. Use sim ou não.")
else:
    em_manutencao = resposta == "sim"

    if energia >= 50 and not em_manutencao:
        print("Missão autorizada.")
        energia = energia - 30
        print("Energia após a missão:", energia)
    elif em_manutencao:
        print("Missão bloqueada:  robô em manutenção.")
    else:
        print("Missão bloqueada: energia insuficiente.")

print("Atendimento encerrado.")                        