'''
Easely rank players or teams using the Elo-rating system.
            
```python
# Example usage:
import elo
r1 = 2400 # Player r1 with rating 2400
r2 = 2000 # Player r2 with rating 2000

# New elo for player r1 after loosing to player r2
r1_prime = elo.update(r1, r2, elo.LOSS)

# New elo for player r2 after winning over player r1
r2_prime = elo.update(r2, r1, elo.WON)
```
'''

K_FACTOR = 32 # The K-factor measures how strong a match will impact the players’ ratings. 

#----- The actual score Used as input for `S(outcome)` function ------
LOSS = 0.0
TIE = 0.5
WON = 1.0
#----------------------------------------------------

def R(r):
    '''
    Compute the transformed rating of a player.
    '''
    return pow(10, r/400)

def E(R1, R2):
    '''
    Returns the expected score of a transformed rating R1 vs another transformed rating R2.
    The return value is a float and ranges between 0 and 1 (inclusive).
    '''
    return R1/(R1 + R2)

def S(outcome):
    '''
    Get the acutal score after a match has finished.
    '''
    return outcome

def r_prime(r1, S1, E1):
    '''
    Get the new elo based on the current rating r1, the score for the target player S1 and
    the exprected score of the target player vs another.    
    '''
    return r1 + K_FACTOR * (S1 - E1)

def update(r1, r2, S1):
    '''
    Get the updated elo (rounded) of a player after a match has finished. 
    '''
    return round(r_prime(r1, S1, E(R(r1), R(r2))))
