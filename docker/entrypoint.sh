#!/bin/bash

# Clonar o repositório do GitHub para /app/repo
git clone $REPO_URL /app/repo

# Criar o diretório de saída se não existir
mkdir -p /app/output

# Executar a ferramenta CK
java -jar /app/ck/target/ck-*-SNAPSHOT-jar-with-dependencies.jar \
    /app/repo \
    true \
    0 \
    true \
    /app/output

# Mover arquivos CSV para o diretório /app/output se eles não estiverem lá
mv /app/*.csv /app/output/

# Exibir arquivos de saída gerados
echo "Listando arquivos em /app/output:"
ls -l /app/output
