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

# Get average results for offensive plays by game for model
# to preserve the dataframe's shape (with GameID being unique), I'm going to use a split-apply-merge strategy

# Split - from origional DF: Get 2 DF's for plays that are labeled Run or Pass
r_off_agg = df[(df.PlayType == "Run")]
p_off_agg = df[(df.PlayType == "Pass") | (df.PlayType == "Sack")]

# Apply - groupby aggregation to find the Median yards by game, team, PlayType, and qtr
r_off_agg = (
    r_off_agg.groupby(["GameID", "qtr", "posteam"])["Yards.Gained"].mean().reset_index()
)
p_off_agg = (
    p_off_agg.groupby(["GameID", "qtr", "posteam"])["Yards.Gained"].mean().reset_index()
)
