import re
from collections import defaultdict

attacks = {
    "magic missile": {"cost": 53, "max_cooldown": 0}, 
    "drain": {"cost": 73, "max_cooldown": 0}, 
    "shield": {"cost": 113, "max_cooldown": 6}, 
    "poison": {"cost": 173, "max_cooldown": 6},
    "recharge": {"cost": 229, "max_cooldown": 5}
}

class State:
    def __init__(self, player_hp, player_mp, boss_hp, boss_damage, hard_mode=False):
        self.player_hp = player_hp
        self.player_mp = player_mp
        self.boss_hp = boss_hp
        self.boss_damage = boss_damage
        self.hard_mode = hard_mode
        self.cooldowns = {name: 0 for name in attacks.keys()}

    def iter_legal_moves(self):
        if self.player_hp <= 0:
            return
        for name, d in attacks.items():
            if self.player_mp >= d["cost"] and self.cooldowns[name] <= 1:
                yield name

    def apply(self, move):
        """
        perform the given action, and then take damage from the boss.
        """

        if self.hard_mode:
            self.player_hp -= 1
            if self.player_hp <= 0:
                return

        self.execute_timer_effects()
        self.decrement_timers()
        self.cooldowns[move] = attacks[move]["max_cooldown"]
        self.player_mp -= attacks[move]["cost"]
        assert self.player_mp >= 0
        assert self.player_hp > 0
        if move == "magic missile":
            self.boss_hp -= 4
        elif move == "drain":
            self.boss_hp -= 2
            self.player_hp += 2

        self.execute_timer_effects()
        self.decrement_timers()
        if self.boss_hp > 0:
            damage = self.boss_damage - (7 if self.cooldowns["shield"] > 0 else 0)
            damage = max(1, damage)
            self.player_hp -= damage

    def applied(self, move):
        """like apply, but returns a modified copy of self, leaving self unmutated"""
        x = self.copy()
        x.apply(move)
        return x

    def execute_timer_effects(self):
        if self.cooldowns["poison"] > 0:
            self.boss_hp -= 3
        if self.cooldowns["recharge"] > 0:
            self.player_mp += 101
        #shield gets applied in `apply`

    def decrement_timers(self):
        for k in self.cooldowns.keys():
            self.cooldowns[k] = max(0, self.cooldowns[k]-1)

    def copy(self):
        x = State(self.player_hp, self.player_mp, self.boss_hp, self.boss_damage, self.hard_mode)
        x.cooldowns = self.cooldowns.copy()
        return x

    def tuple(self):
        return (self.player_hp, self.player_mp, self.boss_hp, self.boss_damage, self.hard_mode,) + tuple(self.cooldowns.values())

    def __eq__(self, other):
        return self.tuple() == other.tuple()

    def __hash__(self):
        return hash(self.tuple())
            
    def __repr__(self):
        return f"State({self.player_hp}, {self.player_mp}, {self.boss_hp}, {self.boss_damage}, {self.hard_mode})"

def djikstra(start):
    visited = set()
    distances = defaultdict(lambda: float("inf"))
    distances[start] = 0
    node = start
    while True:
        if node.boss_hp <= 0:
            return distances[node]
        for move in node.iter_legal_moves():
            neighbor = node.applied(move)
            if neighbor not in visited:
                tentative_distance = distances[node] + attacks[move]["cost"]
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
        visited.add(node)
        node = min((node for node in distances.keys() if node not in visited), key=lambda node: distances[node])

with open("input") as file:
    boss_hp, boss_damage = map(int, re.findall("\d+", file.read()))


for part in (1,2):
    state = State(50, 500, boss_hp, boss_damage, part==2)
    print(djikstra(state))