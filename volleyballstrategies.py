from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator import VolleySimulation, volley_show_simu
from soccersimulator.settings import*
from pinkertons.tools import*
from pinkertons.Simu import*
from pinkertons.action import*
import math



class Echauffement(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Echauffement")

    def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        m=Move(s)
        sh=Shoot(s)
        if(abs((s.ball-s.my_goal).x)<GAME_WIDTH/2):
            return m.to_ball()+sh.to_enemy()
        else:
            return m.to_wait(0.4)+sh.to_enemy()
        
    
class Attaque(Strategy):
    def __init__(self,forcet=1):
        Strategy.__init__(self, "Attaque")
        self.forcet=forcet

    def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        m=Move(s)
        sh=Shoot(s)
                
        if(abs((s.ball-s.my_goal).x)<GAME_WIDTH/2):
            #return m.to_ball()+sh.to_attaque()
            if(abs((s.ball-s.my_goal).x)<GAME_WIDTH/3):
                return m.to_ball()+sh.to_attaque2()
            else:
                return m.to_ball()+sh.to_attaque()
        else:
            return m.to_wait(0.45)+sh.to_attaque()

class Attaque2(Strategy):
    def __init__(self,forcet=1):
        Strategy.__init__(self, "Attaque")
        self.forcet=forcet

    def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        m=Move(s)
        sh=Shoot(s)
                
        if(abs((s.ball-s.my_goal).x)<GAME_WIDTH/2 and abs((s.ball-s.my_goal).x)>GAME_WIDTH/3.1):
            #return m.to_ball()+sh.to_attaque()
            if(abs((s.ball-s.my_goal).x)<GAME_WIDTH/3):
                return m.to_ball()+sh.to_attaque2()
            else:
                return m.to_ball()+sh.to_attaque()
        else:
            return m.to_wait(0.45)+sh.to_attaque()
        


class UnVsUn(Strategy):
    def __init__(self,forcet=1):
        Strategy.__init__(self, "Attaque")
        self.forcet=forcet

    def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        m=Move(s)
        sh=Shoot(s)
        if(abs((s.ball-s.my_goal).x)<GAME_WIDTH/2):
            #return m.to_ball()+sh.to_attaque()
            if(abs((s.ball-s.my_goal).x)<GAME_WIDTH/3):
                return m.to_ball()+sh.to_attaque2()
            else:
                return m.to_ball()+sh.to_attaque()
        else:
            return m.to_wait(0.25)+sh.to_attaque()
        
class Defense(Strategy):
    def __init__(self,forcet=1):
        Strategy.__init__(self, "Attaque")
        self.forcet=forcet

    def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        m=Move(s)
        sh=Shoot(s)
        if(abs((s.ball-s.my_goal).x)<GAME_WIDTH/2):
            return m.to_ball()+sh.to_attaque()
        else:
            return m.to_wait(0.25)+sh.to_attaque()


class Defense2(Strategy):
    def __init__(self,forcet=1):
        Strategy.__init__(self, "Attaque")
        self.forcet=forcet

    def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        m=Move(s)
        sh=Shoot(s)
        if( abs((s.ball-s.my_goal).x)<GAME_WIDTH/3):
            return m.to_ball()+sh.to_passv()
        else:
            #if(abs((s.ball-s.my_goal).x)<GAME_WIDTH/2):
            #    return m.to_ball()+SoccerAction(shoot=(s.anticiperwait(0.45)-s.player)*2)
            #else:
            return m.to_wait(0.3)+sh.to_passv()
        
        
        
        
class Attaque3(Strategy):
    def __init__(self,force):
        Strategy.__init__(self, "Attaque")
        self.force=force

    def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        m=Move(s)
        sh=Shoot(s)
                
        if(abs((s.ball-s.my_goal).x)<GAME_WIDTH/2):
            #return m.to_ball()+sh.to_attaque()
            if(abs((s.ball-s.my_goal).x)<GAME_WIDTH/3):
                return m.to_ball()+sh.to_attaque3(force)
            else:
                return m.to_ball()+sh.to_attaque()
        else:
            return m.to_wait(0.45)+sh.to_attaque()
        
        
        