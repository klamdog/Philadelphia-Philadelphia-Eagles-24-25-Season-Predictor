# PHILADELPHIA EALGES Record Prediction Season 2024/25
# Written by Klamdog - July 2024 -

import random
import time

# Teams
Cowboys_name = "DALLAS COWBOYS"
Cowboys_rank = 10
Cowboys_chance = 32 - Cowboys_rank
Commanders_name = "WASHINGTON COMMMANDERS"
Commanders_rank = 28
Commanders_chance = 32 - Commanders_rank
Giants_name = "NEW YORK GIANTS"
Giants_rank = 30
Giants_chance = 32 - Giants_rank
Eagles_name = "PHILADELPHIA EAGLES"
Eagles_rank = 6
Eagles_chance = 32 - Eagles_rank
Ravens_name = "BALTIMORE RAVENS"
Ravens_rank = 4
Ravens_chance = 32 - Ravens_rank
Patriots_name = "NEW ENGLAND PATRIOTS"
Patriots_rank = 29
Patriots_chance = 32 - Patriots_rank
Vikings_name = "MINNISOTA VIKINGS"
Vikings_rank = 22
Vikings_chance = 32 - Vikings_rank
Packers_name = "GREEN BAY PACKERS"
Packers_rank = 9
Packers_chance = 32 - Packers_rank
Falcons_name = "ATLANTA FALCONS"
Falcons_rank = 14
Falcons_chance = 32 - Falcons_rank
Saints_name = "NEW ORELEANS SAINTS"
Saints_rank = 24
Saints_chance = 32 - Saints_rank
Bucks_name = "TAMPA BAY BUCCANEERS"
Bucks_rank = 23
Bucks_chance = 32 - Bucks_rank
Browns_name = "CLEVELAND BROWNS"
Browns_rank = 13
Browns_chance = 32 - Browns_rank
Bengals_name = "CINCINNATI BENGALS"
Bengals_rank = 5
Bengals_chance = 32 - Bengals_rank
Jaguars_name = "JACKSONVILLE JAGUARS"
Jaguars_rank = 19
Jaguars_chance = 32 - Jaguars_rank
Rams_name = "LOS ANGELES RAMS"
Rams_rank = 16
Rams_chance = 32 - Rams_rank
Panthers_name = "CAROLINA PANTHERS"
Panthers_rank = 32
Panthers_chance = 32 - Panthers_rank
Steelers_name = "PITTSBURGH STEELERS"
Steelers_rank = 17
Steelers_chance = 32 - Steelers_rank

# Wins and Losses

Eagles_wins = 0
Eagles_losses = 0
print("")
print('|-<|SEASON 2024/25//|PHILADELPHIA EAGLES|\\SEASON 2024/25|>-|\n')
time.sleep(2)
print('This script will attempt to predict the PHILADELPHIA EAGLES 2024/25 Season.\n')
time.sleep(3)
print('Teams for the 2024/25 NFL Season are based on the rating provided by the SHARP FOOTBALL ANALYSIS Website (https://www.sharpfootballanalysis.com/analysis/nfl-power-rankings/)\n')
time.sleep(5)
print('LET\'S GET STARTED!\n')
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print('1\n')
time.sleep(1)
print('FOOTBALL!\n')
time.sleep(1)

# Week 1 Green Bay Packers

Packers_chance += random.randint(0,32)
Eagles_chance += random.randint(0,32)
print(f'Week 1: {Eagles_name} vs {Packers_name} (HOME) - 06 September 2024')
time.sleep(2)
if Eagles_chance >= Packers_chance:
    Eagles_wins += 1
    confidence = (Eagles_chance - Packers_chance) / 32 *100
    print(f'{Eagles_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
else:
    Eagles_losses += 1
    confidence =(Packers_chance - Eagles_chance) /32 *100
    print(f'{Packers_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
time.sleep(2)

# Week 2 Atlanta Falcons

Falcons_chance += random.randint(0,32)
print(f'Week 2: {Eagles_name} vs {Falcons_name} (HOME) - 16 September 2024')
time.sleep(2)
if Eagles_chance >= Falcons_chance:
    Eagles_wins += 1
    confidence = (Eagles_chance - Falcons_chance) / 32 *100
    print(f'{Eagles_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
else:
    Eagles_losses += 1
    confidence =(Falcons_chance - Eagles_chance) /32 *100
    print(f'{Falcons_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
time.sleep(2)

# Week 3 New Orleans Saints

Saints_chance += random.randint(0,32)
print(f'Week 3: {Eagles_name} vs {Saints_name} (AWAY) - 22 September 2024')
time.sleep(2)
if Eagles_chance >= Saints_chance:
    Eagles_wins += 1
    confidence = (Eagles_chance - Saints_chance) / 32 *100
    print(f'{Eagles_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
else:
    Eagles_losses += 1
    confidence6 =(Saints_chance - Eagles_chance) /32 *100
    print(f'{Saints_name} Win!\n')
    #print(f'We are {int (confidence6)}% confident in this rating.\n')
time.sleep(2)

# Week 4 Tampa Bay Buccaneers

Bucks_chance += random.randint(0,32)
print(f'Week 4: {Eagles_name} vs {Bucks_name} (AWAY) - 29 September 2024')
time.sleep(2)
if Eagles_chance >= Bucks_chance:
    Eagles_wins += 1
    confidence = (Eagles_chance - Bucks_chance) / 32 *100
    print(f'{Eagles_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
else:
    Eagles_losses += 1
    confidence =(Bucks_chance - Eagles_chance) /32 *100
    print(f'{Bucks_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
time.sleep(2)

# Week 5 BYE

time.sleep(2)
print('Week 5 BYE - 06 October 2024\n')
time.sleep(2)

# Week 6 Cleveland Browns

Browns_chance += random.randint(0,32)
print(f'Week 6: {Eagles_name} vs {Browns_name} (HOME) - 13 October 2024')
time.sleep(2)
if Eagles_chance >= Browns_chance:
    Eagles_wins += 1
    confidence = (Eagles_chance - Browns_chance) / 32 *100
    print(f'{Eagles_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
else:
    Eagles_losses += 1
    confidence =(Browns_chance - Eagles_chance) /32 *100
    print(f'{Browns_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
time.sleep(2)

# Week 7 New York Giants

Giants_chance += random.randint(0,32)
print(f'Week 7: {Eagles_name} vs {Giants_name} (AWAY)- 20 October 2024')
time.sleep(2)
if Eagles_chance >= Giants_chance:
    Eagles_wins += 1
    confidence = (Eagles_chance - Giants_chance) / 32 *100
    print(f'{Eagles_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
else:
    Eagles_losses += 1
    confidence =(Giants_chance - Eagles_chance) /32 *100
    print(f'{Giants_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
time.sleep(2)

# Week 8 Cincinnati Bengals

Bengals_chance += random.randint(0,32)
print(f'Week 8: {Eagles_name} vs {Bengals_name} (AWAY) - 27 October 2024')
time.sleep(2)
if Eagles_chance >= Bengals_chance:
    Eagles_wins += 1
    confidence = (Eagles_chance - Bengals_chance) / 32 *100
    print(f'{Eagles_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
else:
    Eagles_losses += 1
    confidence =(Bengals_chance - Eagles_chance) /32 *100
    print(f'{Bengals_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
time.sleep(2)

# Week 9 Jacksonville Jaguars

Jaguars_chance += random.randint(0,32)
print(f'Week 9: {Eagles_name} vs {Jaguars_name} (HOME) - 03 November 2024')
time.sleep(2)
if Eagles_chance >= Jaguars_chance:
    Eagles_wins += 1
    confidence = (Eagles_chance - Jaguars_chance) / 32 *100
    print(f'{Eagles_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
else:
    Eagles_losses += 1
    confidence =(Jaguars_chance - Eagles_chance) /32 *100
    print(f'{Jaguars_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
time.sleep(2)

# Week 10 Dallas Cowboys

Cowboys_chance += random.randint(0,32)
print(f'Week 10: {Eagles_name} vs {Cowboys_name} (AWAY) - 10 November 2024')
time.sleep(2)
if Eagles_chance >= Cowboys_chance:
    Eagles_wins += 1
    confidence = (Eagles_chance - Cowboys_chance) / 32 *100
    print(f'{Eagles_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
else:
    Eagles_losses += 1
    confidence =(Cowboys_chance - Eagles_chance) /32 *100
    print(f'{Cowboys_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
time.sleep(2)

# Week 11 Washington Commanders

Commanders_chance += random.randint(0,32)
print(f'Week 11: {Eagles_name} vs {Commanders_name} (HOME) - 14 November 2024')
time.sleep(2)
if Eagles_chance >= Commanders_chance:
    Eagles_wins += 1
    confidence = (Eagles_chance - Commanders_chance) / 32 *100
    print(f'{Eagles_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
else:
    Eagles_losses += 1
    confidence =(Commanders_chance - Eagles_chance) /32 *100
    print(f'{Commanders_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
time.sleep(2)

# Week 12 Los Angeles Rams

Rams_chance += random.randint(0,32)
print(f'Week 12: {Eagles_name} vs {Rams_name} (AWAY) - 24 November 2024')
time.sleep(2)
if Eagles_chance >= Rams_chance:
    Eagles_wins += 1
    confidence = (Eagles_chance - Rams_chance) / 32 *100
    print(f'{Eagles_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
else:
    Eagles_losses += 1
    confidence =(Rams_chance - Eagles_chance) /32 *100
    print(f'{Rams_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
time.sleep(2)

# Week 13 Baltimore Ravens

Ravens_chance += random.randint(0,32)
print(f'Week 13: {Eagles_name} vs {Ravens_name} (AWAY) - 01 December 2024')
time.sleep(2)
if Eagles_chance >= Ravens_chance:
    Eagles_wins += 1
    confidence = (Eagles_chance - Ravens_chance) / 32 *100
    print(f'{Eagles_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
else:
    Eagles_losses += 1
    confidence =(Ravens_chance - Eagles_chance) /32 *100
    print(f'{Ravens_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
time.sleep(2)

# Week 14 Carolina Panthers

Panthers_chance += random.randint(0,32)
print(f'Week 14: {Eagles_name} vs {Panthers_name} (HOME) - 08 December 2024')
time.sleep(2)
if Eagles_chance >= Panthers_chance:
    Eagles_wins += 1
    confidence = (Eagles_chance - Panthers_chance) / 32 *100
    print(f'{Eagles_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
else:
    Eagles_losses += 1
    confidence =(Panthers_chance - Eagles_chance) /32 *100
    print(f'{Panthers_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
time.sleep(2)

# Week 15 Pittsburgh Steelers

Steelers_chance += random.randint(0,32)
print(f'Week 15: {Eagles_name} vs {Steelers_name} (HOME) - 15 December 2024')
time.sleep(2)
if Eagles_chance >= Steelers_chance:
    Eagles_wins += 1
    confidence = (Eagles_chance - Steelers_chance) / 32 *100
    print(f'{Eagles_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
else:
    Eagles_losses += 1
    confidence =(Steelers_chance - Eagles_chance) /32 *100
    print(f'{Steelers_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
time.sleep(2)

# Week 16 Washington Commanders

Commanders_chance += random.randint(0,32)
print(f'Week 16: {Eagles_name} vs {Commanders_name} (AWAY) - 22 December 2024')
time.sleep(2)
if Eagles_chance >= Commanders_chance:
    Eagles_wins += 1
    confidence = (Eagles_chance - Commanders_chance) / 32 *100
    print(f'{Eagles_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
else:
    Eagles_losses += 1
    confidence =(Commanders_chance - Eagles_chance) /32 *100
    print(f'{Commanders_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
time.sleep(2)

# Week 17 Dallas Cowboys

Cowboys_chance += random.randint(0,32)
print(f'Week 17: {Eagles_name} vs {Cowboys_name} (HOME) - 29 December 2024')
time.sleep(2)
if Eagles_chance >= Cowboys_chance:
    Eagles_wins += 1
    confidence = (Eagles_chance - Cowboys_chance) / 32 *100
    print(f'{Eagles_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
else:
    Eagles_losses += 1
    confidence =(Cowboys_chance - Eagles_chance) /32 *100
    print(f'{Cowboys_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
time.sleep(2)

# Week 18 New York Giants

Giants_chance += random.randint(0,32)
print(f'Week 18: {Eagles_name} vs {Giants_name} (HOME) - 05 January 2025')
time.sleep(2)
if Eagles_chance >= Giants_chance:
    Eagles_wins += 1
    confidence = (Eagles_chance - Giants_chance) / 32 *100
    print(f'{Eagles_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
else:
    Eagles_losses += 1
    confidence =(Giants_chance - Eagles_chance) /32 *100
    print(f'{Giants_name} Win!\n')
    #print(f'We are {int (confidence)}% confident in this rating.\n')
time.sleep(2)

print('THE REGULAR SEASON HAS ENDED\n')
time.sleep(2)
print(f'PHILADELPHIA EAGLES 2024/25 RECORD: {Eagles_wins} WINS & {Eagles_losses} LOSSES\n')
time.sleep(2)
print('E\n')
time.sleep(.1)
print('A\n')
time.sleep(.1)
print('G\n')
time.sleep(.1)
print('L\n')
time.sleep(.1)
print('E\n')
time.sleep(.1)
print('S\n')
time.sleep(.1)
print('EAGLES!')
