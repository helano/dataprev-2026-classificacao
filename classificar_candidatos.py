import pandas as pd
from datetime import datetime, date

# Data da prova objetiva (11/10/2026)
DATA_PROVA = date(2026, 10, 11)

# Regras de eliminação
NOTA_MINIMA_TOTAL = 57.5

# Critérios de desempate aplicáveis com os dados disponíveis:
# a) idade >= 60 anos
# b) maior nota em Conhecimentos Específicos
# f) mais velho (data de nascimento mais antiga)

# Tabela de vagas extraída do edital (vagas imediatas e cadastro de reserva)
# Formato: (perfil, localidade): {'AC': (imediatas, reserva), 'PCD': (..., ...), 'PP': ..., 'PI': ..., 'PQ': ...}
VAGAS = {
    # 1. ANÁLISE DE NEGÓCIO DE TI
    ("ANÁLISE DE NEGÓCIO DE TI", "BRASÍLIA / DF"): {"AC": (3, 32), "PCD": (1, 2), "PP": (1, 13), "PI": (0, 2), "PQ": (0, 1)},
    ("ANÁLISE DE NEGÓCIO DE TI", "RIO DE JANEIRO / RJ"): {"AC": (0, 6), "PCD": (0, 1), "PP": (0, 2), "PI": (0, 0), "PQ": (0, 0)},
    ("ANÁLISE DE NEGÓCIO DE TI", "SÃO PAULO / SP"): {"AC": (0, 6), "PCD": (0, 1), "PP": (0, 2), "PI": (0, 0), "PQ": (0, 0)},
    ("ANÁLISE DE NEGÓCIO DE TI", "FORTALEZA / CE"): {"AC": (0, 6), "PCD": (0, 1), "PP": (0, 2), "PI": (0, 0), "PQ": (0, 0)},
    ("ANÁLISE DE NEGÓCIO DE TI", "JOÃO PESSOA / PB"): {"AC": (0, 6), "PCD": (0, 1), "PP": (0, 2), "PI": (0, 0), "PQ": (0, 0)},
    ("ANÁLISE DE NEGÓCIO DE TI", "NATAL / RN"): {"AC": (0, 6), "PCD": (0, 1), "PP": (0, 2), "PI": (0, 0), "PQ": (0, 0)},
    ("ANÁLISE DE NEGÓCIO DE TI", "FLORIANÓPOLIS / SC"): {"AC": (0, 6), "PCD": (0, 1), "PP": (0, 2), "PI": (0, 0), "PQ": (0, 0)},

    # 2. ARQUITETURA, ENGENHARIA E SUSTENTAÇÃO TECNOLÓGICA
    ("ARQUITETURA, ENGENHARIA E SUSTENTAÇÃO TECNOLÓGICA", "BRASÍLIA / DF"): {"AC": (6, 32), "PCD": (1, 2), "PP": (3, 12), "PI": (0, 2), "PQ": (0, 1)},
    ("ARQUITETURA, ENGENHARIA E SUSTENTAÇÃO TECNOLÓGICA", "RIO DE JANEIRO / RJ"): {"AC": (6, 32), "PCD": (1, 2), "PP": (3, 12), "PI": (0, 2), "PQ": (0, 1)},
    ("ARQUITETURA, ENGENHARIA E SUSTENTAÇÃO TECNOLÓGICA", "SÃO PAULO / SP"): {"AC": (6, 32), "PCD": (1, 2), "PP": (3, 12), "PI": (0, 2), "PQ": (0, 1)},
    ("ARQUITETURA, ENGENHARIA E SUSTENTAÇÃO TECNOLÓGICA", "FORTALEZA / CE"): {"AC": (0, 5), "PCD": (0, 1), "PP": (0, 3), "PI": (0, 0), "PQ": (0, 0)},
    ("ARQUITETURA, ENGENHARIA E SUSTENTAÇÃO TECNOLÓGICA", "JOÃO PESSOA / PB"): {"AC": (0, 5), "PCD": (0, 1), "PP": (0, 3), "PI": (0, 0), "PQ": (0, 0)},
    ("ARQUITETURA, ENGENHARIA E SUSTENTAÇÃO TECNOLÓGICA", "NATAL / RN"): {"AC": (0, 5), "PCD": (0, 1), "PP": (0, 3), "PI": (0, 0), "PQ": (0, 0)},
    ("ARQUITETURA, ENGENHARIA E SUSTENTAÇÃO TECNOLÓGICA", "FLORIANÓPOLIS / SC"): {"AC": (0, 5), "PCD": (0, 1), "PP": (0, 3), "PI": (0, 0), "PQ": (0, 0)},

    # 3. DESENVOLVIMENTO DE SOFTWARE
    ("DESENVOLVIMENTO DE SOFTWARE", "BRASÍLIA / DF"): {"AC": (0, 11), "PCD": (0, 1), "PP": (0, 4), "PI": (0, 1), "PQ": (0, 0)},
    ("DESENVOLVIMENTO DE SOFTWARE", "RIO DE JANEIRO / RJ"): {"AC": (0, 11), "PCD": (0, 1), "PP": (0, 4), "PI": (0, 1), "PQ": (0, 0)},
    ("DESENVOLVIMENTO DE SOFTWARE", "SÃO PAULO / SP"): {"AC": (0, 11), "PCD": (0, 1), "PP": (0, 4), "PI": (0, 1), "PQ": (0, 0)},
    ("DESENVOLVIMENTO DE SOFTWARE", "FORTALEZA / CE"): {"AC": (13, 52), "PCD": (1, 4), "PP": (5, 20), "PI": (1, 2), "PQ": (0, 2)},
    ("DESENVOLVIMENTO DE SOFTWARE", "JOÃO PESSOA / PB"): {"AC": (13, 52), "PCD": (1, 4), "PP": (5, 20), "PI": (1, 2), "PQ": (0, 2)},
    ("DESENVOLVIMENTO DE SOFTWARE", "NATAL / RN"): {"AC": (13, 52), "PCD": (1, 4), "PP": (5, 20), "PI": (1, 2), "PQ": (0, 2)},
    ("DESENVOLVIMENTO DE SOFTWARE", "FLORIANÓPOLIS / SC"): {"AC": (13, 52), "PCD": (1, 4), "PP": (5, 20), "PI": (1, 2), "PQ": (0, 2)},

    # 4. INTELIGÊNCIA DA INFORMAÇÃO
    ("INTELIGÊNCIA DA INFORMAÇÃO", "BRASÍLIA / DF"): {"AC": (3, 15), "PCD": (1, 1), "PP": (1, 6), "PI": (0, 1), "PQ": (0, 1)},
    ("INTELIGÊNCIA DA INFORMAÇÃO", "RIO DE JANEIRO / RJ"): {"AC": (0, 15), "PCD": (0, 2), "PP": (0, 6), "PI": (0, 1), "PQ": (0, 1)},
    ("INTELIGÊNCIA DA INFORMAÇÃO", "SÃO PAULO / SP"): {"AC": (0, 6), "PCD": (0, 1), "PP": (0, 2), "PI": (0, 0), "PQ": (0, 0)},
    ("INTELIGÊNCIA DA INFORMAÇÃO", "FORTALEZA / CE"): {"AC": (6, 32), "PCD": (1, 2), "PP": (3, 12), "PI": (0, 2), "PQ": (0, 1)},
    ("INTELIGÊNCIA DA INFORMAÇÃO", "JOÃO PESSOA / PB"): {"AC": (6, 32), "PCD": (1, 2), "PP": (3, 12), "PI": (0, 2), "PQ": (0, 1)},
    ("INTELIGÊNCIA DA INFORMAÇÃO", "NATAL / RN"): {"AC": (6, 32), "PCD": (1, 2), "PP": (3, 12), "PI": (0, 2), "PQ": (0, 1)},
    ("INTELIGÊNCIA DA INFORMAÇÃO", "FLORIANÓPOLIS / SC"): {"AC": (6, 32), "PCD": (1, 2), "PP": (3, 12), "PI": (0, 2), "PQ": (0, 1)},

    # 5. SEGURANÇA CIBERNÉTICA E PROTEÇÃO DE DADOS
    ("SEGURANÇA CIBERNÉTICA E PROTEÇÃO DE DADOS", "BRASÍLIA / DF"): {"AC": (3, 12), "PCD": (1, 1), "PP": (1, 5), "PI": (0, 1), "PQ": (0, 1)},
    ("SEGURANÇA CIBERNÉTICA E PROTEÇÃO DE DADOS", "RIO DE JANEIRO / RJ"): {"AC": (3, 12), "PCD": (1, 1), "PP": (1, 5), "PI": (0, 1), "PQ": (0, 1)},
    ("SEGURANÇA CIBERNÉTICA E PROTEÇÃO DE DADOS", "SÃO PAULO / SP"): {"AC": (3, 12), "PCD": (1, 1), "PP": (1, 5), "PI": (0, 1), "PQ": (0, 1)},
    ("SEGURANÇA CIBERNÉTICA E PROTEÇÃO DE DADOS", "FORTALEZA / CE"): {"AC": (0, 3), "PCD": (0, 1), "PP": (0, 1), "PI": (0, 0), "PQ": (0, 0)},
    ("SEGURANÇA CIBERNÉTICA E PROTEÇÃO DE DADOS", "JOÃO PESSOA / PB"): {"AC": (0, 11), "PCD": (0, 1), "PP": (0, 4), "PI": (0, 1), "PQ": (0, 0)},
    ("SEGURANÇA CIBERNÉTICA E PROTEÇÃO DE DADOS", "NATAL / RN"): {"AC": (0, 3), "PCD": (0, 1), "PP": (0, 1), "PI": (0, 0), "PQ": (0, 0)},
    ("SEGURANÇA CIBERNÉTICA E PROTEÇÃO DE DADOS", "FLORIANÓPOLIS / SC"): {"AC": (1, 10), "PCD": (1, 0), "PP": (0, 4), "PI": (0, 1), "PQ": (0, 0)},

    # 6. GESTÃO DE SERVIÇOS DE TIC
    ("GESTÃO DE SERVIÇOS DE TIC", "BRASÍLIA / DF"): {"AC": (3, 28), "PCD": (1, 2), "PP": (1, 11), "PI": (0, 2), "PQ": (0, 1)},
    ("GESTÃO DE SERVIÇOS DE TIC", "RIO DE JANEIRO / RJ"): {"AC": (10, 38), "PCD": (1, 3), "PP": (4, 15), "PI": (0, 2), "PQ": (0, 2)},
    ("GESTÃO DE SERVIÇOS DE TIC", "SÃO PAULO / SP"): {"AC": (10, 38), "PCD": (1, 3), "PP": (4, 15), "PI": (0, 2), "PQ": (0, 2)},

    # 7. ADVOCACIA
    ("ADVOCACIA", "BRASÍLIA / DF"): {"AC": (0, 18), "PCD": (0, 2), "PP": (0, 7), "PI": (0, 1), "PQ": (0, 1)},
    ("ADVOCACIA", "RIO DE JANEIRO / RJ"): {"AC": (0, 15), "PCD": (0, 2), "PP": (0, 6), "PI": (0, 1), "PQ": (0, 1)},

    # 8. CONTABILIDADE
    ("CONTABILIDADE", "RIO DE JANEIRO / RJ"): {"AC": (0, 15), "PCD": (0, 2), "PP": (0, 6), "PI": (0, 1), "PQ": (0, 1)},

    # 9. COMUNICAÇÃO SOCIAL
    ("COMUNICAÇÃO SOCIAL", "BRASÍLIA / DF"): {"AC": (0, 5), "PCD": (0, 1), "PP": (0, 3), "PI": (0, 0), "PQ": (0, 0)},
    ("COMUNICAÇÃO SOCIAL", "RIO DE JANEIRO / RJ"): {"AC": (0, 5), "PCD": (0, 1), "PP": (0, 3), "PI": (0, 0), "PQ": (0, 0)},

    # 10. GESTÃO ECONÔMICO-FINANCEIRA
    ("GESTÃO ECONÔMICO-FINANCEIRA", "RIO DE JANEIRO / RJ"): {"AC": (0, 18), "PCD": (0, 2), "PP": (0, 7), "PI": (0, 1), "PQ": (0, 1)},

    # 11. ADMINISTRAÇÃO E GOVERNANÇA
    ("ADMINISTRAÇÃO E GOVERNANÇA", "BRASÍLIA / DF"): {"AC": (0, 18), "PCD": (0, 2), "PP": (0, 7), "PI": (0, 1), "PQ": (0, 1)},
    ("ADMINISTRAÇÃO E GOVERNANÇA", "RIO DE JANEIRO / RJ"): {"AC": (0, 26), "PCD": (0, 2), "PP": (0, 10), "PI": (0, 1), "PQ": (0, 1)},
    ("ADMINISTRAÇÃO E GOVERNANÇA", "SÃO PAULO / SP"): {"AC": (0, 18), "PCD": (0, 2), "PP": (0, 7), "PI": (0, 1), "PQ": (0, 1)},
    ("ADMINISTRAÇÃO E GOVERNANÇA", "FORTALEZA / CE"): {"AC": (0, 18), "PCD": (0, 2), "PP": (0, 7), "PI": (0, 1), "PQ": (0, 1)},
    ("ADMINISTRAÇÃO E GOVERNANÇA", "JOÃO PESSOA / PB"): {"AC": (0, 18), "PCD": (0, 2), "PP": (0, 7), "PI": (0, 1), "PQ": (0, 1)},
    ("ADMINISTRAÇÃO E GOVERNANÇA", "NATAL / RN"): {"AC": (0, 18), "PCD": (0, 2), "PP": (0, 7), "PI": (0, 1), "PQ": (0, 1)},
    ("ADMINISTRAÇÃO E GOVERNANÇA", "FLORIANÓPOLIS / SC"): {"AC": (0, 18), "PCD": (0, 2), "PP": (0, 7), "PI": (0, 1), "PQ": (0, 1)},

    # 12. ENGENHARIA
    ("ENGENHARIA", "BRASÍLIA / DF"): {"AC": (0, 5), "PCD": (0, 1), "PP": (0, 3), "PI": (0, 0), "PQ": (0, 0)},
    ("ENGENHARIA", "RIO DE JANEIRO / RJ"): {"AC": (0, 5), "PCD": (0, 1), "PP": (0, 3), "PI": (0, 0), "PQ": (0, 0)},
    ("ENGENHARIA", "SÃO PAULO / SP"): {"AC": (0, 5), "PCD": (0, 1), "PP": (0, 3), "PI": (0, 0), "PQ": (0, 0)},
    ("ENGENHARIA", "FORTALEZA / CE"): {"AC": (0, 5), "PCD": (0, 1), "PP": (0, 3), "PI": (0, 0), "PQ": (0, 0)},
    ("ENGENHARIA", "JOÃO PESSOA / PB"): {"AC": (0, 5), "PCD": (0, 1), "PP": (0, 3), "PI": (0, 0), "PQ": (0, 0)},
    ("ENGENHARIA", "NATAL / RN"): {"AC": (0, 5), "PCD": (0, 1), "PP": (0, 3), "PI": (0, 0), "PQ": (0, 0)},
    ("ENGENHARIA", "FLORIANÓPOLIS / SC"): {"AC": (0, 5), "PCD": (0, 1), "PP": (0, 3), "PI": (0, 0), "PQ": (0, 0)},

    # 13. ANALISTA DE PROCESSAMENTO
    ("ANALISTA DE PROCESSAMENTO", "BRASÍLIA / DF"): {"AC": (0, 6), "PCD": (0, 1), "PP": (0, 3), "PI": (0, 0), "PQ": (0, 0)},
    ("ANALISTA DE PROCESSAMENTO", "RIO DE JANEIRO / RJ"): {"AC": (0, 6), "PCD": (0, 1), "PP": (0, 3), "PI": (0, 0), "PQ": (0, 0)},
    ("ANALISTA DE PROCESSAMENTO", "SÃO PAULO / SP"): {"AC": (0, 6), "PCD": (0, 1), "PP": (0, 3), "PI": (0, 0), "PQ": (0, 0)},
}


def calcular_idade(nascimento_str):
    nasc = datetime.strptime(nascimento_str, "%d/%m/%Y").date()
    return DATA_PROVA.year - nasc.year - ((DATA_PROVA.month, DATA_PROVA.day) < (nasc.month, nasc.day))


def classificar(df):
    # Aplica regras de eliminação
    df["eliminado_nota"] = df["prova_objetiva"] < NOTA_MINIMA_TOTAL
    # Não temos notas por disciplina, então não é possível verificar o critério de não zerar disciplina
    df["eliminado"] = df["eliminado_nota"]
    df["idade"] = df["nascimento"].apply(calcular_idade)
    df["idade_60_mais"] = df["idade"] >= 60

    # Apenas aprovados participam da classificação
    df_aprovados = df[~df["eliminado"]].copy()

    # Converte nascimento para datetime para ordenação correta por idade
    df_aprovados["nascimento_dt"] = pd.to_datetime(df_aprovados["nascimento"], format="%d/%m/%Y", errors="coerce")

    # Colunas de classificação
    for sistema in ["AC", "PCD", "PP"]:
        df_aprovados[f"classificacao_{sistema}"] = None
        df_aprovados[f"situacao_{sistema}"] = None

    grupos = df_aprovados.groupby(["perfil", "localidade"])

    for (perfil, localidade), grupo in grupos:
        # Ordenação com critérios de desempate aplicáveis:
        # 1. nota final decrescente
        # 2. idade >= 60 (True antes de False) - critério a
        # 3. conhecimentos específicos decrescente - critério b
        # 4. data de nascimento crescente (mais velho primeiro) - critério f
        grupo_ordenado = grupo.sort_values(
            by=["prova_objetiva", "idade_60_mais", "conhecimentos_especificos", "nascimento_dt"],
            ascending=[False, False, False, True]
        )

        # Classificação AC: todos os aprovados
        classificar_grupo(df_aprovados, grupo_ordenado, "AC")

        # Classificação PCD: apenas candidatos com pcd=True
        pcd_group = grupo_ordenado[grupo_ordenado["pcd"]].copy()
        classificar_grupo(df_aprovados, pcd_group, "PCD")

        # Classificação PP (Pessoa Preta ou Parda): apenas candidatos com negro=True
        pp_group = grupo_ordenado[grupo_ordenado["negro"]].copy()
        classificar_grupo(df_aprovados, pp_group, "PP")

    return df_aprovados


def classificar_grupo(df_aprovados, grupo, sistema):
    if grupo.empty:
        return
    perfil = grupo["perfil"].iloc[0]
    localidade = grupo["localidade"].iloc[0]
    vagas = VAGAS.get((perfil, localidade), {}).get(sistema, (0, 0))
    imediatas, reserva = vagas
    total_classificados = imediatas + reserva

    for idx, (i, row) in enumerate(grupo.iterrows(), start=1):
        df_aprovados.loc[i, f"classificacao_{sistema}"] = idx
        if idx <= imediatas:
            df_aprovados.loc[i, f"situacao_{sistema}"] = "Vaga Imediata"
        elif idx <= total_classificados:
            df_aprovados.loc[i, f"situacao_{sistema}"] = "Cadastro de Reserva"
        else:
            df_aprovados.loc[i, f"situacao_{sistema}"] = "Não Classificado"


if __name__ == "__main__":
    df = pd.read_csv("resultado_parsed.csv")
    print(f"Total de candidatos: {len(df)}")

    df_classificado = classificar(df)

    # Preenche sistemas não elegíveis
    for sistema, cond in [("PCD", ~df_classificado["pcd"]), ("PP", ~df_classificado["negro"])]:
        df_classificado.loc[cond, f"classificacao_{sistema}"] = None
        df_classificado.loc[cond, f"situacao_{sistema}"] = "Não elegível"

    # Junta com os eliminados
    df_eliminados = df[df["eliminado"]].copy()
    for col in ["classificacao_AC", "classificacao_PCD", "classificacao_PP",
                "situacao_AC", "situacao_PCD", "situacao_PP"]:
        df_eliminados[col] = "Eliminado"
    df_final = pd.concat([df_classificado, df_eliminados], ignore_index=True)

    # Converte nascimento para datetime também no df_final
    df_final["nascimento_dt"] = pd.to_datetime(df_final["nascimento"], format="%d/%m/%Y", errors="coerce")

    # Ordena por perfil, localidade, nota final
    df_final = df_final.sort_values(
        by=["perfil", "localidade", "prova_objetiva", "idade_60_mais", "conhecimentos_especificos", "nascimento_dt"],
        ascending=[True, True, False, False, False, True]
    )

    df_final.to_excel("classificacao_final.xlsx", index=False)
    print("Arquivo classificacao_final.xlsx gerado.")

    # Resumo
    print("\nResumo de aprovados/eliminados:")
    print(df_final["eliminado"].value_counts())

    print("\nResumo por sistema (classificados em vagas imediatas + cadastro de reserva):")
    for sistema in ["AC", "PCD", "PP"]:
        col = f"situacao_{sistema}"
        print(f"\n{sistema}:")
        print(df_final[col].value_counts(dropna=False))
