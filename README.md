# Aula 05 — Laboratório de DVC

Notebook executado e projeto Git + DVC para versionamento do dataset Wine.

## Entrega

- [Notebook preenchido e executado](Aula%2005%20-%20DVC%20-%20Lab.ipynb), com todas as fases e respostas de reflexão.
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

O remote `local_remote` aponta para `remote_storage/`, uma pasta local ignorada pelo Git, conforme a proposta do laboratório. Portanto, o clone do GitHub contém os ponteiros, o pipeline, o lockfile, o código e as métricas, mas não contém os objetos do cache DVC. Para reconstruir a execução a partir do GitHub, execute o notebook na raiz do clone; ele gera um novo projeto completo em `workspace_wine/` e faz `dvc push` para o remote local desse projeto.

Os commits na raiz registram v1, v2, o primeiro pipeline e o experimento com `n_estimators` alterado de 100 para 200. Nos dois experimentos, `accuracy` e `f1_macro` ficaram em 1,0; por isso `dvc metrics diff HEAD~1` não mostra diferença.
