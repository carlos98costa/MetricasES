import PySimpleGUI as sg
import os


listLP = ['Cobol', 'Pascal', 'Linguagens Orientadas a Objeto (C++)',
          'Java / Delphi / Visual Basic', 'Geradores de Código (SQL + HTML), PY, JS...']
listTS = ['Sistema Comercial', 'Comércio Eletrônico', 'Sistema Web']
dados = []
dadosNew = []
dadosNewZ = []
soma = 0
FPb = 0
FPr = 0
fa = 1.35
lp = 0
ts = 0
tKLOC = 0
diasM = 22
horasD = 6
minH = 60
vhT = 0
indicador = 0
iso = 132
custo = 0
nameLP = ''
nameTS = ''

##Entrada
count1a4E = 0
count5a15E = 0
count16ouMaisE = 0
entradasSimples = 0
entradasMedio = 0
entradasComplexo = 0
##Saida
count1a5S = 0
count6a19S = 0
count20ouMaisS = 0
saidasSimples = 0
saidasMedio = 0
saidasComplexo = 0
##Consulta
count1a4C = 0
count5a15C = 0
count16ouMaisC = 0
consultasSimples = 0
consultasMedio = 0
consultasComplexo = 0
##Arquivo
count1a19A = 0
count20a50A = 0
count51ouMaisA = 0
arquivosSimples = 0
arquivosMedio = 0
arquivosComplexo = 0
##Interface
count1a19I = 0
count20a50I = 0
count51ouMaisI = 0
interfacesSimples = 0
interfacesMedio = 0
interfacesComplexo = 0




def tela_1():
    sg.theme('Gray Gray Gray')
    layout_1 = [[sg.T('1ª etapa')],
        [sg.Text('Informe um numero:'), sg.Input(size=(10), k='-dados-', do_not_clear=False),
         sg.LB(values=dados, size=(5, 5), k='-LB-', enable_events=True)],
        [sg.Button('Inserir'), sg.Button('Limpar'), sg.Button('-1')],
        [sg.Button('2 etapa', enable_events=True), sg.Cancel('Finalizar')]
    ]

    return sg.Window('1ª Etapa', layout=layout_1, finalize=True, size=(500, 450))

def tela_2():
    sg.theme('Gray Gray Gray')
    layout_2 = [[sg.T('2ª etapa')],
                [sg.T('Clique abaixo para gerar o FPr')],
                [sg.Button('Gerar E2')],
                [sg.T('Ainda não gerou', k='-gerou-', text_color='red')],
                [sg.Button('3 Etapa'), sg.Cancel('Voltar'), sg.Cancel('Finalizar')]]

    return sg.Window('2ª Etapa', layout=layout_2, finalize=True, size=(500, 450))

def tela_3():
    sg.theme('Gray Gray Gray')
    layout_3 = [[sg.T('3ª etapa')],
                [sg.T('Informe a linguagem:'), sg.Combo(values=listLP, default_value=listLP[-1], k='-LP-', enable_events=True)],
                [sg.T('Informe o sistema:'), sg.Combo(values=listTS, default_value=listTS[0], k='-TS-')],
                [sg.T('FPr'), sg.T(FPr, k='-FPr-')],
                [sg.T('LP'), sg.T(lp, k='-LP1-')],
                [sg.T('TS'), sg.T(ts, k='-TS1-')],
                [sg.Button('Gerar E3')],
                [sg.T('Ainda não gerou', k='-gerou1-', text_color='red')],
                [sg.Button('4 Etapa'), sg.Cancel('Voltar'), sg.Cancel('Finalizar')]]

    return sg.Window('3ª Etapa', layout=layout_3, finalize=True, size=(500, 450))

def tela_4():
    sg.theme('Gray Gray Gray')
    layout_4 = [[sg.T('4ª etapa')],
                [sg.T('Dados já gerados anteriormente:')],
                [sg.T('FPr'), sg.T(FPr, k='-FPr-')],
                [sg.T('LP'), sg.T(lp, k='-LP1-')],
                [sg.T('TS'), sg.T(ts, k='-TS1-')],
                [sg.T('Novos dados a serem gerados:')],
                [sg.T('Informe o valor da hora:'), sg.Input(k='-VHT-')],
                [sg.T('Total de KLOC'), sg.T(tKLOC, k='-TKLOC-')],
                [sg.T('Valor Hora de Trabalho'), sg.T(f'R$ {vhT}', k='-RVHT-')],
                [sg.T('Indicador'), sg.T(indicador, k='-I-')],
                [sg.T('Custo'), sg.T(f'R$ {custo}', k='-CUSTO-')],
                [sg.T('Prazo'), sg.T(f'{diasM} d', k='-PRAZOD-'), sg.T(f'{horasD} h', k='-PRAZOH-'), sg.T(f'{minH} m', k='-PRAZOM-')],
                [sg.Button('Gerar E4')],
                [sg.T('Ainda não gerou', k='-gerou2-', text_color='red')],
                [sg.Button('Resultado detalhado'), sg.Cancel('Voltar'), sg.Cancel('Finalizar')]]

    return sg.Window('4ª Etapa', layout=layout_4, finalize=True, size=(500, 450))

def tela_resultado():
    sg.theme('Gray Gray Gray')
    layout_5 = [[sg.T('FPr'), sg.T(FPr, k='-FPr-')],
                [sg.T('LP'), sg.T(lp, k='-LP1-')],
                [sg.T('TS'), sg.T(ts, k='-TS1-')],
                [sg.T('Total de KLOC'), sg.T(tKLOC, k='-TKLOC-')],
                [sg.T('Valor Hora de Trabalho'), sg.T(f'R$ {vhT}', k='-RVHT-')],
                [sg.T('Indicador'), sg.T(indicador, k='-I-')],
                [sg.T('Custo'), sg.T(f'R$ {custo}', k='-CUSTO-')],
                [sg.T('Prazo'), sg.T(f'{diasR}d', k='-PRAZOD-'), sg.T(f'{horasR}h', k='-PRAZOH-'), sg.T(f'{minR}m', k='-PRAZOM-')],
                [sg.Button('Novo exercicio'), sg.Cancel('Voltar'), sg.Cancel('Finalizar')],
                [sg.Button('Gerar TXT')]
                ]

    return sg.Window('Resultado', layout=layout_5, finalize=True, size=(500, 450))

janela1, janela2, janela3, janela4, janela5 = tela_1(), None, None, None, None

while True:
    window,event,values = sg.read_all_windows()

    if event == sg.WIN_CLOSED or event == 'Finalizar':
        break
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela2.un_hide()
    if window == janela4 and event == 'Voltar':
        janela4.hide()
        janela3.un_hide()

    if window == janela1:
        window['-LB-'].update(dados)

    if window == janela1 and event == 'Inserir':
        dadosNew.append(int(values['-dados-']))
        window['-LB-'].update(dadosNew)
    if window == janela1 and event == 'Limpar':
        dadosNew.clear()
        window['-LB-'].update(dadosNew)
    if window == janela1 and event == '-1':
        dadosNew.pop()
        window['-LB-'].update(dadosNew)

    if window == janela1 and event == '2 etapa':
        soma
        for i in dadosNew:
            soma += i

        janela1.hide()
        janela2 = tela_2()

    if window == janela2 and event == 'Gerar E2':
        window['-gerou-'].update('FPr gerado com sucesso!', text_color='green')
        ##ENTRADA
        dadosNewX = dadosNew

        for i in dadosNewX:
            if i >= 1 and i < 5:
                count1a4E += 1
            elif i>= 5 and i < 16:
                count5a15E += 1
            elif i >= 16:
                count16ouMaisE += 1


        if count1a4E == 1:
            entradasSimples += count1a4E
        elif count1a4E == 2:
            entradasSimples += count1a4E
        elif count1a4E >= 3:
            entradasMedio += count1a4E

        if count5a15E == 1:
            entradasSimples += count5a15E
        elif count5a15E == 2:
            entradasMedio += count5a15E
        elif count5a15E >= 3:
            entradasComplexo += count5a15E

        if count16ouMaisE == 1:
            entradasMedio += count16ouMaisE
        elif count16ouMaisE == 2:
            entradasComplexo += count16ouMaisE
        elif count16ouMaisE >= 3:
            entradasComplexo += count16ouMaisE


        ##SAIDA

        dadosNew = dadosNewX
        dadosNew.append(sum(dadosNewX))
        for i in dadosNew:
            if i >= 1 and i < 6:
                count1a5S += 1
            elif i >= 6 and i < 20:
                count6a19S += 1
            elif i >= 20:
                count20ouMaisS += 1

        if count1a5S == 1:
            saidasSimples += count1a5S
        elif count1a5S == 2 or count1a5S == 3:
            saidasSimples += count1a5S
        elif count1a5S >= 4:
            saidasMedio += count1a5S

        if count6a19S == 1:
            saidasSimples += count6a19S
        elif count6a19S == 2 or count6a19S == 3:
            saidasMedio += count6a19S
        elif count6a19S >= 4:
            saidasComplexo += count6a19S

        if count20ouMaisS == 1:
            saidasMedio += count20ouMaisS
        elif count20ouMaisS == 2 or count20ouMaisS == 3:
            saidasComplexo += count20ouMaisS
        elif count20ouMaisS >= 4:
            saidasComplexo += count20ouMaisS


        #CONSULTA
        for i in dadosNewX:
            if i >= 1 and i < 5:
                count1a4C += 1
            elif i >= 5 and i < 16:
                count5a15C += 1
            elif i >= 16:
                count16ouMaisC += 1

        if count1a4C == 1:
            consultasSimples += count1a4C
        elif count1a4C == 2:
            consultasSimples += count1a4C
        elif count1a4C >= 3:
            consultasMedio += count1a4C

        if count5a15C == 1:
            consultasSimples += count5a15C
        elif count5a15C == 2:
            consultasMedio += count5a15C
        elif count5a15C >= 3:
            consultasComplexo += count5a15C

        if count16ouMaisC == 1:
            consultasMedio += count16ouMaisC
        elif count16ouMaisC == 2:
            consultasComplexo += count16ouMaisC
        elif count16ouMaisC >= 3:
            consultasComplexo += count16ouMaisC


        ##ARQUIVO
        dadosNewX.pop()
        for i in dadosNewX:
            if i >= 1 and i < 20:
                count1a19A += 1
            elif i >= 20 and i < 51:
                count20a50A += 1
            elif i >= 51:
                count51ouMaisA += 1

        if count1a19A == 1:
            arquivosSimples += count1a19A
        elif count1a19A >= 2 and count1a19A <= 5:
            arquivosSimples += count1a19A
        elif count1a19A >= 6:
            arquivosMedio += count1a19A

        if count20a50A == 1:
            arquivosSimples += count20a50A
        elif count20a50A >= 2 and count20a50A <= 5:
            arquivosMedio += count20a50A
        elif count20a50A >= 6:
            arquivosComplexo += count20a50A

        if count51ouMaisA == 1:
            arquivosMedio += count51ouMaisA
        elif count51ouMaisA >= 2 and count51ouMaisA <= 5:
            arquivosComplexo += count51ouMaisA
        elif count51ouMaisA >= 6:
            arquivosComplexo += count51ouMaisA


        ##INTERFACE
        dadosNewX.append(sum(dadosNew))
        for i in dadosNewX:
            if i >= 1 and i < 20:
                count1a19I += 1
            elif i >= 20 and i < 51:
                count20a50I += 1
            elif i >= 51:
                count51ouMaisI += 1

        if count1a19I == 1:
            interfacesSimples += count1a19I
        elif count1a19I >= 2 and count1a19I <= 5:
            interfacesSimples += count1a19I
        elif count1a19I >= 6:
            interfacesMedio += count1a19I

        if count20a50I == 1:
            interfacesSimples += count20a50I
        elif count20a50I >= 2 and count20a50I <= 5:
            interfacesMedio += count20a50I
        elif count20a50I >= 6:
            interfacesComplexo += count20a50I

        if count51ouMaisI == 1:
            interfacesMedio += count51ouMaisI
        elif count51ouMaisI >= 2 and count51ouMaisI <= 5:
            interfacesComplexo += count51ouMaisI
        elif count51ouMaisI >= 6:
            interfacesComplexo += count51ouMaisI


        FPb += ((entradasSimples * 3) + (entradasMedio * 4) + (entradasComplexo * 6) +
                 (saidasSimples * 4) + (saidasMedio * 5) + (saidasComplexo * 7) +
                 (consultasSimples * 3) + (consultasMedio * 4) + (consultasComplexo * 6) +
                 (arquivosSimples * 7) + (arquivosMedio * 10) + (arquivosComplexo * 15) +
                 (interfacesSimples * 5) + (interfacesMedio * 7) + (interfacesComplexo * 10))
        FPr = int(round(fa * FPb))



    if window == janela2 and event == '3 Etapa':
        janela2.hide()
        janela3 = tela_3()
    if window == janela3:
        window['-FPr-'].update(str(FPr))

    if window == janela3 and event == 'Gerar E3':

        if values['-LP-'] == 'Cobol':
            nameLP = 'Cobol'
            lp = 100
        elif values['-LP-'] == 'Pascal':
            nameLP = 'Pascal'
            lp = 90
        elif values['-LP-'] == 'Linguagens Orientadas a Objeto (C++)':
            nameLP = 'Linguagens Orientadas a Objeto (C++)'
            lp = 30
        elif values['-LP-'] == 'Java / Delphi / Visual Basic':
            nameLP = 'Java / Delphi / Visual Basic'
            lp = 20
        else:
            nameLP = 'Geradores de Código (SQL + HTML), PY, JS...'
            lp = 15

        if values['-TS-'] == 'Sistema Comercial':
            nameTS = 'Sistema Comercial'
            ts = 2500
        elif values['-TS-'] == 'Comércio Eletrônico':
            nameTS = 'Comércio Eletrônico'
            ts = 3600
        else:
            nameTS = 'Sistema Web'
            ts = 3300

        window['-LP1-'].update(str(lp))
        window['-TS1-'].update(str(ts))
        window['-gerou1-'].update('Valores gerados com sucesso!', text_color='green')

    if window == janela3 and event == '4 Etapa':
        janela3.hide()
        janela4 = tela_4()

    if window == janela4 and event == 'Gerar E4':
        vhT = float(values['-VHT-'])
        vhT = round(vhT, 2)
        tKLOC = FPr * lp
        indicador = round(tKLOC / ts, 2)
        custo = round(indicador * 132 * vhT, 2)
        diasR = int(indicador * diasM)
        horasR = round((indicador * diasM) - diasR, 2)
        minR = round((horasR * horasD)- int(horasR * 6), 2) * 60
        horasR = int(horasR * 6)
        minR = int(minR)
        window['-TKLOC-'].update(str(tKLOC))
        window['-RVHT-'].update(str(vhT))
        window['-I-'].update(str(indicador))
        window['-CUSTO-'].update(str(custo))
        window['-PRAZOD-'].update(str(diasR) + 'd')
        window['-PRAZOH-'].update(str(horasR) + 'h')
        window['-PRAZOM-'].update(str(minR) + 'm')
        window['-gerou2-'].update('Valores gerados com sucesso!', text_color='green')
        #tKLOC = FPr *

    if window == janela4 and event == 'Resultado detalhado':
        janela4.hide()
        janela5 = tela_resultado()

    if window == janela5 and event == 'Voltar':
        janela5.hide()
        janela4.un_hide()

    if window == janela5 and event == 'Gerar TXT':
        janela5.hide()
        dadosNewX.pop()
        resultado = f'Numeros listados:{dadosNew} \n' \
                    f'Geral: {sum(dadosNew)} \n' \
                    f'Entrada Simples: {entradasSimples}, Medio: {entradasMedio}, Complexo: {entradasComplexo} \n' \
                    f'Saida Simples: {saidasSimples}, Medio: {saidasMedio}, Complexo: {saidasComplexo} \n' \
                    f'Consulta Simples: {consultasSimples}, Medio: {consultasMedio}, Complexo: {consultasComplexo} \n' \
                    f'Arquivo Simples: {arquivosSimples}, Medio: {arquivosMedio}, Complexo: {arquivosComplexo} \n' \
                    f'Interface Simples: {interfacesSimples}, Medio: {interfacesMedio}, Complexo: {interfacesComplexo} \n' \
                    f'FPb: {FPb} \n' \
                    f'FPr: {FPr} \n' \
                    f'Linguagem de programação: {nameLP}: Linhas p/ FPb:{lp} \n' \
                    f'Tipo de sistema: {nameTS}: Linhas Tipo Sistema: {ts} \n' \
                    f'Valor da hora de trabalho: R$ {vhT} \n' \
                    f'Total de linhas de codigo: {tKLOC} \n' \
                    f'Indicador: {indicador} \n' \
                    f'Custo do programa: R$ {custo} \n' \
                    f'Prazo de entrega: {diasR} dias {horasR} horas {minR} minutos'


        check = True
        numFile = 0

        sg.popup('O arquivo foi gerado com sucesso!')
        janela5.un_hide()

        while check == True:
            nomeArquivo = (f'Exercicio{numFile}.txt')
            if os.path.exists(nomeArquivo) == True:
                True
            else:
                arquivo = open(nomeArquivo, 'w+')
                arquivo.write(resultado)
                arquivo.close()
                check = False
            numFile = numFile + 1

    if window == janela5 and event == 'Novo exercicio':
        dados = []
        dadosNew = []

        soma = 0
        FPb = 0
        FPr = 0
        fa = 1.35
        lp = 0
        ts = 0
        tKLOC = 0
        diasM = 22
        horasD = 6
        minH = 60
        vhT = 0
        indicador = 0
        iso = 132
        custo = 0

        ##Entrada
        count1a4E = 0
        count5a15E = 0
        count16ouMaisE = 0
        entradasSimples = 0
        entradasMedio = 0
        entradasComplexo = 0
        ##Saida
        count1a5S = 0
        count6a19S = 0
        count20ouMaisS = 0
        saidasSimples = 0
        saidasMedio = 0
        saidasComplexo = 0
        ##Consulta
        count1a4C = 0
        count5a15C = 0
        count16ouMaisC = 0
        consultasSimples = 0
        consultasMedio = 0
        consultasComplexo = 0
        ##Arquivo
        count1a19A = 0
        count20a50A = 0
        count51ouMaisA = 0
        arquivosSimples = 0
        arquivosMedio = 0
        arquivosComplexo = 0
        ##Interface
        count1a19I = 0
        count20a50I = 0
        count51ouMaisI = 0
        interfacesSimples = 0
        interfacesMedio = 0
        interfacesComplexo = 0
        dadosNew.clear()

        janela5.hide()
        janela1.un_hide()
