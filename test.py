import schelling

def main():
    populations = [0.6, 0.8]
    thresholds = [3, 4]
    iterations = 20

    for population in populations:
        for threshold in thresholds:
            model = schelling.Schelling(population, threshold)
            model.run_sim(iterations * 2500)
    
    

if __name__ == "__main__":
    main()