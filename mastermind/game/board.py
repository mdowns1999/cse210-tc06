import random

class Board:
    """A designated playing surface. The responsibility of Board is to keep track of the pieces in play.
    
    Stereotype: 
        Information Holder

    Attributes:
        _piles (list): The number of piles of stones.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._number = 0
        self._prepare()

    def apply(self, move):
        """Applies the given move to the playing surface. In this case, that 
        means removing a number of stones from a pile.
        
        Args:
            self (Board): an instance of Board.
            move (Move): The move to apply.
        """
        pile = move.get_pile()
        stones = move.get_stones()
        self._piles[pile] = max(0, self._piles[pile] - stones)
    
    def is_empty(self):
        """Determines if all the stones have been removed from the board.
        
        Args:
            self (Board): an instance of Board.

        Returns:
            boolean: True if the board has no stones on it; false if otherwise.
        """
        empty = [0] * len(self._piles)
        return self._piles == empty

    def to_string(self, roster):
        """Converts the board data to its string representation.

        Args:
           self (Board): an instance of Board.

        Returns:
            string: A representation of the current board.
        """ 
        text =  "\n--------------------"
        for player in roster.players:
            player = roster.get_current()
            text += (f"\n{player}: " + "----" )
        text += "\n--------------------"
        return text

    def _prepare(self):
        """Sets up the board with a random number between 1000 and 9999
        
        Args:
            self (Board): an instance of Board.
        """
        self._number = random.randint(1000, 10000) 
        # for n in range(piles):
        #     stones = random.randint(1, 9)
        #     self._piles.append(stones)