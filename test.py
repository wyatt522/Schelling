import schelling

def main():
    print("This is the main function")
    model = schelling.Schelling(0.8, 3)
    model.plot_map()
    print(model.count_neighbors(1, (0,0)))

if __name__ == "__main__":
    main()