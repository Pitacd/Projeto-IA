def calcular_pontuacao(tabuleiro):
    pontuacao_total = 0
     for linha in tabuleiro:
       for peca in linha:
           if peca == 0:
               pontuacao_total +=1
    
