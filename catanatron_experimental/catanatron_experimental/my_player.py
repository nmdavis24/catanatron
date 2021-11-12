from typing import Iterable

from catanatron.game import Game
from catanatron.models.actions import Action
from catanatron.models.enums import ActionType, Action, ActionPrompt,BRICK,ORE,Resource,BuildingType,SHEEP,WHEAT,WOOD,action_type_repr
from catanatron.models.player import Player


class MyPlayer(Player):
    def decide(self, game: Game, playable_actions: Iterable[Action]):
        """Should return one of the playable_actions.

        Args:
            game (Game): complete game state. read-only.
            playable_actions (Iterable[Action]): options to choose from
        Return:
            action (Action): Chosen element of playable_actions
        """
        # ===== YOUR CODE HERE =====
        
        print(playable_actions) # Print all possible moves at this iteration

        # When we are rolling or ending turn we will only have one playable action so no reason to decide
        if (len(playable_actions) == 1):
            return playable_actions[0]

        # List of all actions possible: BUILD_INITIAL_SETTLEMENT, 
        # BUILD_INITIAL_ROAD,
        # MOVE_ROBBER,
        # PLAY_TURN,
        # ROLL,
        # PLAY_KNIGHT_CARD,
        # END_TURN,
        # BUY_DEVELOPMENT_CARD, 
        # PLAY_ROAD_BUILDING
        # DISCARD
        # PLAY_MONOPOLY
        # PLAY_YEAR_OF_PLENTY
        # BUILD_ROAD
        # BUILD_SETTLEMENT
        # BUILD_CITY

        
 
        else:

            if (ActionPrompt.BUILD_INITIAL_SETTLEMENT):
                return playable_actions[1]

            return playable_actions[1]



        # ===== END YOUR CODE =====





