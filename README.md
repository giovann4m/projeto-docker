<<<<<<< HEAD
=======
#🐳Projeto Docker

Este projeto contém um backend simples em Flask rodando em um contêiner Docker e um banco de dados PostgreSQL 
gerenciado pelo Docker Compose.

#📌 Pré-requisitos
Antes de começar, certifique-se de ter instalado:
- Docker Desktop e Docker Compose
- Python
- Git

Para verificar se estão instalados, execute os seguintes comandos:

```
docker --version
docker compose version ou docker-compose version (para a versão mais antiga do Docker)
python --version
git --version
```

#🚀 Como rodar o projeto

1. Clone o repositório:

   ```
   git clone https://github.com/giovann4m/projeto-docker.git
   cd projeto-docker
   ```
   
3. Suba os contêineres com Docker Compose:
   ```
   docker compose up ou docker-compose up (para a versão mais antiga do Docker)
   ```
4. Acesse o backend:
   - [http://localhost:5000]
   - Teste a conexão com o banco: [http://localhost:5000/db-test]

#📂 Estrutura do Projeto

```
projeto-dcoker/
   backend/
      app.py            #Código principal da API Flask
      database.py       #Configuração da conexão com o banco de dados     
      Dockerfile        #Configuração do container do backend
      requirements.txt  #Dependências do projeto
docker-compose.yml      #Orquestração dos containers
README.md               #Documentação do Projeto
.venv/                  #Ambiente virtual

```

#⚠️ Possíveis Problemas e Soluções

Erro: "Port 5000 already in use"
Causa: Outra aplicação já está rodando na porta 5000.
Solução:
```
sudo lsof -i :5000   #Verifique qual processo está usando a porta 5000
sudo kill -9 <PID>   #Substituir <PID> pelo número do processo listado
```
Ou, altere a porta no arquivo `docker-compose.yml`:
```yml
ports:
  - "5001:5000"  #Mude a porta externa para 5001
```

#Erro: "Cannot connect to the Docker daemon"
Causa: O Docker pode não estar rodando.
Solução:
- Verifique se o Docker Desktop está aberto.
- No Linux, tente iniciar o Docker com:
  ```
  sudo systemctl start docker
  ```

#Erro: "Database connection failed" ao acessar `http://localhost:5000/db-test`
Causa: O backend pode estar tentando conectar ao banco antes que ele esteja pronto.
Solução:
- Derrube e suba os contêineres novamente:
  ```
  docker compose down && docker compose up --build
  ```
- Verifique os logs do banco:
  ```
  docker compose logs db
  ```

#Erro: "User identity unknown" no Git
Causa: O Git não tem seu usuário configurado.
Solução:
```
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@example.com"
```

#📌 Envio para o Docker Hub
Para enviar sua imagem Docker ao Docker Hub:

1. Faça login no Docker Hub:
   ```
   docker login
   ```
2. Crie a imagem Docker:
   ```
   docker build -t seu-usuario/nome-da-imagem .
   ```
3. Envie para o Docker Hub:
   ```
   docker push seu-usuario/nome-da-imagem
   ```
4. Copie o link da imagem e envie conforme solicitado:
   ```
   https://hub.docker.com/r/seu-usuario/nome-da-imagem
   ```

✉️ Caso tenha dúvidas ou encontre novos problemas, consulte os logs do Docker com:
```
docker compose logs
```
>>>>>>> 3cc1471 (Primeira versão do projeto)
