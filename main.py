from dfa import DFA, TransitionFunction


def main():
    tf = TransitionFunction("definitions/bacteria_automata.csv")
    Q = tf.states
    Q0 = 0
    F = 5
    automaton = DFA(Q, Q0, F, tf)
    states = {
        0: "Initial",
        1: "Compact Structure",
        2: "Dense Branching",
        3: "Meagerly Spaced Branching",
        4: "Sparse Branching",
        5: "Dead State",
    }

    for k in states.keys():
        print(f"{k} : {states[k]}")

    while True:
        print("The current state of the DFA is", states[automaton.current])
        print("Enter the strategy to adopt (a-e), Q to quit: ")
        strat = input(">>> ")
        if strat.upper() == "Q":
            break
        print("#" * 10)
        automaton.run(strat)
    print("Thank you for playing!")


if __name__ == "__main__":
    main()
