# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import*
from .tools import*
from .Simu import*
from .action import*
import math

class AttaquantStrategy(Strategy):
    def __init__(self,strength=5.1,forcet=1):
        Strategy.__init__(self, "Attaquant")
        self.strength=strength
        self.forcet=forcet
        

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s=SuperState(state,id_team,id_player)
        m=Move(s)
        sh=Shoot(s)
        return m.to_ball()+sh.to_goal(self.forcet)

class DefonceurStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defonceur")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s=SuperState(state,id_team,id_player)
        m=Move(s)
        sh=Shoot(s)

        if(s.dball<GAME_WIDTH/2) and (s.dplayeren<(GAME_WIDTH/2)) and s.dgoal>(GAME_WIDTH*5/8):
            if not(s.dball<PLAYER_RADIUS+BALL_RADIUS+GAME_WIDTH*0.1) :
                if(s.dballen>GAME_WIDTH*0.3):
                    return m.to_home()+sh.to_defend()
                else:
                    return m.to_ball()+sh.to_defend()
                
            else:
                if(s.dplayerfr<GAME_HEIGHT/2):
                    if(abs((((s.player-s.poplayerfr)*3+(s.goal-s.player)/2)/12).x)-abs(abs(s.goal.x-GAME_WIDTH)-s.player.x)<GAME_HEIGHT/5 and abs((((s.player-s.poplayerfr)*3+(s.goal-s.player)/2)/12).y)-abs(s.goal.y-s.player.y)<GAME_HEIGHT/5 ):
                         return m.to_ball()+sh.to_defend()
                    else:
                         return m.to_ball()+sh.to_pass()
                else:
                    return m.to_ball()+sh.to_defend()
        else:
            return m.to_home()+sh.to_defend()



        
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



class CoteStrategyd(Strategy):
    def __init__(self,forcet=1):
        Strategy.__init__(self, "wing")
        self.forcet=forcet

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s=SuperState(state,id_team,id_player)
        m=Move(s)
        sh=Shoot(s)
        if(s.ami==False):
            return m.to_betweend()+sh.to_goal(self.forcet)
        else:
            if(s.shouldipass==True):
                return m.to_ball()+sh.to_pass()
            else:
                return m.to_ball()+sh.to_goal(self.forcet)
                
        
class CoteStrategyg(Strategy):
    def __init__(self,forcet=1):
        Strategy.__init__(self, "wing")
        self.forcet=forcet

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s=SuperState(state,id_team,id_player)
        m=Move(s)
        sh=Shoot(s)
        if(s.ami==False):
            return m.to_betweeng()+sh.to_goal(self.forcet)
        else:
            if(s.shouldipass==True):
                return m.to_ball()+sh.to_pass()
            else:
                return m.to_ball()+sh.to_goal(self.forcet)    
                
class StaticStrategy(Strategy):
    def __init__(self,forcet=1):
        Strategy.__init__(self, "wing")
        self.forcet=forcet

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        return SoccerAction() 
        

'''       
class DefonceurStrategyother(Strategy):
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
                return m.to_ball()+sh.to_goal(self.forcet)
            else:
                if(s.dplayerfr<GAME_HEIGHT/2):
                    if(abs((((s.player-s.poplayerfr)*3+(s.goal-s.player)/2)/12).x)-abs(abs(s.goal.x-GAME_WIDTH)-s.player.x)<GAME_HEIGHT/5 and abs((((s.player-s.poplayerfr)*3+(s.goal-s.player)/2)/12).y)-abs(s.goal.y-s.player.y)<GAME_HEIGHT/5 ):
                         return m.to_ball()+sh.to_goal(self.forcet)
                    else:
                         return SoccerAction((s.player-s.poplayerfr)*999,((s.player-s.poplayerfr)*3+(s.goal-s.player)/2)/12)
                else:
                    return m.to_ball()+sh.to_goal(self.forcet)
        else:
            return SoccerAction(Vector2D(abs(s.goal.x-GAME_WIDTH+10)-s.player.x,s.goal.y-s.player.y),s.goal-s.player)
        
'''
"""
        if(s.dball<GAME_WIDTH/2)and(s.dplayeren<GAME_WIDTH/2+30)and((s.goal-s.ball).norm>GAME_WIDTH/2):
            if s.dball<PLAYER_RADIUS+BALL_RADIUS:
                return SoccerAction(s.ball-s.player-s.vball*10,(s.goal-s.player).normalize()*2)
            else:
                return SoccerAction(s.ball+s.vball*10-s.player,0)
        else:
            return SoccerAction(Vector2D(abs(s.goal.x-GAME_WIDTH+10)-s.player.x,s.goal.y-s.player.y),0)

"""




      