# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_conceito(conceito):
  if conceito == "Claro":
    return "Mensagem objetiva e específica"

# COMPLETE AQUI: Preencha corretamente cada conceito, considerando as descrições abaixo:
  elif conceito == "Ambíguo":
    return "Mensagem vaga e imprecisa"

  elif conceito == "Diretivo":
    return "Instrução clara para uma tarefa específica"

  elif conceito == "Indireto":
    return "Pergunta geral que permite interpretações amplas"

# Imprime a descrição do conceito recebido na "entrada" através da função "descrever_conceito". 
print(descrever_conceito(entrada))