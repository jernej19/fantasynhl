import pandas as pd
from flask import Flask, render_template, request
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

# Import CSV files
goalie = pd.read_csv('goalies_predictions_1.csv')
players = pd.read_csv('players_predictions_1.csv')
goalie['goals against average'] = goalie['goals against average'] * (-1)
goalie['goals against'] = goalie['goals against'] * (-1)
scaler = MinMaxScaler()
scaled_values1 = scaler.fit_transform(players.drop(['name'], axis=1))
scaled_values = scaler.fit_transform(goalie.drop(['name'], axis=1))
players.loc[:, players.columns != 'name'] = scaled_values1
goalie.loc[:, goalie.columns != 'name'] = scaled_values

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        # model_selected = request.form['model_selected']
        if request.form.get('a'):
            players['goals'] *= 4.5
        if request.form.get('b'):
            players['assists'] *= 4.5
        if request.form.get('c'):
            players['ppa'] *= 4.5
        if request.form.get('d'):
            players['ppg'] *= 4.5
        if request.form.get('e'):
            players['shots on goal'] *= 4.5
        if request.form.get('f'):
            players['PIM'] *= 4.5
        if request.form.get('g'):
            players['blocks'] *= 4.5
        if request.form.get('h'):
            players['hits'] *= 4.5
        if request.form.get('i'):
            players['fow'] *= 4.5
        if request.form.get('j'):
            goalie['save%'] *= 4.5
        if request.form.get('k'):
            goalie['goals against average'] *= 4.5
        if request.form.get('l'):
            goalie['wins'] *= 4.5
        if request.form.get('m'):
            goalie['saves'] *= 4.5
        if request.form.get('n'):
            goalie['shutouts'] *= 4.5
        players['rank'] = players.sum(axis=1)
        goalie['rank'] = goalie.sum(axis=1)
        df = pd.concat([players, goalie], sort=False)
        df = df.sort_values(by='rank', ascending=False)
        # df = df[['name']]
        return render_template('result.html', tables=[df.to_html(index=False)], titles=df.columns.values)

if __name__ == '__main__':
    app.run()