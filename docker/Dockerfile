# Dockerfile
FROM openjdk:17-slim

# Atualizar o índice de pacotes e instalar o Maven e o Git
RUN apt-get update && apt-get install -y maven git --fix-missing

# Definir o diretório de trabalho
WORKDIR /app

# Clonar a ferramenta CK do repositório GitHub
RUN git clone https://github.com/mauricioaniche/ck.git /app/ck

# Mudar para o diretório do CK
WORKDIR /app/ck

# Construir o projeto usando Maven
RUN mvn clean compile package

# Copiar o script de entrada para o container
COPY entrypoint.sh /app/ck/

# Tornar o script de entrada executável
RUN chmod +x /app/ck/entrypoint.sh

# Definir o script de entrada como ponto de entrada
ENTRYPOINT ["/app/ck/entrypoint.sh"]
