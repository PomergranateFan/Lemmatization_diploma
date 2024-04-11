from pathlib import Path

# Словарь с ключами имя корпуса. В значениях лежит словарь с ключами corpus, pairs, tree, dict

config = {
    'SynTagRus':           {"corpus": Path("data/SynTagRus/corpus"),
                            "pairs" : Path("data/SynTagRus/pairs_SynTagRus_corpus_not_unique.pkl"),
                            "trees": Path("data/SynTagRus/tree_set_SynTagRus_corpus.pkl"),
                            "dict": Path("data/SynTagRus/syntagrus_f_x_dict.pkl")},
    'poetry':              {"corpus": Path("data/poetry/corpus"),
                            "pairs" : Path("data/poetry/pairs_poetry_corpus_not_unique.pkl"),
                            "trees": Path("data/poetry/tree_set_poetry_corpus.pkl"),
                            "dict": Path("data/poetry/poetry_f_x_dict.pkl")},
    'taiga':               {"corpus": Path("data/taiga/corpus"),
                            "pairs" : Path("data/taiga/pairs_taiga_corpus_not_unique.pkl"),
                            "trees": Path("data/taiga/tree_set_taiga_corpus.pkl"),
                            "dict": Path("data/taiga/taiga_f_x_dict.pkl")},
    'gsd':                 {"corpus": Path("data/gsd/corpus"),
                            "pairs" : Path("data/gsd/pairs_gsd_corpus_not_unique.pkl"),
                            "trees": Path("data/gsd/tree_set_gsd_corpus.pkl"),
                            "dict": Path("data/gsd/gsd_f_x_dict.pkl")},
    'pud':                 {"corpus": Path("data/pud/corpus"),
                            "pairs" : Path("data/pud/pairs_pud_corpus_not_unique.pkl"),
                            "trees": Path("data/pud/tree_set_pud_corpus.pkl"),
                            "dict": Path("data/pud/pud_f_x_dict.pkl")},
    'OpenCorpora':         {"corpus": Path("data/OpenCorpora/corpus"),
                            "pairs" : Path("data/OpenCorpora/pairs_OpenCorpora_corpus_not_unique.pkl"),
                            "trees": Path("data/OpenCorpora/tree_set_OpenCorpora_corpus.pkl"),
                            "dict": Path("data/OpenCorpora/OpenCorpora_f_x_dict.pkl")},
    'SynTagRus_original': {"corpus": None,
                            "pairs" : Path("data/SynTagRus_original/pairs_SynTagRus_original_corpus_not_unique.pkl"),
                            "trees": Path("data/SynTagRus_original/tree_set_SynTagRus_original_corpus.pkl"),
                            "dict": Path("data/SynTagRus_original/syntagrus_original_f_x_dict.pkl")},
    'RNC':                {"corpus": None,
                            "pairs" : Path("data/RNC/pairs_RNC_main_corpus_not_unique.pkl"),
                            "trees": Path("data/RNC/tree_set_RNC_main_corpus.pkl"),
                            "dict": Path("RNC_main_f_x_dict.pkl")}
}