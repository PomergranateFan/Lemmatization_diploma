import pickle

def calculate_K(file1, file2):
    '''
    :param file1: файл, содержащий частотную информацию о правилах
    :param file2: файл с множеством правил
    :return: Yule's K - инвариантный отностительно размера коэффициент
    '''

    with open(file1, 'rb') as f:
        f_x_data = pickle.load(f)

    with open(file2, 'rb') as f:
        tree_set = pickle.load(f)

    sum_x = 0
    N = len(tree_set)

    for x, info in f_x_data.items():
        f_x = info['f_x']
        sum_x += f_x * ((x / N) ** 2)

    K = (-1 / N + sum_x)
    return K

# Создание словаря с результатами
corpora_dict = {}


corpora_files = {
    'SynTagRus': ('syntagrus_f_x_dict.pkl', 'tree_set_SynTagRus_corpus.pkl'),
    'poetry': ('poetry_f_x_dict.pkl', 'tree_set_poetry_corpus.pkl'),
    'taiga': ('taiga_f_x_dict.pkl', 'tree_set_taiga_corpus.pkl'),
    'gsd': ('gsd_f_x_dict.pkl', 'tree_set_gsd_corpus.pkl'),
    'pud': ('pud_f_x_dict.pkl', 'tree_set_pud_corpus.pkl'),
    'OpenCorpora': ('OpenCorpora_f_x_dict.pkl', 'tree_set_OpenCorpora_corpus.pkl')
}

for corpus, files in corpora_files.items():
    K = calculate_K(files[0], files[1])
    corpora_dict[corpus] = {'любая_другая_мера': 1, 'K': K}

print(corpora_dict)