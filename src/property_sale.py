Valor_Imovel_Anunciado = input("QUAL O VALOR DO IMÓVEL R$:")
Comissao_Imobiliaria = 6
Valor_Imovel_Anunciado = int(Valor_Imovel_Anunciado)
Valor_Liquido_Vendedor = Valor_Imovel_Anunciado-(Valor_Imovel_Anunciado*Comissao_Imobiliaria/100)
Valor_Comissao_Imobiliaria = (Valor_Imovel_Anunciado*6/100)
print("VALOR LIQUIDO QUE O VENDEDOR VAI RECEBER:" + str(Valor_Liquido_Vendedor) )
print("VALOR DE COMISSÃO DA IMOBILIÁRIA:" + str(Valor_Comissao_Imobiliaria))