# NER-Anonymization-pt_br

Este repositório contém um modelo em Python que permite anonimizar dados textuais não estruturados em arquivos CSV.

### Instalando e executando o modelo

Este projeto inclui um arquivo Pipfile e um arquivo Pipfile.lock, para a gestão de dependências via Pipenv. Para instalar e executar o projeto, siga os passos abaixo:

1. Clone o repositório:
```bash
git clone https://github.com/RafaelBaSantos/NER-Anonymization-pt_br
```

2. Navegue até o diretório do projeto:
```bash
cd NER-Anonymization-pt_br
```

3. Instale o Pipenv:
```bash
pip install pipenv
```

4. Instale as dependências do projeto:
```bash
pipenv install
```
Este comando instalará todas as dependências necessárias em uma virtual environment do Pipenv.

5. Ative a virtual environment:
```bash
pipenv shell
```

6. Baixe o modelo do spaCy em português:
```bash
python -m spacy download pt_core_news_lg
```

7. Execute o arquivo main.py:
```bash
python main.py -i <caminho_do_input> -o <caminho_do_output> -c <colunas>
```

### Configurações:
- -i: input (caminho do arquivo .csv que será tratado)
- -o: output (caminho onde será salvo o arquivo .csv tratado)
- -c: colunas (atributos que serão anonimizados, separados por espaço)

Com estas instruções, será possível instalar e executar o projeto. Em caso de dúvidas ou sugestões, sinta-se à vontade para abrir uma issue no Github.
