from typing import Iterable

from catanatron.game import Game
from catanatron.models.actions import Action
from catanatron.models.enums import ActionType, Action, ActionPrompt,BRICK,ORE,Resource,BuildingType,SHEEP,WHEAT,WOOD,action_type_repr
from catanatron.models.player import Player


class MyPlayer(Player):
    def decide(self, game: Game, playable_actions: Iterable[Action]):


        # When we are rolling or ending turn we will only have one 
        # playable action so no reason to decide. Otherwise select
        # second action
        if (len(playable_actions) == 1):
            return playable_actions[0]

        
        else:
            return playable_actions[1]



        # ===== END YOUR CODE =====







