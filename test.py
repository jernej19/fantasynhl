import pandas as pd
import numpy as np

#  Import data to dataframe
players = pd.read_csv('players.csv')
goalies = pd.read_csv('goalies.csv')

# Remove unnecessary columns:
players = players.drop(columns=['adjusted_assists',
'adjusted_goals',
'adjusted_goals_against_average',
'adjusted_goals_created',
'adjusted_points',
'corsi_against',
'corsi_for',
'corsi_for_percentage',
'defensive_point_shares',
'defensive_zone_start_percentage',
'even_strength_assists',
'even_strength_goals',
'even_strength_goals_allowed',
'even_strength_save_percentage',
'even_strength_shots_faced',
'fenwick_against',
'fenwick_for',
'fenwick_for_percentage',
'giveaways',
'goal_against_percentage_relative',
'goalie_point_shares',
'goals_against_on_ice',
'goals_created',
'goals_for_on_ice',
'goals_saved_above_average',
'height',
'league',
'minutes',
'offensive_point_shares',
'offensive_zone_start_percentage',
'pdo',
'point_shares',
'power_play_goals_against_on_ice',
'power_play_goals_allowed',
'power_play_goals_for_on_ice',
'power_play_save_percentage',
'power_play_shots_faced',
'quality_start_percentage',
'relative_corsi_for_percentage',
'relative_fenwick_for_percentage',
'save_percentage_on_ice',
'shooting_percentage_on_ice',
'shootout_attempts',
'shootout_goals',
'shootout_misses',
'shootout_percentage',
'short_handed_goals_allowed',
'short_handed_save_percentage',
'short_handed_shots_faced',
'shots_against',
'takeaways',
'ties_plus_overtime_loss',
'time_on_ice_even_strength',
'total_goals_against_on_ice',
'total_goals_for_on_ice',
'weight',
'faceoff_losses',
'faceoff_percentage',
'wins',
'total_shots',
'shutouts',
'quality_starts',
'really_bad_starts',
'save_percentage',
'saves',
'losses',
'goals_against_average',
'goals_against',
])

goalies = goalies.drop(columns=['adjusted_assists',
'adjusted_goals',
'adjusted_goals_against_average',
'adjusted_goals_created',
'adjusted_points',
'corsi_against',
'corsi_for',
'corsi_for_percentage',
'defensive_point_shares',
'defensive_zone_start_percentage',
'even_strength_assists',
'even_strength_goals',
'even_strength_goals_allowed',
'even_strength_save_percentage',
'even_strength_shots_faced',
'fenwick_against',
'fenwick_for',
'fenwick_for_percentage',
'giveaways',
'goal_against_percentage_relative',
'goalie_point_shares',
'goals_against_on_ice',
'goals_created',
'goals_for_on_ice',
'goals_saved_above_average',
'height',
'league',
'minutes',
'offensive_point_shares',
'offensive_zone_start_percentage',
'pdo',
'point_shares',
'power_play_goals_against_on_ice',
'power_play_goals_allowed',
'power_play_goals_for_on_ice',
'power_play_save_percentage',
'power_play_shots_faced',
'quality_start_percentage',
'relative_corsi_for_percentage',
'relative_fenwick_for_percentage',
'save_percentage_on_ice',
'shooting_percentage_on_ice',
'shootout_attempts',
'shootout_goals',
'shootout_misses',
'shootout_percentage',
'short_handed_goals_allowed',
'short_handed_save_percentage',
'short_handed_shots_faced',
'shots_against',
'takeaways',
'ties_plus_overtime_loss',
'time_on_ice_even_strength',
'total_goals_against_on_ice',
'total_goals_for_on_ice',
'weight',
'faceoff_losses',
'faceoff_percentage',
'assists',
'average_time_on_ice',
'blocks_at_even_strength',
'faceoff_wins',
'game_winning_goals',
'games_played',
'goals',
'hits_at_even_strength',
'penalties_in_minutes',
'plus_minus',
'points',
'power_play_assists',
'power_play_goals',
'shooting_percentage',
'short_handed_assists',
'short_handed_goals',
'shots_on_goal'
])

players = players.fillna(0)
goalies = goalies.fillna(0)

# Replace season values
s = players['season'].isin(['Career', 'season'])
players.loc[~s, 'season'] = players.groupby(s.ne(s.shift()).cumsum()).cumcount() + 1
l = goalies['season'].isin(['Career', 'season'])
goalies.loc[~l, 'season'] = goalies.groupby(l.ne(s.shift()).cumsum()).cumcount() + 1

# Drop Career and season rows
players.drop(players[players['season'] == 'Career'].index, inplace=True)
players.drop(players[players['season'] == 'season'].index, inplace=True)
goalies.drop(goalies[goalies['season'] == 'Career'].index, inplace=True)
goalies.drop(goalies[goalies['season'] == 'season'].index, inplace=True)

# Change column values to ints
changes_players = ['assists',
       'blocks_at_even_strength', 'faceoff_wins', 'game_winning_goals',
       'goals', 'hits_at_even_strength',
       'penalties_in_minutes', 'plus_minus', 'points',
       'power_play_assists', 'power_play_goals',
       'short_handed_assists', 'short_handed_goals',
       'shots_on_goal', 'games_played', 'season']

changes_goalies = ['losses',
       'quality_starts', 'really_bad_starts',
       'saves', 'shutouts',
       'time_on_ice', 'total_shots', 'wins']

for integer in changes_players:
    players[integer] = pd.to_numeric(players[integer])

for integer in changes_goalies:
    goalies[integer] = pd.to_numeric(goalies[integer])


####################### TEST ENVIRONMENT ################################
test = pd.DataFrame()
test['goals/game'] = players['goals']/(players['games_played'])
test['points/game'] = players['points']/(players['games_played'])
test['shots/game'] = players['shots_on_goal']/(players['games_played'])
test['gwg'] = players['game_winning_goals']/(players['games_played'])
test['assists'] = players['assists']/(players['games_played'])
test['ppa'] = players['power_play_assists']/(players['games_played'])
test['ppg'] = players['power_play_goals']/(players['games_played'])
test['shp'] = (players['short_handed_assists']+players['short_handed_goals'])/(players['games_played'])
test['season'] = players['season']
# test['shooting%'] = players['shooting_percentage']
test['plus_minus'] = players['plus_minus']
test['name'] = players['name']
test['hits'] = players['hits_at_even_strength']/(players['games_played'])
test['blocks'] = players['blocks_at_even_strength']/(players['games_played'])
test['PIM'] = players['penalties_in_minutes']/(players['games_played'])
# test['TOI'] = players['average_time_on_ice']
# test['FO%'] = players['faceoff_percentage']
test['FOW'] = players['faceoff_wins']/(players['games_played'])
test['games_played'] = players['games_played']
# For loop to predict all players
selected_players = [player for player in test['name']]
selected_players = list(set(selected_players))

player_prediction = pd.DataFrame()
player_prediction_1 = pd.DataFrame()

for selected_player in selected_players:
    ovechkin = test.loc[test.name == selected_player]
    shots = ovechkin['shots/game']
    goals = ovechkin['goals/game']
    ppa = ovechkin['ppa']
    ppg = ovechkin['ppg']
    a = ovechkin['assists']
    # sh_per = ovechkin['shooting%']
    shp = ovechkin['shp']
    fow = ovechkin['FOW']
    hits = ovechkin['hits']
    blocks = ovechkin['blocks']
    pim = ovechkin['PIM']
    plusMinus = ovechkin['plus_minus']
    season = ovechkin['season']
    games_played = ovechkin['games_played']
    ovechkin_1 = ovechkin.drop(['name'], 1)

    ####################################################################
    if len(ovechkin_1['season']) > 2:
        weights = season
        weights.loc[:] = 0.5
        weights[-2:] = 7
        shots_avg = np.average(shots, weights=weights)
        goals_avg = np.average(goals, weights=weights)
        ppa_avg = np.average(ppa, weights=weights)
        ppg_avg = np.average(ppg, weights=weights)
        shp_avg = np.average(shp, weights=weights)
        assists_avg = np.average(a, weights=weights)
        fow_avg = np.average(fow, weights=weights)
        hits_avg = np.average(hits, weights=weights)
        blocks_avg = np.average(blocks, weights=weights)
        pim_avg = np.average(pim, weights=weights)
        plusMinus_avg = np.average(plusMinus, weights=weights)
        player_prediction = player_prediction.append(
            pd.DataFrame({'name': [selected_player], 'shots on goal': [shots_avg * 82],
                          'ppa': [ppa_avg * 82],
                          'goals': [goals_avg*82],
                          'ppg': [ppg_avg * 82],
                          # 'shooting%': [sh_per.mean()],
                          'shp': [shp_avg * 82],
                          'assists': [assists_avg * 82],
                          'fow': [fow_avg * 82],
                          'hits': [hits_avg * 82],
                          'blocks': [blocks_avg * 82],
                          'plus/minus': [plusMinus_avg],
                          'PIM': [pim_avg * 82]}))

for selected_player in selected_players:
    ovechkin = test.loc[test.name == selected_player]
    shots = ovechkin['shots/game']
    goals = ovechkin['goals/game']
    ppa = ovechkin['ppa']
    ppg = ovechkin['ppg']
    a = ovechkin['assists']
    # sh_per = ovechkin['shooting%']
    shp = ovechkin['shp']
    fow = ovechkin['FOW']
    hits = ovechkin['hits']
    blocks = ovechkin['blocks']
    pim = ovechkin['PIM']
    plusMinus = ovechkin['plus_minus']
    season = ovechkin['season']
    games_played = ovechkin['games_played']
    ovechkin_1 = ovechkin.drop(['name'], 1)

    if len(ovechkin_1['season']) <= 2:
        ######### TEST NUMBER 1.05, CHANGE WHEN IT'S CALCULATED!!!!!!! ##########
        player_prediction_1 = player_prediction_1.append(
            pd.DataFrame({'name': [selected_player], 'shots on goal': [(shots.mean() * 1.05) * 82],
                          'ppa': [(ppa.mean() * 1.05) * 82],
                          'goals': [(goals.mean() * 1.05) * 82],
                          'ppg': [(ppg.mean() * 1.05) * 82],
                          # 'shooting%': [sh_per.mean()],
                          'shp': [(shp.mean() * 1.05) * 82],
                          'assists': [(a.mean() * 1.05) * 82],
                          'fow': [(fow.mean()*1.05)*82],
                          'hits': [(hits.mean() * 1.05) * 82],
                          'blocks': [(blocks.mean() * 1.05) * 82],
                          'plus/minus': [plusMinus.mean() * 1.05],
                          'PIM': [(pim.mean() * 1.05) * 82]}))

df = pd.concat([player_prediction, player_prediction_1], sort=False)

df.to_csv('players_predictions_1.csv', index=False)

#################################################
# GOALIE PREDICTIONS
#################################################

# goalies_test = pd.DataFrame()
# goalies_test['starts'] = goalies['goals']/(players['games_played']) ########### GOALIE STARTS MISSING!!!!!!!!!!!!!!!!!!
goalies_test['wins'] = goalies['wins'].astype(int)
goalies_test['ga'] = goalies['goals_against'].astype(int)
goalies_test['ga'] = goalies_test['ga'].astype(int)
goalies_test['gaa'] = goalies['goals_against_average']
goalies_test['gaa'] = goalies_test['gaa'].astype(float)
goalies_test['sv'] = goalies['saves'].astype(int)
goalies_test['sv%'] = goalies['save_percentage'].astype(float)
goalies_test['sho'] = goalies['shutouts'].astype(int)
goalies_test['age'] = goalies['age']
goalies_test['name'] = goalies['name']
goalies_test['season'] = goalies['season']

selected_goalies = [player for player in goalies_test['name']]
selected_goalies = list(set(selected_goalies))
test_5 = pd.DataFrame()
for selected_goalie in selected_goalies:
    price = goalies_test.loc[goalies_test.name == selected_goalie]
    wins = price['wins']
    ga = price['ga']
    gaa = price['gaa']
    sv = price['sv']
    sv_per = price['sv%']
    sho = price['sho']
    season = price['season']
    price_1 = price.drop(['name'],1)

    if len(price_1['season']) <= 2:
    ######### TEST NUMBER 1.05, CHANGE WHEN IT'S CALCULATED!!!!!!! ##########
        test_5 = test_5.append(pd.DataFrame({'name': [selected_goalie], 'wins': [wins.mean()],
                                                                   'goals against': [ga.mean()],
                                                                   'goals against average': [gaa.mean()],
                                                                   'saves': [sv.mean()],
                                                                   'save%': [sv_per.mean()],
                                                                   'shutouts': [sho.mean()]}))
    ####################################################################
    else:
        weights = season
        weights.loc[:] = 0.5
        weights[-2:] = 5
        wins_avg = np.average(wins, weights=weights)
        ga_avg = np.average(ga, weights=weights)
        gaa_avg = np.average(gaa, weights=weights)
        saves_avg = np.average(sv, weights=weights)
        so_avg = np.average(sho, weights=weights)
        svPer_avg = np.average(sv_per, weights=weights)
        test_5 = test_5.append(pd.DataFrame({'name': [selected_goalie], 'wins': [wins_avg],
                                                                   'goals against': [ga_avg],
                                                                   'goals against average': [gaa_avg],
                                                                   'saves': [saves_avg],
                                                                   'save%': [svPer_avg],
                                                                   'shutouts': [so_avg]}))
test_5.to_csv('goalies_predictions_1.csv', index=False)
