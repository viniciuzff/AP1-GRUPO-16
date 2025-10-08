# 🏫 API de Gestão Escolar — Flask + SQLite + SQLAlchemy + Docker

# INTEGRANTES
MURILO LUIZ INÁCIO DE SOUZA – RA 2400933 
TULIO DA SILVA COSTA – RA 2302336 
VINICIUS FERREIRA DE FREITAS – RA 2403865

## 📘 Descrição
API REST construída com **Flask**, estruturada no padrão **MVC**, para o **gerenciamento de Professores, Turmas e Alunos**.  
A aplicação permite realizar operações CRUD completas e documentadas com **Swagger**, com persistência de dados em **SQLite** e containerização via **Docker**.

---

## 🧩 Funcionalidades

### 👨‍🏫 Professores
- Criar, listar, atualizar e excluir professores  
- Campos: `id`, `nome`, `idade`, `materia`, `observacoes`

### 🏫 Turmas
- Criar, listar, atualizar e excluir turmas  
- Cada turma pertence a um professor  
- Campos: `id`, `descricao`, `professor_id`, `ativo`

### 👨‍🎓 Alunos
- Criar, listar, atualizar e excluir alunos  
- Cada aluno pertence a uma turma  
- Campos: `id`, `nome`, `idade`, `turma_id`, `data_nascimento`, `nota_primeiro_semestre`, `nota_segundo_semestre`, `media_final`

---

## ⚙️ Tecnologias Utilizadas
- Python 3.x  
- Flask  
- Flask SQLAlchemy  
- Flask-RESTx (Swagger UI)  
- SQLite  
- Docker  

---

## 🧱 Estrutura do Projeto

