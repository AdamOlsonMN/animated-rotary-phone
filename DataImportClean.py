# Essentials: Data Cleansing and ETL
import pandas as pd

import numpy as np

df = pd.read_csv('./plays.csv')
# add in team here
plays = ['Date','GameID','qtr','time','yrdline100','PlayType','FieldGoalResult','FieldGoalDistance','posteam','DefensiveTeam','PosTeamScore','DefTeamScore','Season']
plays = df[plays]
# https://www.kaggle.com/gnarlyinsights/nfl-analysis-predicting-play-type