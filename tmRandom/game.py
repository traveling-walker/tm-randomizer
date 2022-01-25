import random
import json


class Game:
    def __init__(self, mini, merchants, num_players, players):
        self.num_players = 0
        self.players = []
        self.merchants = False
        self.board = ""
        self.scoring_bonus = ""
        self.bonus_tiles = []
        self.round_tiles = {}
        self.game_type = ''
        self.random_draw = False

        self.set_game_type(mini, merchants)
        self.set_players(num_players, players)
        self.set_board()
        self.set_scoring_bonus()
        self.set_bonus_tiles()
        self.set_round_tiles()

    def set_game_type(self, mini, merchants):
        if mini:
            self.game_type = 'expansion'
        if merchants:
            self.merchants = True

    def set_players(self, num_players, players):
        self.num_players = num_players

        while len(self.players) < int(self.num_players):
            self.players.append(players[len(self.players)])

        random.shuffle(self.players)
        random.shuffle(self.players)

    def set_board(self):
        boards = [
            "Base Game",
            "Revised Base Game",
            "Fire & Ice",
            "Loon Lakes",
            "Fjords"
        ]
        random.shuffle(boards)
        random.shuffle(boards)
        self.board = boards.pop()

    def set_scoring_bonus(self):
        tiles = [
            "Greatest Distance",
            "Stronghold & Sanctuary",
            "Outposts",
            "Settlements"
        ]
        if self.merchants:
            tiles.append("Most Trades")
        random.shuffle(tiles)
        random.shuffle(tiles)
        self.scoring_bonus = tiles.pop()

    def set_bonus_tiles(self):
        tiles = ["1 Priest",
                 "1 Worker/3 Power",
                 "6 Money",
                 "+1 Shipping/3 Power",
                 "2 Money/Spade Action",
                 "4 Money/Cult Action",
                 "2 Money/Dwelling Bonus",
                 "1 Worker/Trading House Bonus",
                 "2 Workers/Big Building Bonus"]
        if self.game_type == 'expansion':
            tiles.append("3 Power/Shipping Bonus")
        if self.merchants:
            tiles.extend(["Ship Action/Trade Bonus",
                          "1 Worker & 1 Money/Ships Bonus",
                          "1 Ship/Ship Move Action"])
        random.shuffle(tiles)
        random.shuffle(tiles)
        while len(self.bonus_tiles) < len(self.players) + 3:
            self.bonus_tiles.append(tiles.pop())

    def set_round_tiles(self):
        tiles = ["2VP/Dwelling | Priest/4 Water",
                 "2VP/Dwelling | 4 Power/4 Fire",
                 "3VP/Trading House | Spade/4 Air",
                 "3VP/Trading House | Spade/4 Water",
                 "5VP/StrongSanct | Worker/2 Air",
                 "5VP/StrongSanct | Worker/2 Fire",
                 "2VP/Spade | Money/1 Earth",
                 "5VP/Town | Spade/4 Earth"
                 ]
        if self.game_type == 'expansion':
            tiles.append("4VP/Temple | 2 Money/Priest Sacrificed")
        if self.merchants:
            tiles = [
                "5VP/Town | 1 Money/1 Fire",
                "5VP/BigBuilding | Spade/4 Fire",
                "2VP/Trade | Priest/4 Fire",
                "2VP/Advance | 2 Money/2 Water",
                "3VP/Trading House | Worker/2 Water",
                "2VP/Dwelling | Ship/4 Water",
                "5VP/BigBuilding | Worker/2 Earth",
                "2VP/Spade | 3 Power/3 Earth",
                "4VP/Temple | Advance Ship/5 Earth",
                "2VP/Dwelling | 1 Power/1 Air",
                "3VP/Trading House, Ship/4 Air",
                "2VP/Trade | Spade/4 Air"
            ]
        random.shuffle(tiles)
        random.shuffle(tiles)
        round_num = 6
        while round_num > 0:
            choice = tiles.pop()
            if round_num > 4 and "2VP/Spade" in choice:
                spade_tile = choice
                choice = tiles.pop()
                tiles.append(spade_tile)
                random.shuffle(tiles)
            self.round_tiles[str(round_num)] = choice
            round_num -= 1

    def output(self):
        output = {'players': self.players, 'board': self.board, 'scoring_bonus': self.scoring_bonus,
                  'bonus_tiles': self.bonus_tiles, 'round_tiles': list(self.round_tiles.items())}

        return json.dumps(output)
