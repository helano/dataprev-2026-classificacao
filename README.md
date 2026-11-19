# Dataprev 2026 — Classificação do Concurso Público

Este repositório contém a extração, tratamento e classificação dos candidatos aprovados na **Prova Objetiva** do **Concurso Público da Dataprev 2026**, com base no edital e no resultado oficial divulgado.

## 📁 Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `29.10-edital-2-retificacao-dataprev.pdf` | Edital do concurso (2ª retificação) |
| `18.11-dataprev2026-resultado-prova-objetiva.pdf` | Resultado oficial da Prova Objetiva |
| `resultado_parsed.csv` | Dados extraídos do PDF de resultados em formato tabular |
| `classificacao_final.xlsx` | Classificação dos candidatos por sistema de ingresso (AC, PCD, PP) |
| `resumo_classificacao.xlsx` | Resumo por cargo/perfil e localidade |
| `classificar_candidatos.py` | Script Python que executa a extração e classificação |
| `RESUMO_REGRAS_E_CLASSIFICACAO.md` | Documento com as regras do edital e resultado da classificação |

## ⚖️ Regras aplicadas

### Aprovação na Prova Objetiva
De acordo com o edital, é considerado aprovado o candidato que, **cumulativamente**:
1. Obtiver **no mínimo 57,5 pontos** na prova objetiva;
2. **Não zerar nenhuma disciplina**.

> **Nota:** o PDF de resultados divulgado contém apenas candidatos aprovados. Por isso, todos os registros processados já atendem ao critério mínimo de pontuação.

### Estrutura da prova
- **70 questões**, pontuação máxima de **115 pontos**
- **Conhecimentos Gerais**: 40 questões, peso 1 (máx. 40 pts)
- **Conhecimentos Específicos**: 30 questões, peso 2,5 (máx. 75 pts)

### Critérios de desempate
A classificação obedece, na ordem:
1. Idade igual ou superior a 60 anos;
2. Maior nota em Conhecimentos Específicos;
3. Maior nota em Língua Portuguesa;
4. Maior nota em Língua Inglesa;
5. Ter exercido função de jurado;
6. Candidato mais velho.

> Foram aplicados os critérios disponíveis nos dados do PDF: **idade ≥ 60 anos**, **nota em Conhecimentos Específicos** e **candidato mais velho**. Não foi possível aplicar os critérios 3, 4 e 5 porque o resultado divulgado não traz notas por disciplina nem informação sobre função de jurado.

### Sistemas de ingresso
- **AC**: Ampla Concorrência
- **PCD**: Pessoa com Deficiência
- **PP**: Pessoa Preta ou Parda

> Não foi possível classificar nos sistemas **PI** (Pessoa Indígena) e **PQ** (Pessoa Quilombola) porque essas informações não constam no PDF de resultados.

## 📊 Resultado geral

| Sistema | Vagas Imediatas | Cadastro de Reserva | Não Classificado | Não Elegível |
|---------|----------------|---------------------|------------------|--------------|
| AC | 133 | 1.019 | 18.722 | — |
| PCD | 20 | 94 | 894 | 18.866 |
| PP | 55 | 407 | 3.387 | 16.025 |

## 🚀 Como executar

```bash
# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install pdfplumber pandas openpyxl

# Executar a classificação
python3 classificar_candidatos.py
```

## ⚠️ Limitações

- O PDF de resultados não discrimina notas por disciplina individual (apenas os módulos agregados).
- Não há identificação de candidatos indígenas (PI) ou quilombolas (PQ) no resultado divulgado.
- A ordenação por idade exige que a data de nascimento seja tratada como tipo data, não como texto.

## 📌 Observação

Os dados aqui processados são de uso informativo e acadêmico. A classificação oficial e as convocações são de responsabilidade da **Dataprev** e da **FGV**.
