import pandas as pd


class TransitionFunction:
    def __init__(self, fp: str):
        """Creates a TransitionFunction object given file path to its .csv definition file

        Args:
            fp (str): Path to definition file
        """
        self.transition_table = pd.read_csv(fp)
        self.lexicon = list(self.transition_table.keys())[1:]
        self.states = self.transition_table["state"].to_list()

    def run(self, state: int, input_string: str) -> int:
        """Returns the next state given current state and input string.

        Args:
            state (int): Current state
            input_string (str): Input string, has to be in the lexicon

        Raises:
            Exception: if the state is not found it will raise an error

        Returns:
            int: The next state
        """
        if state == -1:
            return -1
        if (input_string in self.lexicon) and (state in self.states):
            out = self.transition_table.query(f"state == {state}")[
                str(input_string)
            ].to_list()[0]
            return out
        raise Exception("No such transition found!")


class DFA:
    def __init__(
        self, Q: list, Q0: int, F: int, transition_function: TransitionFunction
    ) -> None:
        """Creates a DFA using its tuple definition. Use the run() method to update state given an input string.
        Each state is defined using an unique integer value. -1 is reserved as a dead state.

        Args:
            Q (list): List of states
            Q0 (int): Initial state
            F (int): Final state
            transition_function (TransitionFunction): A TransitionFunction object used to define the transitions for the DFA
        """
        self.Q = Q
        self.Q0 = Q0
        self.F = F
        self.transition_function = transition_function
        self.current = Q0

    def run(self, input_string: str) -> None:
        """Updates the internal current state given the input string.

        Args:
            input_string (str): The input string for the transition function.
        """
        self.current = self.transition_function.run(self.current, input_string)

    @property
    def is_dead(self):
        return self.current == -1

    @property
    def is_sucessful(self):
        return self.current == self.F
