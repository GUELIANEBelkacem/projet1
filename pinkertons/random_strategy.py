# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import*
from .tools import*
from .Simu import*
from .action import*
import math

class AttaquantStrategy(Strategy):
    def __init__(self,strength=5.1):
        Strategy.__init__(self, "Attaquant")
        self.strength=strength

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s=SuperState(state,id_team,id_player)
        m=Move(s)
        sh=Shoot(s)
        
        return m.to_ball()+sh.to_goal()


class DefonceurStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defonceur")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s=SuperState(state,id_team,id_player)
        m=Move(s)
        sh=Shoot(s)

        if(s.dball<GAME_WIDTH/2) and (s.dplayeren<(GAME_WIDTH*3/5)) and s.dgoal>(GAME_WIDTH*5/8):
            if not(s.dball<PLAYER_RADIUS+BALL_RADIUS) :
                return m.to_ball()+sh.to_goal()
            else:
                if(s.dplayerfr<GAME_HEIGHT/2):
                    return SoccerAction((s.player-s.poplayerfr)*999,(s.player-s.poplayerfr)*999)
                else:
                    return m.to_ball()+sh.to_goal()
        else:
            return SoccerAction(Vector2D(abs(s.goal.x-GAME_WIDTH+10)-s.player.x,s.goal.y-s.player.y),s.goal-s.player)
        
        
"""
        if(s.dball<GAME_WIDTH/2)and(s.dplayeren<GAME_WIDTH/2+30)and((s.goal-s.ball).norm>GAME_WIDTH/2):
            if s.dball<PLAYER_RADIUS+BALL_RADIUS:
                return SoccerAction(s.ball-s.player-s.vball*10,(s.goal-s.player).normalize()*2)
            else:
                return SoccerAction(s.ball+s.vball*10-s.player,0)
        else:
            return SoccerAction(Vector2D(abs(s.goal.x-GAME_WIDTH+10)-s.player.x,s.goal.y-s.player.y),0)

"""


'''
class FonceurStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonceur")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s=SuperState(state,id_team,id_player)
        if s.dball<PLAYER_RADIUS+BALL_RADIUS:
            return SoccerAction(s.ball-s.player,s.goal-s.player)
        else:
            return SoccerAction(s.ball-s.player,s.goal-s.player)
'''        