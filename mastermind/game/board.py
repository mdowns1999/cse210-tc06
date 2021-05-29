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
        self._items = {}
        self._numbers = {}
        self.guess = ""
        self.code = ""
        self.hint = ""
        
    # def split(self, variable):
    #     return list(variable)

    def apply(self, player, move):
        """Applies the given move to the playing surface. In this case, that 
        means removing a number of stones from a pile.
        
        Args:
            self (Board): an instance of Board.
            move (Move): The move to apply.
        """
        name = player.get_name()
        player_input = list(move.get_guess())

        guess = list(self._items[name][0])
        code = list(self._numbers[name])
        hint = list(self._items[name][1])

        for i in range(0, 4):

            if player_input[i] in code: 
                # checking for equality of digits
                if player_input[i] == code[i]:  

                    # hence, the digit is stored in correct[].
                    guess[i] = player_input[i]
                    hint[i] = "x"

                    print(f"You guessed the number {player_input[i]} in the right spot!")

                else:
                    hint[i] = "o"

                    print(f"The number {player_input[i]} is correct, but its in a different spot!")


        self.guess = "".join(guess)
        self.code = "".join(code)
        self.hint = "".join(hint)

        self._items[name] = [self.guess, self.hint]

        # pile = move.get_pile()
        # stones = move.get_stones()
        # self._piles[pile] = max(0, self._piles[pile] - stones)
    
    def is_empty(self):
        """Determines if all the stones have been removed from the board.
        
        Args:
            self (Board): an instance of Board.

        Returns:
            boolean: True if the board has no stones on it; false if otherwise.
        """
        if self.guess == self.code:
            return True
        else:
            return False
        # empty = [0] * len(self._piles)
        # return self._piles == empty

    def to_string(self):
        """Converts the board data to its string representation.

        Args:
           self (Board): an instance of Board.

        Returns:
            string: A representation of the current board.
        """ 

        text =  "\n--------------------\n"
        for key, value in self._items.items():
            value = " , ".join(value)
            text += "Player {}: {}\n".format(key, value)
        text += "--------------------"
        return text

    def prepare(self, player):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
        """
        name = player.get_name()
        self.code = str(random.randint(1000, 10000))
        self.guess = "----"
        self.hint = "****"
        self._numbers[name] = self.code
        self._items[name] = [self.guess, self.hint]

        

    #CODE SNIPPTS DOWN BELOW
    
        
    def _create_hint(self, code, guess):
        """Generates a hint based on the given code and guess.

        Args:
            self (Board): An instance of Board.
            code (string): The code to compare with.
            guess (string): The guess that was made.

        Returns:
            string: A hint in the form [xxxx]
        """ 
        hint = ""
        for index, letter in enumerate(guess):
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return hint