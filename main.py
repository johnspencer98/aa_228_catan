from tkinter import *
import math
import numpy as np
import player
import vertex
import Edge
import tile

# ok and we add the vertices!
vertices_coordinates = ['top_left', 'top_center', 'top_right', 'mid_left', 'mid_center', 'mid_right', 'bot_left',
                        'bot_center', 'bot_right']

# now we map vertices to edges, we will use this when building roads because we need to know
# which edges we can build our roads on
vert2edge = {'top_left': [(1, 1), (2, 1)], 'top_center': [(1, 1), (1, 2), (2, 2)],
             'top_right': [(1, 2), (2, 3)], 'mid_left': [(2, 1), (3, 1)],
             'mid_center': [(2, 2), (3, 2), (3, 1), (4, 2)],
             'mid_right': [(3, 2), (2, 3)], 'bot_left': [(4, 1), (5, 1)],
             'bot_center': [(5, 1), (5, 2)], 'bot_right': [(4, 3), (5, 2)],
             }

# now we map vertices to edges, we will use this when building roads because we need to know
# which edges we can build our roads on
edge2vert = {(1, 1): ['top_left', 'top_center'], (1, 2): ['top_center', 'top_right'],
             (2, 1): ['top_left', 'mid_left'], (2, 2): ['top_center', 'mid_center'],
             (2, 3): ['top_right', 'mid_right'], (3, 1): ['mid_left', 'mid_center'],
             (3, 2): ['mid_center', 'mid_right'], (4, 1): ['mid_left', 'bot_left'],
             (4, 2): ['mid_center', 'bot_center'], (4, 3): ['mid_right', 'bot_right'],
             (5, 1): ['bot_left', 'bot_center'], (5, 2): ['bot_center', 'bot_right'],
             (5, 3): ['bot_right', 'bot_center']}

# now we map vertices to tiles, where each key is a vertex and the value is the adjacent tiles
# we will use this when collecting resources on the tiles that are adjacent to our settlements
vert2tiles = {'top_left': ['tile_2'], 'top_center': ['tile_1', 'tile_2'],
              'top_right': ['tile_1'], 'mid_left': ['tile_2', 'tile_3'],
              'mid_center': ['tile_1', 'tile_2', 'tile_3', 'tile_4'],
              'mid_right': ['tile_1', 'tile_4'], 'bot_left': ['tile_3'],
              'bot_center': ['tile_3', 'tile_4'], 'bot_right': ['tile_4']
              }


def createBoard(tiles_list, vertices_list, edges_list):
    # now we initiate vertices as objects
    for coord in vertices_coordinates:
        new_vertex = vertex.Vertex()
        new_vertex.coordinate = coord
        new_vertex.edges = vert2edge[coord]
        new_vertex.tiles = vert2tiles[coord]
        vertices_list.append(new_vertex)

    # now we define edges! lets do some numerical indexing here, so this is what it looks like visually
    edge_coords = [(1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (4, 1), (4, 2), (4, 3), (5, 1), (5, 2)]
    for coord in edge_coords:
        new_edge = Edge.Edge()
        new_edge.coordinate = coord
        new_edge.vertices = edge2vert[coord]
        edges_list.append(new_edge)

    # let's create a super simple board
    tile_coord = ['tile_1', 'tile_2', 'tile_3', 'tile_4']
    resources = ['wood', 'brick', 'wood', 'brick']
    roll_numbers = [1, 2, 3, 4]
    resource_assignment = np.random.choice(4, 4, replace=False)
    roll_assignment = np.random.choice(4, 4, replace=False)

    for z, t_coord in enumerate(tile_coord):
        new_tile = tile.Tile()
        new_tile.coordinate = t_coord
        new_tile.dice_roll = roll_numbers[resource_assignment[z]]
        new_tile.resource = resources[roll_assignment[z]]
        tiles_list.append(new_tile)
    # let's print what our random board looks like
    # printBoard()


def give_resources(roll):
    for cur_player in players:
        for cur_vertex in cur_player.settlements:
            for cur_tile_coord in cur_vertex.tiles:
                cur_tile = next((x for x in tiles if x.coordinate == cur_tile_coord), None)
                if cur_tile.dice_roll == roll:
                    cur_player.hand[cur_tile.resource] += 1


def printBoard():
    # top_left <- (1,1) -> top_center <- (1,2) -> top_right
    #   ^                      ^                        ^
    #   |                      |                        |
    # (2,2)     *tile_2*     (2,2)       *tile_1*     (2,3)
    #   |       *roll #*       |         *roll #*       |
    #   v                      v                        v
    # mid_left <- (3,1) -> mid_center <- (3,2)  -> mid_right
    #   ^                      ^                        ^
    #   |                      |                        |
    # (4,1)     *tile_3*     (4,2)       *tile_4*     (4,3)
    #   |       *roll #*       |         *roll #*       |
    #   v                      v                        v
    # bot_left <- (5,1) -> bot_center <- (5,2) -> bot_right

    print('GAME BOARD')
    print()
    print(next((x for x in vertices if x.coordinate == 'top_left'), None).to_string() + ' <- '
          + next((x for x in edges if x.coordinate == (1, 1)), None).to_string() + ' -> '
          + next((x for x in vertices if x.coordinate == 'top_center'), None).to_string() + ' <- '
          + next((x for x in edges if x.coordinate == (1, 2)), None).to_string() + ' -> '
          + next((x for x in vertices if x.coordinate == 'top_right'), None).to_string())
    print('  ^                      ^                        ^')
    print('  |                      |                        |')
    print(next((x for x in edges if x.coordinate == (2, 1)), None).to_string() + '      '
          + next((x for x in tiles if x.coordinate == 'tile_2'), None).resource + '     '
          + next((x for x in edges if x.coordinate == (2, 2)), None).to_string() + '        '
          + next((x for x in tiles if x.coordinate == 'tile_1'), None).resource + '      '
          + next((x for x in edges if x.coordinate == (2, 3)), None).to_string())
    print('  |          ' + str(next((x for x in tiles if x.coordinate == 'tile_2'), None).dice_roll) + '           | '
          + '          ' + str(next((x for x in tiles if x.coordinate == 'tile_1'), None).dice_roll) + '            | ')
    print('  v                      v                        v')
    print(next((x for x in vertices if x.coordinate == 'mid_left'), None).to_string() + ' <- '
          + next((x for x in edges if x.coordinate == (3, 1)), None).to_string() + ' -> '
          + next((x for x in vertices if x.coordinate == 'mid_center'), None).to_string() + ' <- '
          + next((x for x in edges if x.coordinate == (3, 2)), None).to_string() + ' -> '
          + next((x for x in vertices if x.coordinate == 'mid_right'), None).to_string())
    print('  ^                      ^                        ^')
    print('  |                      |                        |')
    print(next((x for x in edges if x.coordinate == (4, 1)), None).to_string() + '      '
          + next((x for x in tiles if x.coordinate == 'tile_3'), None).resource + '     '
          + next((x for x in edges if x.coordinate == (4, 2)), None).to_string() + '        '
          + next((x for x in tiles if x.coordinate == 'tile_4'), None).resource + '      '
          + next((x for x in edges if x.coordinate == (4, 3)), None).to_string())
    print('  |          ' + str(next((x for x in tiles if x.coordinate == 'tile_3'), None).dice_roll) + '           | '
          + '          ' + str(next((x for x in tiles if x.coordinate == 'tile_4'), None).dice_roll) + '            | ')
    print('  v                      v                        v')
    print(next((x for x in vertices if x.coordinate == 'bot_left'), None).to_string() + ' <- '
          + next((x for x in edges if x.coordinate == (5, 1)), None).to_string() + ' -> '
          + next((x for x in vertices if x.coordinate == 'bot_center'), None).to_string() + ' <- '
          + next((x for x in edges if x.coordinate == (5, 2)), None).to_string() + ' -> '
          + next((x for x in vertices if x.coordinate == 'bot_right'), None).to_string())


if __name__ == '__main__':
    # Welcome to the simulator
    no_of_games = 1000
    pl1_count = 0
    pl2_count = 0
    for i in range(no_of_games):
        #print(i)
        tiles = []
        edges = []
        vertices = []
        #print('Tiles', tiles)
        createBoard(tiles, vertices, edges)
        players = []
        # let's create player 1
        pl1 = player.RandomPlayer('pl1')
        # lets create player 2
        pl2 = player.GreedyPlayer('pl2')
        players.append(pl1)
        players.append(pl2)

        # now let's have both select their first settlements
        pl1.choose_first_settlement(vertices)
        pl2.choose_first_settlement(vertices)
        pl1.choose_first_settlement(vertices)
        pl2.choose_first_settlement(vertices)

        # now lets simulate who wins!!!
        turns = 1
        finished = False
        while (not finished) and turns < 50:
            pl1_dice_roll = np.random.randint(1, 5)
            # print('pl1_dice_roll: ', pl1_dice_roll)
            give_resources(pl1_dice_roll)
            pl1.take_turn(vertices, edges)
            if pl1.player_score() > 4:
                # printBoard()
                pl1_count += 1
                finished = True
            else:
                pl2_dice_roll = np.random.randint(1, 5)
                # print('pl2_dice_roll: ', pl2_dice_roll)
                pl2.take_turn(vertices, edges)
                if pl2.player_score() > 4:
                    # printBoard()
                    pl2_count += 1
                    finished = True
            turns += 1
        #print(turns)
        del tiles
        del edges
        del vertices
        del players

    print(pl1_count, pl2_count)
    print('pl1 Winning %:', float(pl1_count) / (pl1_count + pl2_count) * 100, 'pl2 Winning %:',
          float(pl2_count) / (pl1_count + pl2_count) * 100)

    # print(pl1.hand)
    # print(pl2.hand)
