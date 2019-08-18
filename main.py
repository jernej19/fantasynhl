import pandas as pd
from flask import Flask, render_template, request

import cgi

app = Flask(__name__)

# Import CSV files
goalie = pd.read_csv('goalies_predictions_1.csv')
players = pd.read_csv('players_predictions_1.csv')
# scoring = players[['name', 'assists', 'goals', 'ppa', 'ppg', 'shots on goal', 'shp']]
# misc = players[['PIM', 'blocks', 'hits', 'fow']]

# Ranking players
players['fow'] = players['fow'] / 30
players['hits'] = players['hits'] / 7.5
players['blocks'] = players['blocks'] / 4
players['assists'] = players['assists'] / 2
players['shots on goal'] = players['shots on goal'] / 7
players['PIM'] = players['PIM'] / 4.5
goalie['saves'] = goalie['saves'] / 36
goalie['save%'] = goalie['save%'] * 50
goalie['wins'] = goalie['wins'] / 2
goalie['goals against average'] = goalie['goals against average'] * (-1)
goalie['goals against'] = goalie['goals against'] / 3
# Models:
# 1 - scoring + misc
# 2 - scoring + goalie
# 3 - misc + goalies
# 4 - scoring + misc + goalieGS --> NEEDS TO BE DEFINED!!!!!!!!!!!!!

######## DEFINE MODEL SELECTED!!!!!!!#################
######################################################
# variable = 'krneki'
#
# if "a" in model_selected:
#     players['goals'] *= 2.5
# if "b" in model_selected:
#     players['assists'] *= 2.5
# if "c" in model_selected:
#     players['ppa'] *= 2.5
# if "d" in model_selected:
#     players['ppg'] *= 2.5
# if "e" in model_selected:
#     players['shots on goal'] *= 2.5
# if "f" in model_selected:
#     players['PIM'] *= 2.5
# if "g" in model_selected:
#     players['blocks'] *= 2.5
# if "h" in model_selected:
#     players['hits'] *= 2.5
# if "i" in model_selected:
#     players['fow'] *= 2.5
# if "j" in model_selected:
#     goalie['save%'] *= 2.5
# if "k" in model_selected:
#     goalie['goals against average'] *= 2.5
# if "l" in model_selected:
#     goalie['wins'] *= 2.5
# if "m" in model_selected:
#     goalie['saves'] *= 2.5
# if "2" in model_selected:
#     players['assists'] *= 2.5
    # elif category == str(2):
    #     players['assists'] *= 2.5
    # elif category == str(3):
    #     players['ppa'] *= 2.5
    # elif category == str(4):
    #     players['ppg'] *= 2.5
    # elif category == str(5):
    #     players['shots on goal'] *= 2.5
    # elif category == str(6):
    #     players['PIM'] *= 2.5
    # elif category == str(7):
    #     players['blocks'] *= 2.5
    # elif category == str(8):
    #     players['hits'] *= 2.5
    # elif category == str(9):
    #     players['fow'] *= 2.5
    # elif category == str(10):
    #     goalie['save%'] *= 2.5
    # elif category == str(11):
    #     goalie['goals against average'] *= 2.5
    # elif category == str(12):
    #     goalie['wins'] *= 2.5
    # elif category == str(13):
    #     goalie['saves'] *= 2.5
    # elif category == 14:
    #     players['assists'] *=2
    # elif category == 15:
    #     players['assists'] *=2
    # elif category == 16:
    #     players['assists'] *=2
    # elif category == 17:
    #     players['assists'] *=2
    # elif category == 18:
    #     players['assists'] *=2

# if model_selected == str(1):
#     players[['assists', 'goals', 'ppa', 'ppg', 'shots on goal', 'shp']] *= 1.5
#     players[['PIM', 'blocks', 'hits', 'fow']] = players[['PIM', 'blocks', 'hits', 'fow']] * 1.5

    # rank = players.sum(axis=1)
    # print(rank)
    # players['rank'] = rank
    # players['rank'] = players.sum(axis=1)
    # goalie['rank'] = goalie.sum(axis=1)
# players['rank'] = players.sum(axis=1)
# goalie['rank'] = goalie.sum(axis=1)
#     # players.to_csv('testin.csv')
# df = pd.concat([players, goalie], sort=False)
# df.to_html()
#
# elif model_selected == str(2):
#     players[['assists', 'goals', 'ppa', 'ppg', 'shots on goal', 'shp']] *= 1.5
#     goalie[['save%', 'goals against average', 'saves', 'shutouts', 'wins']] *= 1.5
#     players['rank'] = players.drop('name', axis=1).sum(axis=1)
#     goalie['rank'] = goalie.drop('name', axis=1).sum(axis=1)
#     df = pd.concat([players, goalie])
#     df.to_csv('test_final_predictions.csv', index=False)
#
# elif model_selected == str(3):
#     goalie[['save%', 'goals against average', 'saves', 'shutouts', 'wins']] *= 1.5
#     players[['PIM', 'blocks', 'hits', 'fow']] = players[['PIM', 'blocks', 'hits', 'fow']] * 1.5
#     players['rank'] = players.drop('name', axis=1).sum(axis=1)
#     goalie['rank'] = goalie.drop('name', axis=1).sum(axis=1)
#     df = pd.concat([players, goalie])
#     df.to_csv('test_final_predictions.csv', index=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        model_selected = request.form['model_selected']
        if "a" in model_selected:
            players['goals'] *= 2.5
        if "b" in model_selected:
            players['assists'] *= 2.5
        if "c" in model_selected:
            players['ppa'] *= 2.5
        if "d" in model_selected:
            players['ppg'] *= 2.5
        if "e" in model_selected:
            players['shots on goal'] *= 2.5
        if "f" in model_selected:
            players['PIM'] *= 2.5
        if "g" in model_selected:
            players['blocks'] *= 2.5
        if "h" in model_selected:
            players['hits'] *= 2.5
        if "i" in model_selected:
            players['fow'] *= 2.5
        if "j" in model_selected:
            goalie['save%'] *= 2.5
        if "k" in model_selected:
            goalie['goals against average'] *= 2.5
        if "l" in model_selected:
            goalie['wins'] *= 2.5
        if "m" in model_selected:
            goalie['saves'] *= 2.5
        players['rank'] = players.sum(axis=1)
        goalie['rank'] = goalie.sum(axis=1)
        df = pd.concat([players, goalie], sort=False)
        df = df.sort_values(by='rank', ascending=False)
        df = df[['name']]
        return render_template('result.html', tables=[df.to_html(index=False)], titles=df.columns.values)

if __name__ == '__main__':
    app.run()