foo = "SSYYNNOOPPSSIISS"
import itertools
print(''.join(ch for ch, _ in itertools.groupby(foo)))