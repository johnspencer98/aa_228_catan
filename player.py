import numpy as np
import vertex
import Edge


class GreedyPlayer:

    def __init__(self, name):
        self.name = name

        self.hand = {'ore  ': 0,
                     'wheat': 0,
                     'wood': 0,
                     'brick': 0}

        self.settlements = []
        self.cities = []
        self.roads = []
        self.points = 0

    # greedy choose best settlement by choosing spot with most potential for resources
    def choose_first_settlement(self, vertices):
        # score is represented by probability that a certain tile gets a resource
        best_score = 0
        best_vertex = None
        for cur_vertex in vertices:
            # check to see if the vertex is already chosen
            if cur_vertex.player is None:
                cur_score = len(cur_vertex.tiles)
                if cur_score > best_score:
                    best_score = cur_score
                    best_vertex = cur_vertex
        # now we set the best vertex
        if best_vertex is not None:
            best_vertex.player = self.name
            # choose settlement
            best_vertex.type = 'set'
            self.settlements.append(best_vertex)
        else:
            pass
            # print('Could not find valid location for settlement')

    # randomly builds a road
    def build_road(self, vertices, edges):
        if self.hand['wood'] > 0 and self.hand['brick'] > 0 and np.random.rand > 0.5:
            decision_order = np.random.choice(len(self.vertices), len(self.vertices), replace=False)
            for i in range(len(decision_order)):
                cur_vertex = vertices[decision_order[i]]
                for cur_edge in cur_vertex.edges:
                    if cur_edge.player is None:
                        cur_edge.player = self.name
                        self.roads = cur_edge
                    return
        else:
            return

    # randomly builds another settlement
    def build_settlement(self, vertices, edges):
        if self.hand['wood'] > 2 and self.hand['brick'] > 2:
            # score is represented by probability that a certain tile gets a resource
            best_score = 0
            best_vertex = None
            for cur_vertex in vertices:
                # check to see if the vertex is already chosen
                if cur_vertex.player is None:
                    cur_score = len(cur_vertex.tiles)
                    if cur_score > best_score:
                        best_score = cur_score
                        best_vertex = cur_vertex
            # now we set the best vertex
            if best_vertex is not None:
                best_vertex.player = self.name
                # choose settlement
                best_vertex.type = 'set'
                self.settlements.append(best_vertex)
                self.hand['wood'] -= 2
                self.hand['brick'] -= 2
            else:
                pass
                # print('Could not find valid location for settlement')

    def take_turn(self, vertices, edges):
        self.build_settlement(vertices, edges)

    def player_score(self):
        return len(self.settlements) + len(self.cities)


class RandomPlayer:

    def __init__(self, name):
        self.name = name

        self.hand = {'ore  ': 0,
                     'wheat': 0,
                     'wood': 0,
                     'brick': 0}

        self.settlements = []
        self.cities = []
        self.roads = []
        self.points = 0

    # randomly choose best settlement
    def choose_first_settlement(self, vertices):
        decision_order = np.random.choice(len(vertices), len(vertices), replace=False)
        for i in range(len(decision_order)):
            # check to see if the vertex is already chosen
            cur_vertex = vertices[decision_order[i]]
            if cur_vertex.player is None:
                cur_vertex.player = self.name
                # choose settlement
                cur_vertex.type = 'set'
                self.settlements.append(cur_vertex)
                return
        # print('Could not find valid location for settlement')

    # randomly choose best road
    def build_road(self, vertices, edges):
        if self.hand['wood'] > 0 and self.hand['brick'] > 0:
            decision_order = np.random.choice(len(self.vertices), len(self.vertices), replace=False)
            for i in range(len(decision_order)):
                cur_vertex = vertices[decision_order[i]]
                for cur_edge in cur_vertex.edges:
                    if cur_edge.player is None:
                        cur_edge.player = self.name
                        self.roads = cur_edge
                    return
        else:
            return

    # randomly choose best settlement
    def build_settlement(self, vertices, edges):
        if self.hand['wood'] > 2 and self.hand['brick'] > 2:
            decision_order = np.random.choice(len(vertices), len(vertices), replace=False)
            for i in range(len(decision_order)):
                # check to see if the vertex is already chosen
                cur_vertex = vertices[decision_order[i]]
                if cur_vertex.player is None:
                    cur_vertex.player = self.name
                    # choose settlement
                    cur_vertex.type = 'set'
                    self.settlements.append(cur_vertex)
                    self.hand['wood'] -= 2
                    self.hand['brick'] -= 2
                    return
            # print('Could not find valid location for settlement')

    def take_turn(self, vertices, edges):
        self.build_settlement(vertices, edges)

    def player_score(self):
        return len(self.settlements) + len(self.cities)
