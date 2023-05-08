# NER-Anonymization-pt_br

Anonimiza dados textuais não estruturados de um arquivo CSV.

### Instalação via Pipenv

Esse projeto inclue um Pipfile e um Pipfile.lock, para a gestão de dependencias via Pipenv.

1. Clone o repositório
```bash
git clone https://github.com/RafaelBaSantos/NER-Anonymization-pt_br
```

2. Navegue até o diretório do projeto
```bash
cd NER-Anonymization-pt_br
```

3. Instale o Pipenv
```bash
pip install pipenv
```

4. Install os packages
```bash
pipenv install
```
Isso vai instalar todos os pacotes requeridos em uma virtual enviroment do Pipenv.

5. Ative a virtual env
```bash
pipenv shell
```

6. Baixe o modelo do spacy em português
```bash
python -m spacy download pt_core_news_lg
```

7. Execute o modelo
```bash
python -m spacy download pt_core_news_lg
```

Execute o arquivo main.py
```bash
python main.py -i <caminho_do_input> -o <caminho_do_outut> -c <colunas>
```

### Configurações:
- -i: input (caminho do arquivo .csv que será tratado)
- -o: output (caminho onde será salvo o arquivo .csv tratado)
- -c: colunas  (atributos que serão anonimizados, separados por espaço)
