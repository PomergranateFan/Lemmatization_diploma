from LemmaWordformProcessor_class import LemmaWordformProcessor
from Visualization_class import VisualizationProcessor

processor = LemmaWordformProcessor()

###################################################
visualization_processor = VisualizationProcessor(processor, 'tree_set_SynTagRus_corpus.pkl',
                                                  'pairs_SynTagRus_corpus_not_unique.pkl', 'syntagrus_f_x_dict.pkl')

# visualization_processor.build_dictionary()
visualization_processor.visualize()

####################################################

visualization_processor_poetry = VisualizationProcessor(processor, 'tree_set_poetry_corpus.pkl',
                                                  'pairs_poetry_corpus_not_unique.pkl', 'poetry_f_x_dict.pkl')

visualization_processor_poetry.visualize()

####################################################

visualization_processor_taiga = VisualizationProcessor(processor, 'tree_set_taiga_corpus.pkl',
                                                  'pairs_taiga_corpus_not_unique.pkl', 'taiga_f_x_dict.pkl')

visualization_processor_taiga.visualize()

####################################################

visualization_processor_gsd = VisualizationProcessor(processor, 'tree_set_gsd_corpus.pkl',
                                                  'pairs_gsd_corpus_not_unique.pkl', 'gsd_f_x_dict.pkl')

visualization_processor_gsd.visualize()

####################################################

visualization_processor_pud = VisualizationProcessor(processor, 'tree_set_pud_corpus.pkl',
                                                  'pairs_pud_corpus_not_unique.pkl', 'pud_f_x_dict.pkl')

visualization_processor_pud.visualize()

####################################################

visualization_processor_OpenCorpora = VisualizationProcessor(processor, 'tree_set_OpenCorpora_corpus.pkl',
                                                  'pairs_OpenCorpora_corpus_not_unique.pkl', 'OpenCorpora_f_x_dict.pkl')

visualization_processor_OpenCorpora.visualize()


