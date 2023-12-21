import pickle
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load data
with open('str_f_x_correct.pkl', 'rb') as f:
    data1 = pickle.load(f)

with open('str_f_x_potential.pkl', 'rb') as f:
    data2 = pickle.load(f)

with open('str_f_x_lemmas.pkl', 'rb') as f:
    data3 = pickle.load(f)

with open('corpora_f_x_correct.pkl', 'rb') as f:
    data4 = pickle.load(f)

with open('corpora_f_x_potential.pkl', 'rb') as f:
    data5 = pickle.load(f)

with open('corpora_f_x_lemmas.pkl', 'rb') as f:
    data6 = pickle.load(f)

with open('corpora_corpus_f_x_correct.pkl', 'rb') as f:
    data7 = pickle.load(f)

with open('corpora_corpus_f_x_potential.pkl', 'rb') as f:
    data8 = pickle.load(f)

with open('corpora_corpus_f_x_lemmas.pkl', 'rb') as f:
    data9 = pickle.load(f)

with open('uni_f_x_correct.pkl', 'rb') as f:
    data10 = pickle.load(f)

with open('uni_f_x_potential.pkl', 'rb') as f:
    data11 = pickle.load(f)

with open('uni_f_x_lemmas.pkl', 'rb') as f:
    data12 = pickle.load(f)


# Create subplots
fig = make_subplots(rows=4, cols=3, subplot_titles=[
    '# деревьев корректно строят лемму x раз',
    '# деревьев потенциально строят лемму x раз',
    '# деревьев строят конкретную лемму x раз'
], shared_xaxes=True, shared_yaxes=True)

for i, data in enumerate([data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12], start=1):
    row = (i - 1) // 3 + 1
    col = (i - 1) % 3 + 1

    if i < 4:
        graph = "SynTagRus Corpus"
    elif i < 7:
        graph = "Opencorpora"
    elif i < 10:
        graph = "Opencorpora Corpus"
    else:
        graph = "Unimorph"

    fig.add_trace(go.Scatter(
        x=list(data.keys()),
        y=list(data.values()),
        mode='markers',
        name=graph,
    ), row=row, col=col)

    # Set logarithmic scale for both x and y axes
    fig.update_xaxes(type='log', range=[0, 6], row=row, col=col)
    fig.update_yaxes(type='log', range=[0, 3], row=row, col=col)

fig.show()