imovel = input("Por favor, informe o tipo do imóvel: (Ex.: casa, comercial ou apartamento) \n")

if imovel != "comercial" and imovel != "casa" and imovel != "apartamento":
    print("Opção informada inválida")
else:
    m3 = int(input("Por favor, informe o consumo mensal: m³ (Número decimal) \n"))
    if imovel == "comercial":
        print("Tarifa comercial aplicada - Consulte o plano corporativo")

    if imovel == "apartamento" and m3 < 10:
        print("Consumo Econômico - Excelente controle de água!")

    if (imovel == "apartamento" or imovel == "casa") and m3 <= 25:
        print("Consumo moderado - Dentro do padrão residencial.")

    if m3 > 25:
        print("Consumo Excessivo - Adote medidas de economias e verifique vazamentos. ")

 