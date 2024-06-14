


#pip install pandas openpyxl

# import pandas as pd

 # from google.colab import files

#uploaded = files.upload()


# A planilha adicionada originalmente está vazia. Deve-se adicionar uma planilha e tudo funcionará como determinado.

import pandas as pd;

def carregar_planilha(arquivo):
    return pd.read_excel(arquivo)

def verificar_coluna_idade(df):
    if 'idade' not in df.columns:
        df['idade'] = pd.NA
    return df

def calcular_media_idades(df):
    return df['idade'].mean()

def filtrar_pacientes_idosos(df):
    return df[df['idade'] > 60]

def encontrar_paciente_mais_jovem(df):
    return df.loc[df['idade'].idxmin()]

def salvar_dataframe(df, arquivo):
    df.to_excel(arquivo, index=False)

def exibir_numero_pacientes(df, df_idosos):
    print(f'Número de pacientes no DataFrame original: {len(df)}')
    print(f'Número de pacientes no DataFrame de pacientes idosos: {len(df_idosos)}')

def menu():
    print('Sistema de Gerenciamento de Pacientes')
    print('1. Carregar planilha')
    print('2. Verificar Coluna "Idade"')
    print('3. Calcular Média de Idades')
    print('4. Filtrar Pacientes com mais de 60 anos')
    print('5. Encontrar paciente mais jovem')
    print('6. Salvar DataFrame de pacientes idosos')
    print('7. Exibir Número de pacientes')
    print('8. Sair')

def main():
    df = None
    df_idosos = None
    while True:
        menu()
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            df = carregar_planilha('paciente.xlsx')
            print("Planilha carregada com sucesso.")

        elif escolha == '2':
            if df is not None:
                df = verificar_coluna_idade(df)
                print('Verificação Concluída')
            else:
                print('Carregue a planilha primeiro')

        elif escolha == '3':
            if df is not None:
                media_idades = calcular_media_idades(df)
                print(f'Média de idades dos pacientes: {media_idades}')
            else:
                print('Carregue a planilha primeiro.')

        elif escolha == '4':
            if df is not None:
                df_idosos = filtrar_pacientes_idosos(df)
                print('Pacientes idosos filtrados com sucesso.')
            else:
                print('Carregue a planilha primeiro.')

        elif escolha == '5':
            if df is not None:
                paciente_mais_jovem = encontrar_paciente_mais_jovem(df)
                print('Paciente mais jovem encontrado: ')
                print(paciente_mais_jovem)
            else:
                print('Carregue a planilha primeiro.')

        elif escolha == '6':
            if df_idosos is not None:
                salvar_dataframe(df_idosos, 'pacientes_acima_60.xlsx')
                print('DataFrame dos pacientes idosos salvo com sucesso')
            else:
                print('Filtre os pacientes idosos primeiro.')

        elif escolha == '7':
            if df is not None and df_idosos is not None:
                exibir_numero_pacientes(df, df_idosos)
            else:
                print('Carregue a planilha e filtre os pacientes idosos primeiro.')

        elif escolha == '8':
            print('Saindo do Sistema...')
            break

        else:
            print('Opção Inválida. Tente Novamente.')

if __name__ == "__main__":
    main()