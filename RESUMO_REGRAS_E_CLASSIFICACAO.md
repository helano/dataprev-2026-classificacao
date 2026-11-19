# Resumo: Regras do Edital e Classificação dos Candidatos

## 1. Fontes
- **Edital:** `29.10-edital-2-retificacao-dataprev.pdf`
- **Resultado da Prova Objetiva:** `18.11-dataprev2026-resultado-prova-objetiva.pdf`

## 2. Regras de Eliminação / Reprovação na Prova Objetiva

Conforme o **subitem 9.17** do edital, será considerado aprovado na Prova Objetiva o candidato que, **cumulativamente**:

1. **Obtiver, no mínimo, 57,5 pontos** na prova objetiva; e
2. **Não zerar nenhuma disciplina**.

O candidato que não atender a esses requisitos será eliminado do concurso.

### Observação sobre os dados
O PDF de resultado da prova objetiva divulgado contém **apenas candidatos aprovados**. Todos os 19.874 registros extraídos possuem nota final igual ou superior a 57,5 pontos. O critério de "não zerar nenhuma disciplina" não pôde ser verificado automaticamente porque o resultado divulgado traz apenas as notas agregadas dos módulos:
- Conhecimentos Gerais (máximo 40 pontos)
- Conhecimentos Específicos (máximo 75 pontos)

## 3. Estrutura da Prova Objetiva

A prova possui **70 questões**, com pontuação máxima de **115 pontos**:

| Módulo | Disciplina | Questões | Peso | Pontuação Máxima |
|--------|-----------|----------|------|------------------|
| **Conhecimentos Gerais** | Língua Portuguesa | 12 | 1 | 12 |
| | Língua Inglesa | 12 | 1 | 12 |
| | Raciocínio Lógico Matemático | 5 | 1 | 5 |
| | Atualidades e Inteligência Artificial | 6 | 1 | 6 |
| | Legislação Acerca de Segurança da Informação e Proteção de Dados | 5 | 1 | 5 |
| | **Total** | **40** | | **40** |
| **Conhecimentos Específicos** | Conhecimentos Específicos | 30 | 2,5 | 75 |
| | **Total** | **30** | | **75** |

## 4. Classificação

A Nota Final é a nota obtida na Prova Objetiva. Os candidatos aprovados são ordenados por nota final decrescente, por sistema de ingresso.

### Sistemas de Ingresso
- **AC**: Ampla Concorrência
- **PCD**: Pessoa com Deficiência
- **PP**: Pessoa Preta ou Parda
- **PI**: Pessoa Indígena
- **PQ**: Pessoa Quilombola

A classificação em cada sistema respeita as vagas imediatas e o cadastro de reserva previstos no edital para cada cargo/perfil e localidade.

## 5. Critérios de Desempate

Conforme o **subitem 12.1**, em caso de empate, terá preferência o candidato que:

1. Tiver idade igual ou superior a 60 anos;
2. Obtiver a maior nota no Módulo de Conhecimentos Específicos;
3. Obtiver a maior nota na disciplina de Língua Portuguesa;
4. Obtiver a maior nota na disciplina de Língua Inglesa;
5. Tiver exercido efetivamente a função de jurado;
6. For o candidato mais velho.

### Aplicação nos dados disponíveis
Foram aplicados os critérios 1, 2 e 6, pois os dados disponíveis no PDF de resultados não incluem notas individuais por disciplina nem informação sobre exercício de jurado.

## 6. Observações Importantes

- Candidatos negros/indígenas/quilombolas e/ou com deficiência concorrem simultaneamente à vaga reservada e à vaga de ampla concorrência.
- De acordo com o item 11.6 do edital, se um candidato classificado em lista reservada for convocado para uma vaga de ampla concorrência, ele **não será considerado** para o preenchimento das vagas reservadas.
- Não foi possível classificar candidatos nos sistemas **PI** (Pessoa Indígena) e **PQ** (Pessoa Quilombola) porque o PDF de resultados não traz essas informações individualmente.

## 7. Arquivos Gerados

- `resultado_parsed.csv`: dados extraídos do PDF de resultados em formato tabular.
- `classificacao_final.xlsx`: classificação de todos os candidatos com colunas para AC, PCD e PP.
- `resumo_classificacao.xlsx`: resumo por perfil/localidade com quantidade de classificados em cada sistema.
- `classificar_candidatos.py`: script Python utilizado para processar os dados e aplicar as regras.

## 8. Resumo Geral da Classificação

| Sistema | Vagas Imediatas | Cadastro de Reserva | Não Classificado | Não Elegível |
|---------|----------------|---------------------|------------------|--------------|
| AC | 133 | 1.019 | 18.722 | - |
| PCD | 20 | 94 | 894 | 18.866 |
| PP | 55 | 407 | 3.387 | 16.025 |
