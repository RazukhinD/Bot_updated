max_total = 150
total= max_total
game = False
bot_level = 'light'

def get_total():
    global total
    return total

def set_max_total(value: int):
    global max_total
    max_total=value


def take_candies(take: int):
    global total
    total -= take

def check_game():
    global game
    return game

def new_game():
    global game
    global total
    if game:
        game=False
    else:
        total = max_total
        game=True

def change_level():
    global bot_level
    if bot_level == 'light':
        bot_level ='hard'
    else:
        bot_level='light'

def get_bot_level():
    global bot_level
    return bot_level
# class Games:
#     total: int
#     player_one_id: int
#     player_two_id: int
#
#     def __int__(self, total: int, player_on_id: int):
#         self.total = total
#         self.player_one_id = player_on_id
#