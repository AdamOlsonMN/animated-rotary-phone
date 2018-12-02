# Essentials: Data Cleansing and ETL
## Load Packages
import pandas as pd
import numpy as np

# Read And Parse Data
df = pd.read_csv("./dat/plays.csv")

## Pick Vars for Analysis
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

## Remove special teams plays and missing
plays = plays[
    plays.PlayType.notna()
    & (plays.PlayType != "No Play")
    & (plays.PlayType != "Kickoff")
    & (plays.PlayType != "Extra Point")
]
plays = plays.rename(columns={"posteam": "Team"})
