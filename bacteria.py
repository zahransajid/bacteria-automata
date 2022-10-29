from __future__ import annotations
import numpy as np
from dfa import DFA, TransitionFunction


class Simulator:
    def __init__(self, growthMat: np.ndarray, strategy: str) -> None:
        """Creates a simulator to find the growth of bacteria in a medium.

        Args:
            growthMat (np.ndarray): The medium to grow in, the intensity of values models the harshness of the environment
            strategy (str): The strategy to be adopted for colonies in general can be a character a-e representing chance for a colony to defect

        Raises:
            ValueError: The growth matrix must be a square martrix
        """
        self.growthMat = np.ndarray
        if self.growthMat.shape[0] != self.growthMat.shape[1]:
            raise ValueError("The given growth matrix must be a square matrix")
        self.sideLength = 15
        self.tf = TransitionFunction(r"definitions\DFA1.csv")
        self.states = self.tf.states
        self.automaton = DFA(self.states, 0, 5, self.tf)
        self.colonies = []
        self.strategies = {
            "a": 1,
            "b": 0.75,
            "c": 0.5,
            "d": 0.25,
            "e": 0,
        }
        self.strategy = strategy

        self.branching_state = {0: "I", 1: "CS", 2: "DB", 3: "MSB", 4: "SB", 5: "DS"}

    def getInitVectors(self, col: Colony) -> tuple:
        """Initialises a colony with its position and growth vectors, similar to position and velocity vectors.
        Also adds the colony to the internal list of colonies.

        Args:
            col (Colony): A colony object

        Returns:
            tuple: The position,growth vector pair
        """
        x = np.random.random() * np.random.choice([1, -1])
        y = np.sqrt(1 - x**2) * np.random.choice([1, -1])
        pos = np.array([x, y], dtype=np.float64)
        self.colonies.append(col)
        return (pos, pos * (np.random.random() * 0.5 + 1))

    def updateVectors(self, col: Colony) -> np.ndarray:
        # TO BE IMPLEMENTED
        pass

    def lookupGrowthMat(self, posVec: np.ndarray):
        """Looks up the growth matrix to find harshness within a point bound by (sidelength,sidelength)

        Args:
            posVec (np.ndarray): Position vector to look up

        Returns:
            float: intensity at that point
        """
        pos = (posVec / self.sideLength) + np.array(
            [15 / 2, 15 / 2], dtype=np.float32
        )  # shift to centre
        pos = self.growthMat.shape[0] * pos
        pos = np.array(pos, dtype=np.int32)
        return self.growthMat[pos]

    def PI_C(self) -> float:
        """Payoff to cooperate, used to update growth vectors

        Returns:
            float: The payoff value between 3 and 0
        """
        return (3 * self.strategies[self.strategy]) / len(self.colonies)

    def PI_D(self) -> float:
        """Payoff to defect, used to update growth matrix

        Returns:
            float: payoff value between 5 and 1
        """
        x = self.strategies[self.strategy]
        n = len(self.colonies)
        return (5 * x + n - x + 1) / (n - 1)

    def randDefect(self) -> bool:
        """Whether to defect or not calculated based on strategy adopted

        Returns:
            bool: To defect
        """
        return np.random.random() > self.strategies[self.strategy]


class Colony:
    def __init__(self, sim: Simulator):
        self.sim = sim
        self.posVec, self.growthVec = self.sim.getInitVectors(self)
        self.state = 0
        self.toDefect = self.sim.randDefect()
        pass
