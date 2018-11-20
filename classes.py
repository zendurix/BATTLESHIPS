class Place:
    id_counter = 0
    x = 0
    y = 0
    usr_ship_count = 0
    bot_ship_count = 0

    def __init__(self, x, y, id_counter):
        self.x = x
        self.y = y
        self.state = 'clear'
        self.id = id_counter
        self.pformat = Place.print_format(self)
        Place.id_counter += 1
        Place.x += 1
        if Place.x == 5:
            Place.x = 0
            Place.y += 1

    def print_format(self):
        if self.state == 'clear':
            return '0'
        elif self.state == 'ship':
            return 'S'
        elif self.state == 'wreck':
            return 'W'
        elif self.state == 'miss':
            return 'x'

    def place_ship(self):
        self.state = 'ship'
        self.pformat = self.print_format()
        Place.usr_ship_count += 1

    def bot_place_ship(self):
        self.state = 'ship'
        Place.bot_ship_count += 1

    def shot(self):
        if self.state == 'ship':
            self.state = 'wreck'
            Place.usr_ship_count -= 1
        elif self.state == 'clear':
            self.state = 'miss'

        self.pformat = self.print_format()

    def bot_shot(self):
        if self.state == 'ship':
            self.state = 'wreck'
            Place.bot_ship_count -= 1
        elif self.state == 'clear':
            self.state = 'miss'

        self.pformat = self.print_format()



