# Aula 05 — Laboratório de DVC

Notebook executado e projeto Git + DVC para versionamento do dataset Wine.

## Entrega

- [Notebook preenchido e executado](Aula%2005%20-%20DVC%20-%20Lab.ipynb), com todas as fases e respostas de reflexão.
- [PDF de conferência e entrega](Aula%2005%20-%20DVC%20-%20Conferencia%20e%20Entrega.pdf), com os links e o checklist da atividade.
- `data/wine.csv.dvc`: ponteiro para o dataset Wine; os commits `data: wine.csv v1` e `data: wine.csv v2` registram 178 e 130 amostras.
- `dvc.yaml` e `dvc.lock`: stages `preparar` e `treinar`, parâmetros, hashes e saídas.
- `artifacts/metrics.json`: métricas da última execução.

## Como executar o notebook

Instale Git, Python e as dependências:

```bash
python -m pip install dvc scikit-learn pandas numpy pyyaml joblib jupyter
```

Abra o notebook **na raiz deste repositório** e execute as células em ordem. Ele cria os repositórios de demonstração `demo_iris/` e `workspace_wine/` como pastas locais ignoradas pelo Git. Não execute o notebook a partir da pasta pai do clone se o clone também se chamar `workspace_wine`, pois a primeira célula da Fase 3 recria essa pasta.

## Projeto DVC na raiz

O remote `local_remote` aponta para `remote_storage/`, uma pasta local ignorada pelo Git, conforme a proposta do laboratório. Para que um clone também consiga recuperar os dados, os nove objetos DVC estão em uma [release do projeto](https://github.com/Rafaela091/aula-05-dvc-lab/releases/tag/dvc-cache-v1). O script verifica o SHA-256 do arquivo antes de restaurar o remote local:

```bash
python scripts/restore_remote.py
dvc pull
dvc repro
dvc metrics show
```

Com isso, o clone recupera `data/wine.csv`, os dados preparados e o modelo correspondentes ao `dvc.lock` da revisão atual. O histórico Git mantém v1, v2, o primeiro pipeline e o experimento com `n_estimators` alterado de 100 para 200. Nos dois experimentos, `accuracy` e `f1_macro` ficaram em 1,0; por isso `dvc metrics diff HEAD~1` não mostra diferença.
