# Imagem base
FROM python:3.12-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependências
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos do projeto
COPY . .

# Expõe a porta padrão do Flask
EXPOSE 5000

# Comando para rodar o app
CMD ["python", "app.py"]
