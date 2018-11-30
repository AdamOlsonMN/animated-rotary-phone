# Essentials: Data Cleansing and ETL
import pandas as pd

import numpy as np

df = pd.read_csv("./plays.csv")
# add in team here
play_attr = [
    "GameID",
    "qtr",
    "TimeSecs",
    "yrdline100",
    "ydstogo",
    "Drive",
    "down",
    "PlayType",
    "PassAttempt",
    "RushAttempt",
    "Yards.Gained",
    "posteam",
    "DefensiveTeam",
    "PosTeamScore",
    "DefTeamScore",
    "Season",
]
plays = df[play_attr]

plays = plays[
    plays.PlayType.notna()
    & (plays.PlayType != "No Play")
    & (plays.PlayType != "Kickoff")
    & (plays.PlayType != "Extra Point")
]
plays = plays.rename(columns={"posteam": "Team"})
