import argparse
import spacy
import pandas as pd


def tratar_texto(serie: pd.Series) -> pd.Series:
    serie_tratada = serie.str.replace(r'\s+', ' ', regex=True).str.strip()
    return serie_tratada


def encontrar_entidade(doc, idx):
    ls_temp = [doc[idx].text]
    for termo in doc[idx+1:]:
        if termo.ent_iob_ != "I":
            break
        ls_temp.append(termo.text)
    return " ".join(ls_temp)


def anonimizar(txt, nlp):
    # Tratamento dos números
    txt = "".join(["1" if char.isnumeric() else char for char in txt])

    # Tratamento das entidades
    doc = nlp(txt)

    dic_per = dict()
    dic_loc = dict()
    dic_org = dict()
    dic_misc = dict()

    idx_per = 0
    idx_loc = 0
    idx_org = 0
    idx_misc = 0

    ls_termo = []
    for i in range(len(doc)):
        termo = doc[i]
        if termo.ent_type_ == "":
            ls_termo.append(termo.text)
        elif (termo.ent_type_ == 'PER') & (termo.ent_iob_ == 'B'):
            entidade = encontrar_entidade(doc, i)
            if entidade not in dic_per:
                idx_per += 1
                dic_per[entidade] = idx_per
            ls_termo.append('*[PER_' + str(dic_per[entidade])+"]*")

        elif (termo.ent_type_ == 'LOC') & (termo.ent_iob_ == 'B'):
            entidade = encontrar_entidade(doc, i)
            if entidade not in dic_loc:
                idx_loc += 1
                dic_loc[entidade] = idx_loc
            ls_termo.append('*[LOC_' + str(dic_loc[entidade])+"]*")

        elif (termo.ent_type_ == 'ORG') & (termo.ent_iob_ == 'B'):
            entidade = encontrar_entidade(doc, i)
            if entidade not in dic_org:
                idx_org += 1
                dic_org[entidade] = idx_org
            ls_termo.append('*[ORG_' + str(dic_org[entidade])+"]*")

        elif (termo.ent_type_ == 'MISC') & (termo.ent_iob_ == 'B'):
            entidade = encontrar_entidade(doc, i)
            if entidade not in dic_misc:
                idx_misc += 1
                dic_misc[entidade] = idx_misc
            ls_termo.append('*[MISC_' + str(dic_misc[entidade])+"]*")

    return " ".join(ls_termo)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Anonimiza entidades de um arquivo CSV.')
    parser.add_argument('-i', dest="input", metavar='input', type=str, help='path do arquivo de entrada')
    parser.add_argument('-o', dest="output", metavar='output', type=str, help='path do arquivo de saída')
    parser.add_argument('-c', dest="colunas", metavar='colunas', type=str, help='lista de atributos que serão anonimizados')
    args = parser.parse_args()

    path_input = args.input
    path_output = args.output
    colunas = args.colunas

    nlp = spacy.load("pt_core_news_lg", disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"])

    df = pd.read_csv(path_input)

    colunas = colunas.split()

    for coluna in colunas:
        df[coluna] = df[coluna].astype(str)
        df[coluna] = tratar_texto(df[coluna])
        df[coluna] = df[coluna].apply(lambda x: anonimizar(x, nlp))

    df.to_csv(path_output, sep=";", index=False)
