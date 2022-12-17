class Combat():
    def __init__(self, 
    player_characters, 
    non_player_characters, 
    player_ply_function, 
    endgame_function):
    
        self.player_characters = player_characters
        self.non_player_characters = non_player_characters
        self.interactive_mode = True
        self.party_xp = 0
        self.party_success = False
        self.ordered_combatants = []
        self.player_ply_function = player_ply_function
        self.endgame_function = endgame_function

    def are_all_characters_dead():
        pass
    def is_combat_over():
        pass
    def end_combat():
        pass
    def ply():
        pass
    def print_stats():
        pass
    def turn():
        pass
    def star():
        pass