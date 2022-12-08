# Achados e Perdidos - API

### Instalando o projeto

#### Clonar o projeto
`git clone https://github.com/eduardobdamacena/achados-perdidos-backend`

#### Instalar dependências
`pip install -r requirements.txt`

#### Alterar as configurações do BD no arquivo `settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_bd',
        'HOST': 'host_do_bd',
        'PORT': 'porta_bd',
        'USER': 'usuario_bd',
        'PASSWORD': 'senha_bd'
    }
}
```

#### Migrar o banco de dados
`python manage.py migrate`

#### Iniciar o servidor
`python manage.py runserver`