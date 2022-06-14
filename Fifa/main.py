#importing the pandas and matplotlib for ease of use
import pandas as pd
import matplotlib.pyplot as plot
#reading file
player_data = pd.read_csv('players_20.csv')
#create german player list
german_players = player_data.loc[player_data['nationality'] == 'Germany']
#creates Real Madrid player list
rm_players = player_data.loc[player_data['club'] == 'Real Madrid']

#number 1:
#Uses head() function to display top 5 players in list
def display_top_5(player_data):
    play = player_data.head()
    return play.to_string(index=False)

#uses columns.values to display list of columns
def see_columns(player_data):
    col = player_data.columns.values
    return col


def num_rows_columns(player_data):
    rows = len(player_data)
    cols = len(player_data.columns)
    values = ("Rows: " + str(rows) + " Columns: " + str(cols))
    return values


def players_countries(player_data):
    nats_value = player_data['nationality'].value_counts()
    return nats_value


def top10_countries(player_data):
    top10_nats = player_data['nationality'].value_counts().nlargest(10)
    return top10_nats


def bar_plot_top5(player_data):
    top5_nation = player_data['nationality'].value_counts().nlargest(5).plot(kind='bar', color='green')
    plot.title("Top 5 Countries ")
    plot.tight_layout()
    plot.show()


def top5_player(player_data):
    top5 = player_data[['short_name', 'wage_eur']].head()
    return top5.to_string(justify='center', index=False)


def top5_earners(player_data):
    topEarner = player_data[['short_name', 'wage_eur']].sort_values(by='wage_eur', ascending=False).head()
    return topEarner.to_string(justify='center', index=False)


def bar_plot_top5_earn(player_data):
    top5_earners = player_data[['short_name', 'wage_eur']].sort_values(by='wage_eur', ascending=False).head()
    top5_earners.plot(x='short_name', y='wage_eur', kind='bar', color='green')
    plot.title("Top 5 wage earners")
    plot.tight_layout()
    plot.show()


def top10_Germany(german_players):
    top10_ger_outcomes = german_players[['short_name', 'nationality', 'overall']].sort_values(by='overall',
                                                                                              ascending=False) \
        .nlargest(10, 'overall')
    return top10_ger_outcomes.to_string(justify='center', index=False)


def top5_max_Germany(german_players):
    german_players_max = german_players[['short_name', 'nationality', 'height_cm', 'weight_kg', 'wage_eur']].sort_values \
        (by='height_cm', ascending=False).sort_values(by='weight_kg', ascending=False).sort_values(by="wage_eur",
                                                                                                   ascending=False) \
        .head()
    german_players_max = german_players_max.rename(columns={'short_name': 'Short Name', 'nationality': 'Nationality', \
                            'height_cm': 'Height in cm', 'weight_kg':'Weight in kg', 'wage_eur':'Euro Wages'})
    return german_players_max.to_string(justify='center', index=False)


def top5_shrt(german_players):
    german_players_5_earn = german_players[['short_name', 'wage_eur']].sort_values(by='wage_eur', ascending=False) \
        .head()
    german_players_5_earn=german_players_5_earn.rename(columns={'short_name':'Short Name', 'wage_eur': 'Euro Wages'})
    return german_players_5_earn.to_string(justify='center', index=False)


def top_5_ger_shoot(german_players):
    top5_ger_shoot = german_players[['short_name', 'shooting']].sort_values(by='shooting', ascending=False).nlargest\
        (5,'shooting')
    top5_ger_shoot = top5_ger_shoot.rename(columns={'short_name':'Short Name', 'shooting':'Shooting Record'})
    return top5_ger_shoot.to_string(justify='center', index=False)


def top5_defenders(player_data):
    top_defenders = player_data[['short_name', 'defending', 'nationality', 'club']].sort_values(by='defending',\
                                                                        ascending=False).nlargest(5, 'defending')
    top_defenders = top_defenders.rename(
        columns={'short_name': 'Short Name', 'defending': 'Defending', 'nationality': 'Nationality', 'club': 'Club'})
    return top_defenders.to_string(justify='center', index=False)


def top5_wage_RM(rm_players):
    top5_rm_wage = rm_players[['wage_eur']].sort_values(by='wage_eur', ascending=False).nlargest(5, 'wage_eur')
    top5_rm_wage = top5_rm_wage.rename(columns={'wage_eur': 'Real Madrid Top 5 Wage Earners'})
    return top5_rm_wage.to_string(justify='center', index=False)


def top5_shoot_RM(rm_players):
    top5_rm_shoot = rm_players[['shooting']].sort_values(by='shooting', ascending=True).nlargest(5, 'shooting')
    top5_rm_shoot = top5_rm_shoot.rename(columns={'shooting': 'Real Madrid Top 5 Shooters'})
    return top5_rm_shoot.to_string(justify='center', index=False)


def top5_defend_RM(rm_players):
    top5_rm_defend = rm_players[['defending']].sort_values(by='defending', ascending=True).nlargest(5, 'defending')
    top5_rm_defend = top5_rm_defend.rename(columns={'defending': 'Real Madrid Top 5 Defenders'})
    return top5_rm_defend.to_string(justify='center', index=False)


def top5_nat_RM(rm_players):
    top5_rm_nat = rm_players[['nationality']].head()
    top5_rm_nat = top5_rm_nat.rename(columns={'nationality': 'Real Madrid Top 5 Nationalities'})
    return top5_rm_nat.to_string(justify='center', index=False)


print("\nRequirements #1")
print(display_top_5(player_data))
print("\nRequirements #2")
print(see_columns(player_data))
print("\nRequirements #3")
print(num_rows_columns(player_data))
print("\nRequirements #4")
print(players_countries(player_data))
print("\nRequirements #5")
print(top10_countries(player_data))
print("\nRequirements #6")
bar_plot_top5(player_data)
print("\nRequirements #7")
print(top5_player(player_data))
print("\nRequirements #8")
print(top5_earners(player_data))
print("\nRequirements #9")
bar_plot_top5_earn(player_data)
print("\nRequirements #10")
print(top10_Germany(german_players))
print("\nRequirements #11")
print(top5_max_Germany(german_players))
print("\nRequirements #12")
print(top5_shrt(german_players))
print("\nRequirements #13")
print(top_5_ger_shoot(german_players))
print("\nRequirements #14")
print(top5_defenders(player_data))
print("\nRequirements #15")
print(top5_wage_RM(rm_players))
print("\nRequirements #16")
print(top5_shoot_RM(rm_players))
print("\nRequirements #17")
print(top5_defend_RM(rm_players))
print("\nRequirements #18")
print(top5_nat_RM(rm_players))
