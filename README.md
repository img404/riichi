This repo contains self-directed learning for Python through riichi mahjong topics. 


The first program was **riichi_score_calculator**, which takes user input about a winning hand and calculates score payments. The initial iteration uploaded to GitHub took about a week to write. After initially using a naive version tracking system, I am now using SemVar (https://semver.org/) to track updates.

Roadmap for riichi_score_calculator.py:
1. Input validation is needed for han, fu, and honba.
2. Add a variable at the top for kiriage mangan (a bool that controls whether 4han 30fu & 3han 60fu rounds up to mangan).
3. Add a variable that determines how multiple yakunan are handled, including WRC "yonbaiman" instead of kazoe (counted) yakuman. 

 
Future project ideas include:
1. Haipai (opening hand) simulator.
2. Hand validator, with yaku detection and auto-scoring. 
3. Shanten calculator.
