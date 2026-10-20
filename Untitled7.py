
print("=== BEM-VINDO AO SUPORTE ===")
nome = input("Digite seu nome: ")

# 1. Verifica se o nome foi preenchido
if not nome:
    nome = "Cliente Anônimo"

print(f"\nOlá, {nome}!")
print("Escolha o tipo de problema:")
print("1 - Problema com a Internet")
print("2 - Problema com a Fatura")
print("3 - Outros assuntos")

opcao = input("Digite o número da opção: ")

# 2. Tratamento da opção principal
if opcao == "1":
    print("\n[Internet]")
    status = input("A luz do roteador está vermelha? (s/n): ")
    if status.lower() == "s":
        print("Ação: Reinicie o roteador tirando da tomada por 10 segundos.")
    else:
        print("Ação: Vamos abrir um chamado técnico.")

elif opcao == "2":
    print("\n[Fatura]")
    via = input("Deseja a 2ª via por e-mail? (s/n): ")
    if via.lower() == "s":
        print("Ação: 2ª via enviada com sucesso!")
    else:
        print("Ação: Consulte o boleto no aplicativo.")

elif opcao == "3":
    print("\n[Outros assuntos]")
    urgente = input("É uma emergência? (s/n): ")
    if urgente.lower() == "s":
        print("Ação: Transferindo para um atendente humano urgente.")
    else:
        print("Ação: Retornaremos em até 24 horas.")

else:
    print("\nOpção inválida! Encerrando atendimento.")

print("\nObrigado por usar nosso sistema!")