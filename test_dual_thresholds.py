import schelling_dual_thresholds

def main():
    populations = [0.6, 0.8]
    thresholds = [3, 4]
    iterations1 = 20
    iterations2 = 40

    for population in populations:
        for threshold in thresholds:
            model = schelling_dual_thresholds.schelling_dual_thresholds(population, threshold)
            model.run_sim(iterations1 * 2500)
        model = schelling_dual_thresholds.schelling_dual_thresholds(population, 5, 3, .2)
        model.run_sim(iterations2 * 2500)
        
    
    

if __name__ == "__main__":
    main()