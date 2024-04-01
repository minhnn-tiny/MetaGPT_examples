import tournament

def main():
    """
    The main function.
    """

    # Create a tournament with 8 chefs.
    chefs = [
        tournament.Chef("Chef 1", 0),
        tournament.Chef("Chef 2", 0),
        tournament.Chef("Chef 3", 0),
        tournament.Chef("Chef 4", 0),
        tournament.Chef("Chef 5", 0),
        tournament.Chef("Chef 6", 0),
        tournament.Chef("Chef 7", 0),
        tournament.Chef("Chef 8", 0),
    ]
    tournament_obj = tournament.Tournament(chefs)

    # Simulate the tournament.
    final_chefs = tournament_obj.simulate()

    # Calculate the expected difference in prize tokens between the final two competitors.
    expected_difference = tournament_obj.get_expected_difference()

    # Print the results.
    print("The final two chefs are:")
    for chef in final_chefs:
        print(f"  {chef.get_name()}")
    print(f"The expected difference in prize tokens between the final two competitors is: {expected_difference}")

if __name__ == "__main__":
    main()
