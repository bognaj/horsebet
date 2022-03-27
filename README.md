# Horsebet

Having fun with making original problem originally stated by Enns and Ferenstein a little bit more interesting. 

## Original problem
Two gentlemen, Mr White and Mr Black are coowners of the horse named Jerome. Jerome takes part in n races during the season, each of the same length. 
Men decide to play a game to win a horse. During the season each player want to choose race result better than the opponent. 
After each race they meet and discuss. If both of the players hasn't made a desision yet, Mr White is first to decide whether to take the most recent result or not. If he rejects, the same option is given to Mr Black. Previously rejected results can not be reconsidered. When one player makes a selection, the other continues to play alone and try to pick the better result. 
As shown by Enns and Ferenstein, the probability of Mr White victory when n -> infinity is about 0.67. 

## Modified problem
After playing many games, having lost over 2/3 of them, Mr Black wants to change the rules to have the greater chances of winning. Now, at the beginning of the season, random barrier value is stated. 
Mr Black has two ways to win:
1. Take the greater score than Mr White (as usual)
2. Take a result close enough to the barrier such that $f(d)$ is greater than result selected by Mr White, where d is equal to distance of chosen score to the barrier. We consider to versions of f:
* f(d) = |1 - d|
* f(d) = (1 - d)^(n-1)
