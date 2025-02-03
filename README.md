# Projeto Docker

Este projeto contém um backend simples em Flask rodando em um contêiner Docker e um banco de dados PostgreSQL gerenciado pelo Docker Compose.

## 📌 Pré-requisitos
Antes de começar, certifique-se de ter instalado:
- **Docker Desktop** e **Docker Compose**
- **Python**
- **Git**

Para verificar se estão instalados, execute os seguintes comandos:

docker --version
docker compose version
python --version
git --version

## 🚀 Como rodar o projeto

1. **Clone o repositório:**
   ````bash
   git clone https://github.com/giovann4m/projeto-docker.git <br>
   cd projeto-docker
   
3. **Suba os contêineres com Docker Compose:**
   ```bash
   docker compose up
   ```
4. **Acesse o backend:**
   - [http://localhost:5000](http://localhost:5000)
   - Teste a conexão com o banco: [http://localhost:5000/db-test](http://localhost:5000/db-test)

## 📂 Estrutura do Projeto

```
projeto-docker/
│── backend/
│   ├── app.py               # Código principal da API Flask
│   ├── database.py          # Configuração da conexão com o banco de dados
│   ├── Dockerfile           # Configuração do container do backend
│   ├── requirements.txt     # Dependências do projeto
│── docker-compose.yml       # Orquestração dos contêineres
│── README.md                # Documentação do projeto
│── .venv/                   # Ambiente virtual (se aplicável)
```

## ⚠️ Possíveis Problemas e Soluções

### 🔴 Erro: **"Port 5000 already in use"**
**Causa:** Outra aplicação já está rodando na porta 5000.
**Solução:**
```bash
sudo lsof -i :5000   # Verifique qual processo está usando a porta 5000
sudo kill -9 <PID>   # Substitua <PID> pelo número do processo listado
```
Ou, altere a porta no arquivo `docker-compose.yml`:
```yaml
ports:
  - "5001:5000"  # Mude a porta externa para 5001
```

### 🔴 Erro: **"Cannot connect to the Docker daemon"**
**Causa:** O Docker pode não estar rodando.
**Solução:**
- Verifique se o Docker Desktop está aberto.
- No Linux, tente iniciar o Docker com:
  ```bash
  sudo systemctl start docker
  ```

### 🔴 Erro: **"Database connection failed"** ao acessar `http://localhost:5000/db-test`
**Causa:** O backend pode estar tentando conectar ao banco antes que ele esteja pronto.
**Solução:**
- Derrube e suba os contêineres novamente:
  ```bash
  docker compose down && docker compose up --build
  ```
- Verifique os logs do banco:
  ```bash
  docker compose logs db
  ```

### 🔴 Erro: **"User identity unknown" no Git**
**Causa:** O Git não tem seu usuário configurado.
**Solução:**
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@example.com"
```

### 🔴 Erro: **"Updates were rejected because the remote contains work that you do not have locally"**
**Causa:** O repositório remoto tem alterações que você ainda não baixou.
**Solução:**
```bash
git pull origin main --rebase
git push origin main
```
Se necessário, force o push:
```bash
git push --force origin main
```

## 📌 Envio para o Docker Hub
Para enviar sua imagem Docker ao Docker Hub:

1. **Faça login no Docker Hub:**
   ```bash
   docker login
   ```
2. **Crie a imagem Docker:**
   ```bash
   docker build -t seu-usuario/nome-da-imagem .
   ```
3. **Envie para o Docker Hub:**
   ```bash
   docker push seu-usuario/nome-da-imagem
   ```
4. **Copie o link da imagem** e envie conforme solicitado:
   ```
   https://hub.docker.com/r/seu-usuario/nome-da-imagem
   ```

---
✉️ **Caso tenha dúvidas ou encontre novos problemas, consulte os logs do Docker com:**
```bash
docker compose logs
```

