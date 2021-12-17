class Moneyfmt:
    def __init__(self, kol):
        self.kol = kol

    def update(self, kol_new):
        self.kol = kol_new

    def __repr__(self):
        print(f'${round(self.kol, 1)}')
        return (f'${round(self.kol, 1)}')

    def __str__(self):
        g = round(self.kol, 2)
        r = f'{g:,}'
        return f'${r}'

