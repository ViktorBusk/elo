# Easily rank players with the Elo-rating system in Python!

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
