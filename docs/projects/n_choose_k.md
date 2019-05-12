Stumbled upon this and thought it was cool. There's probably
just some math from high school that i'm forgetting about
that explains this in very simple terms.

If I have a set of `N` values:

```
[0,1,2,3]
```

I can figure out the number of possible ways to choose `k`
values from them using 'n-choose-k':

```
n_choose_k = N! / ( k! (N-k)! )
```

This gives rise to pascal's triangle:

```python
from scipy.special import comb
ns = range(10)
combos = [list(int(comb(n,i)) for i in range(n+1)) for n in ns]
```

combos:

```
[[1],
 [1, 1],
 [1, 2, 1],
 [1, 3, 3, 1],
 [1, 4, 6, 4, 1],
 [1, 5, 10, 10, 5, 1],
 [1, 6, 15, 20, 15, 6, 1],
 [1, 7, 21, 35, 35, 21, 7, 1],
 [1, 8, 28, 56, 70, 56, 28, 8, 1],
 [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]
```

For another problem, I thought I needed to sum up all of
these possible combinations for a given `N`:

```python
from scipy.special import comb
ns = range(10)
combos = [sum(comb(n,i) for i in range(n+1)) for n in ns]
```

And holy crow, that's just `2^N`:

```
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```
