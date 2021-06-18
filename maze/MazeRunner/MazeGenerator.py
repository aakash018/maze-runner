from random import randint, randrange, shuffle


class MazeGenerator:
    def __init__(self, row=None, column=None):
        self.row = row or 12
        self.column = column or 12

    def write(self, filename):
        f = open(filename, 'w')
        f.write(self.make_maze(self.row, self.column))
        f.close()

    def make_maze(self, w, h):
        grid = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
        col = [["X "] * w + ['X'] for _ in range(h)] + [[]]
        row = [["XX"] * w + ['X'] for _ in range(h + 1)]

        # debug helper

        # def debugPrint():
        #     print("-"*16)
        #     s = ""
        #     for (a, b) in zip(row, col):
        #         s += ''.join(a + ['\n'] + b + ['\n'])
        #     print(s )

        #     for r in grid:
        #         print(r)

        def walk(x, y):

            # debug helper

            # debugPrint()

            grid[y][x] = 1  # mark random cell as visited

            # getting possible neighbours
            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(d)  # shuffling possible neighbours
            for (xx, yy) in d:
                if grid[yy][xx]:
                    continue  # ignore if visited cell or a wall
                if xx == x:
                    row[max(y, yy)][x] = "X "  # randomly
                if yy == y:
                    r_trap = randint(1, 17)
                    if(r_trap == 4):
                        col[y][max(x, xx)] = "T "  # trap1
                    elif (r_trap < 3):
                        col[y][max(x, xx)] = "U "  # trap2
                    else:
                        col[y][max(x, xx)] = "  "  # open walls

                walk(xx, yy)

        walk(randrange(w), randrange(h))

        s = ""
        for (a, b) in zip(row, col):
            s += ''.join(a + ['\n'] + b + ['\n'])

        l = list(s)
        l[(self.column*2)+2] = "S"
        l[(((self.column*2+1) * (self.column*2+1)) - 4)+(self.column*2+2)] = "E"
        print(len(l))
        fin = ""
        fin += ''.join(l)
        return fin


MazeGenerator()
