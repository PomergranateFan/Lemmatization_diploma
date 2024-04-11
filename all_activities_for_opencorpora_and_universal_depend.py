from LemmaWordformProcessor_class import LemmaWordformProcessor
from Visualization_class import VisualizationProcessor
from DictionaryProcessor_class import SynTagRusCorpus
from DictionaryProcessor_class import OpenCorporaCorpus
from DictionaryProcessor_class import BaseDictionaryCorpus

'''
########################################################################################################################

# Спарсим пары лемма-словоформа из корпуса SynTagRus из Universal Dependencies и построим деревья для них
syntagrus = SynTagRusCorpus(config['SynTagRus']['corpus'], config['SynTagRus']['pairs'], config['SynTagRus']['trees'])
syntagrus.extract_lemma_wordform_pairs_not_unique()
syntagrus.build_trees()
syntagrus.save_tree_set()

# Построим словарь частотности с примерами деревьев и пар
processor_syntagrus = LemmaWordformProcessor()
visualization_processor = VisualizationProcessor(processor_syntagrus, config['SynTagRus']['trees'],
                                                  config['SynTagRus']['pairs'], config['SynTagRus']['dict'])
visualization_processor.build_dictionary()

########################################################################################################################

# Спарсим пары лемма-словоформа из корпуса taiga из Universal Dependencies и построим деревья для них
taiga = SynTagRusCorpus(config['taiga']['corpus'], config['taiga']['pairs'], config['taiga']['trees'])
taiga.extract_lemma_wordform_pairs_not_unique()
taiga.build_trees()
taiga.save_tree_set()

# Построим словарь частотности с примерами деревьев и пар
processor_taiga = LemmaWordformProcessor()
visualization_processor = VisualizationProcessor(processor_taiga, config['taiga']['trees'],
                                                  config['taiga']['pairs'], config['taiga']['dict'])
visualization_processor.build_dictionary()

########################################################################################################################

# Спарсим пары лемма-словоформа из корпуса poetry из Universal Dependencies и построим деревья для них
poetry = SynTagRusCorpus(config['poetry']['corpus'], config['poetry']['pairs'], config['poetry']['trees'])
poetry.extract_lemma_wordform_pairs_not_unique()
poetry.build_trees()
poetry.save_tree_set()

# Построим словарь частотности с примерами деревьев и пар
processor_poetry = LemmaWordformProcessor()
visualization_processor = VisualizationProcessor(processor_poetry, config['poetry']['trees'],
                                                  config['poetry']['pairs'], config['poetry']['dict'])
visualization_processor.build_dictionary()

########################################################################################################################

# Спарсим пары лемма-словоформа из корпуса gsd из Universal Dependencies и построим деревья для них
gsd = SynTagRusCorpus(config['gsd']['corpus'], config['gsd']['pairs'], config['gsd']['trees'])
gsd.extract_lemma_wordform_pairs_not_unique()
gsd.build_trees()
gsd.save_tree_set()

# Построим словарь частотности с примерами деревьев и пар
processor_gsd = LemmaWordformProcessor()
visualization_processor = VisualizationProcessor(processor_gsd, config['gsd']['trees'],
                                                  config['gsd']['pairs'], config['gsd']['dict'])
visualization_processor.build_dictionary()

########################################################################################################################

# Спарсим пары лемма-словоформа из корпуса pud из Universal Dependencies и построим деревья для них
pud = SynTagRusCorpus(config['pud']['corpus'], config['pud']['pairs'], config['pud']['trees'])
pud.extract_lemma_wordform_pairs_not_unique()
pud.build_trees()
pud.save_tree_set()

# Построим словарь частотности с примерами деревьев и пар
processor_pud = LemmaWordformProcessor()
visualization_processor = VisualizationProcessor(processor_pud, config['pud']['trees'],
                                                  config['pud']['pairs'], config['pud']['dict'])
visualization_processor.build_dictionary()

########################################################################################################################
########################################################################################################################

# Спарсим пары лемма-словоформа из корпуса OpenCorpora и построим деревья для них
opencorporacorpus = OpenCorporaCorpus(config['OpenCorpora']['corpus'], config['OpenCorpora']['pairs'], config['OpenCorpora']['trees'])
opencorporacorpus.extract_lemma_wordform_pairs_not_unique()
opencorporacorpus.build_trees()
opencorporacorpus.save_tree_set()

# Построим словарь частотности с примерами деревьев и пар
processor_OpenCorpora = LemmaWordformProcessor()
visualization_processor = VisualizationProcessor(processor_OpenCorpora, config['OpenCorpora']['tree'],
                                                  config['OpenCorpora']['pairs'], config['OpenCorpora']['dict'])

visualization_processor.build_dictionary()
'''
########################################################################################################################
########################################################################################################################
'''
# Построим деревья для пар из для последней версии оригинала СинТагРуса ~ 1.5 млн словоформ
syntagrus_original = BaseDictionaryCorpus(config['SynTagRus_original]['pairs'], config['SynTagRus_original]['trees'], config['SynTagRus_original]['corpus'])
# syntagrus_original.extract_lemma_wordform_pairs_not_unique()
syntagrus_original.build_trees()
syntagrus_original.save_tree_set()

# Построим словарь частотности с примерами деревьев и пар
processor_syntagrus_original = LemmaWordformProcessor()
visualization_processor = VisualizationProcessor(processor_syntagrus_original, config['SynTagRus_original]['trees'],
                                                  config['SynTagRus_original]['pairs'], config['SynTagRus_original]['dict'])
visualization_processor.build_dictionary()
'''

########################################################################################################################
########################################################################################################################


# Построим деревья для пар из для последней версии оригинала СинТагРуса ~ 1.5 млн словоформ
RNC_main_corpus = BaseDictionaryCorpus(config['RNC']['pairs'], config['RNC']['trees'], config['RNC']['corpus'])
# syntagrus_original.extract_lemma_wordform_pairs_not_unique()
RNC_main_corpus.build_trees()
RNC_main_corpus.save_tree_set()

# Построим словарь частотности с примерами деревьев и пар
processor_RNC_main_corpus = LemmaWordformProcessor()
visualization_processor = VisualizationProcessor(processor_RNC_main_corpus, config['RNC']['trees'],
                                                  config['RNC']['pairs'], config['RNC']['dict'])
visualization_processor.build_dictionary()
