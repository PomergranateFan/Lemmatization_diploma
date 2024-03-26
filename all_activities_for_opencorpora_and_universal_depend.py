from LemmaWordformProcessor_class import LemmaWordformProcessor
from Visualization_class import VisualizationProcessor
from DictionaryProcessor_class import SynTagRusCorpus
from DictionaryProcessor_class import OpenCorporaCorpus

########################################################################################################################

# Спарсим пары лемма-словоформа из корпуса SynTagRus из Universal Dependencies и построим деревья для них
syntagrus = SynTagRusCorpus("syntagrus", "pairs_SynTagRus_corpus_not_unique.pkl", "tree_set_SynTagRus_corpus.pkl")
syntagrus.extract_lemma_wordform_pairs_not_unique()
syntagrus.build_trees()
syntagrus.save_tree_set()

# Построим словарь частотности с примерами деревьев и пар
processor_syntagrus = LemmaWordformProcessor()
visualization_processor = VisualizationProcessor(processor_syntagrus, 'tree_set_SynTagRus_corpus.pkl',
                                                  'pairs_SynTagRus_corpus_not_unique.pkl', 'syntagrus_f_x_dict.pkl')
visualization_processor.build_dictionary()

########################################################################################################################

# Спарсим пары лемма-словоформа из корпуса taiga из Universal Dependencies и построим деревья для них
taiga = SynTagRusCorpus("taiga", "pairs_taiga_corpus_not_unique.pkl", "tree_set_taiga_corpus.pkl")
taiga.extract_lemma_wordform_pairs_not_unique()
taiga.build_trees()
taiga.save_tree_set()

# Построим словарь частотности с примерами деревьев и пар
processor_taiga = LemmaWordformProcessor()
visualization_processor = VisualizationProcessor(processor_taiga, 'tree_set_taiga_corpus.pkl',
                                                  'pairs_taiga_corpus_not_unique.pkl', 'taiga_f_x_dict.pkl')
visualization_processor.build_dictionary()

########################################################################################################################

# Спарсим пары лемма-словоформа из корпуса poetry из Universal Dependencies и построим деревья для них
poetry = SynTagRusCorpus("poetry", "pairs_poetry_corpus_not_unique.pkl", "tree_set_poetry_corpus.pkl")
poetry.extract_lemma_wordform_pairs_not_unique()
poetry.build_trees()
poetry.save_tree_set()

# Построим словарь частотности с примерами деревьев и пар
processor_poetry = LemmaWordformProcessor()
visualization_processor = VisualizationProcessor(processor_poetry, 'tree_set_poetry_corpus.pkl',
                                                  'pairs_poetry_corpus_not_unique.pkl', 'poetry_f_x_dict.pkl')
visualization_processor.build_dictionary()

########################################################################################################################

# Спарсим пары лемма-словоформа из корпуса gsd из Universal Dependencies и построим деревья для них
gsd = SynTagRusCorpus("gsd", "pairs_gsd_corpus_not_unique.pkl", "tree_set_gsd_corpus.pkl")
gsd.extract_lemma_wordform_pairs_not_unique()
gsd.build_trees()
gsd.save_tree_set()

# Построим словарь частотности с примерами деревьев и пар
processor_gsd = LemmaWordformProcessor()
visualization_processor = VisualizationProcessor(processor_gsd, 'tree_set_gsd_corpus.pkl',
                                                  'pairs_gsd_corpus_not_unique.pkl', 'gsd_f_x_dict.pkl')
visualization_processor.build_dictionary()

########################################################################################################################

# Спарсим пары лемма-словоформа из корпуса pud из Universal Dependencies и построим деревья для них
pud = SynTagRusCorpus("pud", "pairs_pud_corpus_not_unique.pkl", "tree_set_pud_corpus.pkl")
pud.extract_lemma_wordform_pairs_not_unique()
pud.build_trees()
pud.save_tree_set()

# Построим словарь частотности с примерами деревьев и пар
processor_pud = LemmaWordformProcessor()
visualization_processor = VisualizationProcessor(processor_pud, 'tree_set_pud_corpus.pkl',
                                                  'pairs_pud_corpus_not_unique.pkl', 'pud_f_x_dict.pkl')
visualization_processor.build_dictionary()

########################################################################################################################
########################################################################################################################

# Спарсим пары лемма-словоформа из корпуса OpenCorpora и построим деревья для них
opencorporacorpus = OpenCorporaCorpus("annot.opcorpora.no_ambig.xml", "pairs_OpenCorpora_corpus_not_unique.pkl", "tree_set_OpenCorpora_corpus.pkl")
opencorporacorpus.extract_lemma_wordform_pairs_not_unique()
opencorporacorpus.build_trees()
opencorporacorpus.save_tree_set()

# Построим словарь частотности с примерами деревьев и пар
processor_OpenCorpora = LemmaWordformProcessor()
visualization_processor = VisualizationProcessor(processor_OpenCorpora, 'tree_set_OpenCorpora_corpus.pkl',
                                                  'pairs_OpenCorpora_corpus_not_unique.pkl', 'OpenCorpora_f_x_dict.pkl')

visualization_processor.build_dictionary()
