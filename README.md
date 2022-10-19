## Fazer no cmd

```sh
# Criar env
python -m venv nome_da_env

# Ativar env
.\venv\Scripts\activate.bat

# Instalar depedências do projeto
pip install -r requirements.txt

# Setar o flask
set FLASK_APP=api.py

# Rodar as migrations
flask db init
flask db migrate
flask db upgrade
```
