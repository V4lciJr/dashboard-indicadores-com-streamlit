# 📊 WebApp de Análise de Dados com Streamlit e Autenticação de Usuários 🔐

Este projeto é uma aplicação interativa desenvolvida com **Streamlit**, que permite:

- 🔐 Login seguro com autenticação de usuários
- 🛂 Controle de acesso baseado em perfil (Admin ou Comum)
- 🗂️ Integração com banco de dados via SQLAlchemy
- 📊 Visualização de dados em dashboards dinâmicos
- 🧭 Navegação entre múltiplas páginas com interface intuitiva

---

## 🚀 Tecnologias Utilizadas

- 🐍 Python 3.11+
- 📦 Streamlit
- 🔐 streamlit-authenticator
- 🗃️ SQLAlchemy
- 🧮 SQLite (ou outro banco relacional à sua escolha)

---

## ⚙️ Funcionalidades

### ✅ Autenticação de Usuários
- Sistema de login com validação de email e senha.
- Geração de cookies de sessão.
- Mensagens dinâmicas de erro caso o login falhe.
- Permissão especial para usuários do tipo **admin**.

### 👥 Controle de Acesso
- Usuários comuns acessam somente as páginas de visualização.
- Admins acessam também páginas de gerenciamento, como **criação de contas**.

### 📊 Dashboards Interativos
- Visualização de indicadores e gráficos com dados atualizados.
- Navegação entre dashboards e relatórios por meio de um menu lateral.

### 🧭 Navegação por Páginas
- Interface com `st.navigation()` permitindo múltiplas páginas:
  - `Home`
  - `Dashboards` (Dash’s + Indicadores)
  - `Conta` (Criar conta / Logout)

---

## 🗃️ Estrutura do Projeto

```

📁 projeto/
├── models.py               # Definição do modelo Usuario com SQLAlchemy
├── homepage.py             # Página inicial da aplicação
├── dashboard.py            # Página com gráficos e análises
├── indicadores.py          # Página com KPIs e métricas
├── criar\_conta.py          # Tela de criação de conta (admin)
├── main.py                 # Arquivo principal com autenticação e navegação
└── README.md               # Documentação do projeto

````

---

## 🧪 Como Rodar Localmente

1. **Clone o repositório**:
```bash
git clone https://github.com/seuusuario/seurepositorio.git
cd seurepositorio
````

2. **Crie e ative o ambiente virtual** (opcional):

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. **Instale as dependências**:

```bash
pip install -r requirements.txt
```

4. **Execute a aplicação**:

```bash
streamlit run main.py
```

---

## 🔐 Exemplo de Dados de Usuário

A tabela `Usuario` inclui os seguintes campos:

* `id`: ID do usuário
* `nome`: Nome completo
* `email`: Email (usado para login)
* `senha`: Hash da senha
* `admin`: Booleano para indicar se é administrador

> ⚠️ As senhas devem ser armazenadas com hash seguro! Use o `stauth.Hasher` para isso.

---

## 🛠️ Customização

Você pode facilmente:

* Alterar o banco de dados (PostgreSQL, MySQL etc.)
* Adicionar páginas com novos dashboards
* Integrar APIs externas para alimentar os dados

---

## 🤝 Contribuições

Contribuições são super bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

## 🧑‍💻 Autor

Desenvolvido por [Valci Júnior](https://www.linkedin.com/in/valci-junior/) 🧠

---

## 📜 Licença

Este projeto está licenciado sob a **MIT License**. Foi desenvolvido junto o curso de Pyhton Impressionador da [Hashtag Treinamentos](https://www.hashtagtreinamentos.com/).

---

## 🌐 Demonstração

> Assim que o deploy da aplicação for realizado, colocarei o link aqui
---

✨ **Obrigado por visitar este repositório! Que a análise de dados esteja com você!** 📈💡
