from bacteria import Colony, Simulator


def main():
    sim = Simulator()
    col = Colony(sim)

    print(col.growthVec, col.posVec)


if __name__ == "__main__":
    main()
