'''
SecureIn
Problem Statement: The Doomed Dice Challenge

PART - A

You are given two six-sided dice, Die A and Die B, each with faces numbered from 1 to 6. You can only roll both the dice together, and your turn is guided by the obtained sum.

Problem statement:
Given that there are essentially two dice, dice A and dice B can be taken as [1,2,3,4,5,6] in the grid matrix.

1.	How many total combinations are possible? Show the math along with the code.
To find the total number of combinations, we can simply square the number of possibilities for one die. This is because each roll of one die can be paired with any of the 6 possibilities of the other die.
Total combinations = Possibilities for one die * Possibilities for the other die
  = 6 * 6
  = 36

So, there are 36 total combinations possible.
'''
# Import Libraries
from itertools import product
from collections import Counter

class Dice:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def total_combinations(self):
        return self.num_sides ** 2

    '''
    Calculate and display the distribution of all possible combinations that can be obtained when rolling both Die A and Die B together. Show the math along with the code!

    The function distributionCombinations creates a list of lists, where each inner list represents a combination of rolls for two six-sided dice (Die A and Die B). 
    It iterates through all possible values for Die A and Die B, appending each combination as a pair [Die A value, Die B value] to the list. 
    Finally, it returns the list containing all combinations. When executed in the main function, it prints out all possible combinations of rolls for Die A and Die B.
    '''
    def distribution_combinations(self):
        dieA = range(1, 7)
        dieB = range(1, 7)
        combinations_list = []
        for i in dieA:
            temp = []
            for j in dieB:
                temp.append([i, j])
            combinations_list.append(temp)
        return combinations_list

    '''
    Calculate the Probability of all Possible Sums occurring among the number of combinations from (2).
    Example: P(Sum = 2) = 1/X as there is only one combination possible to obtain Sum = 2. Die A = Die B = 1.

    To calculate the probability of all possible sums from 2 to 12, we need to consider all combinations of values from both dice. 
    The minimum sum occurs when both dice show a value of 1, and the maximum sum occurs when both dice show a value of 6. 
    We will iterate through all possible combinations of values for both dice, compute the sum, and then calculate the probability for each sum.
    '''
    def probability_sum(self):
        dieA = range(1, self.num_sides + 1)
        dieB = range(1, self.num_sides + 1)
        sums_list = []
        for i in dieA:
            for j in dieB:
                s = i + j
                sums_list.append(s)

        counts = {}
        prob = {}

        for i in sums_list:
            counts[i] = counts.get(i, 0) + 1

        for i in range(2, 2 * self.num_sides + 1):
            count_i = counts.get(i, 0)
            prob_i = count_i / len(sums_list)
            prob[i] = {"count": count_i, "prob": str(round(prob_i, 3))}

        return prob

    ''''
    PART - B
    You were happily spending a lazy afternoon playing your board game with your dice when suddenly the mischievous Norse God Loki (You love Thor too much & Loki didn't like that much) appeared. Loki dooms your dice for his fun removing all the "Spots" off the dice. No problem! You have the tools to re-attach the "Spots" back on the Dice. However, Loki has doomed your dice with the following conditions:

    Die A cannot have more than 4 Spots on a face.
    Die A may have multiple faces with the same number of spots.
    Die B can have as many spots on a face as necessary, i.e., even more than 6. But in order to play your game, the probability of obtaining the Sums must remain the same! So if you could only roll P(Sum=2) = 1/X, then the new dice must have the spots reattached such that those probabilities are not changed.
    Input:

    Die_A = [1, 2, 3, 4, 5, 6] & Die_B = Die_A = [1, 2, 3, 4, 5, 6]
    Output:

    A Transform Function undoom_dice that takes (Die_A, Die_B) as input & outputs New_Die_A = [?, ?, ?, ?, ?, ?], New_Die_B = [?, ?, ?, ?, ?, ?] where,
    No New_Die A[x] > 4
    '''

    def undoom_dice(self):
        combos = list(product(range(1, self.num_sides + 1), repeat=2))
        combos.sort(key=lambda x: sum(x))
        new_die_a = [0] * self.num_sides
        new_die_b = [0] * self.num_sides
        for i, combo in enumerate(combos):
            if combo[0] <= 4:
                if i < self.num_sides:
                    new_die_a[i] = combo[0]
                    new_die_b[i] = combo[1]
            else:
                if i < self.num_sides:
                    new_die_a[i] = combo[1]
                    new_die_b[i] = combo[0]
        return new_die_a, new_die_b


#main function
if __name__ == "__main__":
    dice = Dice(6)
    print("SecureIn Part - A", "\n")
    print("1. Total Combinations Possible by the Dice :", dice.total_combinations(), "\n")

    print("2. Distribution of all possible combinations: ", dice.distribution_combinations(), "\n")

    print("3. Probability of all Possible Sums occurring among the number of combinations:")
    probabilities = dice.probability_sum()
    for key, value in probabilities.items():
        print(f"Sum: {key}, Count: {value['count']}, Probability: {value['prob']}")
    print()

    print("SecureIn Part - B", "\n")
    new_die_a, new_die_b = dice.undoom_dice()
    print("4. Probability of Obtaining the Sum after reattachment :", "\n", new_die_a, "\n", new_die_b)