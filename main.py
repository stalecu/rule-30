import random
import argparse
import pyxel

class App:
    def __init__(self, bg=5, fg=10, seed_no=6, width=1920, height=1080, scale=4) -> None:
        self.bg = bg
        self.fg = fg
        self.seed_no = seed_no
        self.scale = scale
        self.width = width
        self.height = height
        self.screen_dims = (width // scale, height // scale)

        pyxel.init(self.screen_dims[0], self.screen_dims[1], fps=60, title='Rule 30')

        self.new_cells = [False] * pyxel.width
        self.time = 0

        for _ in range(self.seed_no):
            i = random.randint(0, self.screen_dims[0] - 1)
            self.new_cells[i] = not self.new_cells[i]

        self.old_cells = self.new_cells.copy()

        pyxel.cls(self.bg)
        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        self.old_cells = self.new_cells.copy()

        for i in range(self.screen_dims[0]):
            self.new_cells[i] = (
                    self.old_cells[(i - 1) % self.screen_dims[0]] ^
                    (self.old_cells[i] or self.old_cells[(i + 1) % self.screen_dims[0]])
            )

        self.time = (self.time + 1) % self.screen_dims[1]

    def draw(self):
        pyxel.line(
            0, self.time,
            self.screen_dims[0], self.time,
            self.bg
        )
        for idx, cell in enumerate(self.new_cells):
            pyxel.pset(idx, self.time, self.fg) if cell else None


if __name__ == '__main__':
    # Insert argparse stuff here
    App()
