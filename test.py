import schelling

def main():
    print("This is the main function")
    model = schelling.Schelling(0.8, 4)
    model.run_sim(100)
    

if __name__ == "__main__":
    main()