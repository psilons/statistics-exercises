# https://en.wikipedia.org/wiki/Positive_and_negative_parts

def pos_parts(x: float) -> float:
    return 0 if x < 0 else x


def neg_parts(x: float) -> float:
    return 0 if x > 0 else x


def segs(x: float) -> float:
    return pos_parts(neg_parts(x-1) + 1)


import matplotlib.pyplot as plt

xs = [i for i in range(-2, 3)]
ys = [segs(i) for i in range(-2, 3)]

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.plot(xs, ys)

plt.ylabel('segs(x)')
plt.ylim([-1, 2])

fig.tight_layout()
plt.show()
