import xml.etree.ElementTree as ET
import pickle

# Парсинг словаря
tree = ET.parse("dict.opcorpora_0_82.xml")  # Место
root = tree.getroot()

lemma_wordform_pairs = []

# Соберем пары лемма-словоформа
for lemma in root.find("lemmata").iter("lemma"):
    lemma_id = lemma.get("id")
    lemma_text = lemma.find("l").get("t")
    for wordform in lemma.iter("f"):
        wordform_text = wordform.get("t")
        lemma_wordform_pairs.append((lemma_text, wordform_text))  # Use lemma_text instead of lemma_id

# сохраним пары в файл.pkl
with open("lemma_wordform_pair.pkl", "wb") as pickle_file:
    pickle.dump(lemma_wordform_pairs, pickle_file)

print("Extracted and saved lemma-wordform pairs.")