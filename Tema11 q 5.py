def calcular_inss(salario_bruto):
    # tabela de alíquotas do inss para 2024 
    faixas = [
        (1412.00, 0.075),
        (2666.68, 0.09),
        (4000.03, 0.12),
        (7786.02, 0.14),
    ]
    
    #calcula a contribuição do INSS 
    contribuicao = 0.0 
    for faixa, alíquota in faixas:
        if salario_bruto > faixa:
            contribuicao += faixa * alíquota
            
        else:
            contribuicao += salario_bruto - contribuicao 
            
            return contribuicao, salario_liquido 
        
        # entrada do usuario 
        salario_bruto = float(input("Digite o valor do salário bruto: R$ "))
        
        # Calcula a contribuição e o salario liquido 
        contribuicao, salario_liquido = calcular_inss(salario_bruto)
        
        # Exibe os resultados 
        print("Contribuição ao INSS: R$ " + str(round(contribuicao, 2)))
        
        print("Salário liquido: R$ " + str(round(salario_liquido, 2)))
        