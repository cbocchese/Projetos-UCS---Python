#Na prática, introdução à lógica de programação e ambiente Phython
#Programação de auxílio ao cálculo do preço de custo e preço final

#v_couro é o valor do couro para fabricação unitária
v_couro=float(input('Digite o valor do COURO:'))
#v_solado é o valor do solado para fabricação unitária
v_solado=float(input('Digite o valor do SOLADO:'))
#v_cordoes é o valor dos cordões e ilhóses para fabricação unitária
v_cordoes=float(input('Digite o valor de CORDOES E ILHOSES:'))
#v_insumos é o valor dos insumos para fabricação unitária
v_insumos=float(input('Digite o valores de INSUMOS:'))
#v_MaoObra é o valor da Mão de Obra para fabricação unitária
v_maobra=float(input('Digite o valor de Mão de Obra:'))
#v_maketing é o valor de Marketing e Propaganda dividido pela produção
v_marketing=float(input('Digite o valor de Marketing:'))
#v_vendas é o valor do custo de vendas dividido pela Produção
v_vendas=float(input('Digite o valor dos custos de VENDAS:'))

#CÁLCULO DO PREÇO DE CUSTO
preco_custo=(v_couro*0.30)+(v_solado*0.20)+(v_cordoes*0.05)+(v_insumos*0.05)+(v_maobra*0.20)+(v_marketing*0.10)+(v_vendas*0.10)
print ('O preço do custo unitário deste modelo de sapato é:',preco_custo)

#CALCULANDO O PREÇO FINAL:
#CALCULO DO PREÇO ADICIONANDO NO LUCRO DO FABRICANTE
Preco_Lucro=preco_custo*1.30
#CALCULO DO PREÇO ADICIONANDO PERDAS DE CAPITAL
Preco_Perdas=Preco_lucro*1.15
#CALCULO DO PREÇO ADICIONANDO IMPOSTOS FEDERAIS
Preco_IPI_COFINS=Preco_perdas*1.15
#CALCULO DO PREÇO ADICIONANDO MARGEM DE VENDAS
Preco_vendas=Preco_IPI_COFINS*1.25
#CALCULO DO PREÇO ADICIONANDO IMPOSTOS ESTADUAIS E MUNICIPAIS
Preco_ICMS_INSS=Preco_venda*1.30

#PREÇO FINAL, ACRESCIDO DE TODOS OS IMPOSTOS E MARGENS DE LUCRO
Preco_Final=Preco_ICMS_INSS
print('O preço final ao consumidor deste sapato é:',Preco_Final)





