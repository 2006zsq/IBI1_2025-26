## This script contains two main components:
##1. A function to predict protein mass from amino acid sequences
##2. A class and function for tracking nutritional data


# ============================================================================
# PART 1: Protein Mass Predictor
# ============================================================================

##Approach:
##- Create a dictionary mapping amino acid symbols to their residue masses
##- Define a function that takes an amino acid sequence string
##- Iterate through each character in the sequence
##- For each amino acid, look up its mass in the dictionary
##- Sum all masses and return the total
##- If an unknown amino acid is found, raise an error with clear message


def calculate_protein_mass(amino_acid_sequence):
    
    ##Calculate the total mass of a protein from its amino acid sequence.
    
    ##Parameters:
    ## amino_acid_sequence (str): A string of single-letter amino acid codes
    
    ##Returns:
    ##float: Total protein mass in atomic mass units (amu)
    
    ##Raises:
    ## ValueError: If an unknown amino acid symbol is encountered
    
    
    # Step 1: Define the dictionary of amino acid masses
    # Each key is the single-letter symbol, value is the monoisotopic mass in amu
    amino_acid_masses = {
        'G': 57.02,   # Glycine
        'A': 71.04,   # Alanine
        'S': 87.03,   # Serine
        'P': 97.05,   # Proline
        'V': 99.07,   # Valine
        'T': 101.05,  # Threonine
        'C': 103.01,  # Cysteine
        'I': 113.08,  # Isoleucine
        'L': 113.08,  # Leucine
        'N': 114.04,  # Asparagine
        'D': 115.03,  # Aspartic Acid
        'Q': 128.06,  # Glutamine
        'K': 128.09,  # Lysine
        'E': 129.04,  # Glutamic Acid
        'M': 131.04,  # Methionine
        'H': 137.06,  # Histidine
        'F': 147.07,  # Phenylalanine
        'R': 156.10,  # Arginine
        'Y': 163.06,  # Tyrosine
        'W': 186.08   # Tryptophan
    }
    
    # Step 2: Initialize total mass to zero
    total_mass = 0.0
    
    # Step 3: Convert sequence to uppercase to handle lowercase input
    sequence = amino_acid_sequence.upper()
    
    # Step 4: Process each amino acid in the sequence
    for i, amino_acid in enumerate(sequence):
        # Try to find the amino acid in our dictionary
        if amino_acid in amino_acid_masses:
            # Add its mass to the running total
            total_mass += amino_acid_masses[amino_acid]
        else:
            # If we can't find it, raise an error with helpful information
            raise ValueError(
                f"Unknown amino acid '{amino_acid}' found at position {i+1} "
                f"in sequence '{amino_acid_sequence}'. "
                f"Please use valid single-letter amino acid codes."
            )
    
    # Step 5: Return the calculated total mass
    return total_mass


# Example usage of the protein mass function
print("=" * 60)
print("PROTEIN MASS CALCULATOR DEMONSTRATION")
print("=" * 60)

# Example 1: Calculate mass of a short peptide "ACDE"
example_sequence = "ACDE"
try:
    mass = calculate_protein_mass(example_sequence)
    print(f"Sequence: {example_sequence}")
    print(f"Protein mass: {mass:.2f} amu")
except ValueError as e:
    print(f"Error: {e}")

# Example 2: Try with an invalid sequence to demonstrate error handling
invalid_sequence = "AXYZ"
try:
    mass = calculate_protein_mass(invalid_sequence)
    print(f"Sequence: {invalid_sequence}")
    print(f"Protein mass: {mass:.2f} amu")
except ValueError as e:
    print(f"\nError: {e}")

print()


# ============================================================================
# PART 2: Nutrition Data Tracker
# ============================================================================

##Approach:
##- Define a food_item class with attributes for nutritional information
##- The class constructor initializes name, calories, protein, carbs, and fat
##- Create a function that takes a list of food_item objects
##- Sum up all nutritional values across the food items
##- Check if total calories exceed 2500 or fat exceeds 90g
##- Display the results with warnings if thresholds are exceeded


class food_item:
    ##A class to represent a food item with nutritional information.
    
    ##Attributes:
    ##name (str): Name of the food item
    ##calories (float): Calories in the food item
    ##protein (float): Protein content in grams
    ##carbohydrates (float): Carbohydrate content in grams
    ##fat (float): Fat content in grams
    
    
    def __init__(self, name, calories, protein, carbohydrates, fat):
        
        ##Initialize a food_item object with nutritional data.
        
        ##Parameters:
        ##name (str): Name of the food
        ##calories (float): Caloric content
        ##protein (float): Protein in grams
        ##carbohydrates (float): Carbohydrates in grams
        ##fat (float): Fat in grams
        
        # Step 1: Store all nutritional information as instance attributes
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat
    
    def __str__(self):
        ##Return a string representation of the food item.
        return (f"{self.name}: {self.calories} cal, {self.protein}g protein, "
                f"{self.carbohydrates}g carbs, {self.fat}g fat")


def analyze_daily_intake(food_list):
    ##Calculate and report total nutritional intake from a list of food items.
    ##Warns if caloric intake exceeds 2500 calories or fat exceeds 90g.
    
    ##Parameters:
    ##food_list (list): List of food_item objects consumed in 24 hours
    
    ##Returns:
    ##dict: Dictionary containing total nutritional values
    
    
    # Step 1: Initialize totals for each nutritional category
    total_calories = 0.0
    total_protein = 0.0
    total_carbs = 0.0
    total_fat = 0.0
    
    # Step 2: Sum up nutritional values from all food items
    for food in food_list:
        total_calories += food.calories
        total_protein += food.protein
        total_carbs += food.carbohydrates
        total_fat += food.fat
    
    # Step 3: Display the daily summary
    print("DAILY NUTRITION SUMMARY")
    print("-" * 40)
    print(f"Total Calories: {total_calories:.1f} kcal")
    print(f"Total Protein:  {total_protein:.1f} g")
    print(f"Total Carbohydrates: {total_carbs:.1f} g")
    print(f"Total Fat: {total_fat:.1f} g")
    print("-" * 40)
    
    # Step 4: Check for excessive intake and display warnings
    warning_issued = False
    
    if total_calories > 2500:
        excess_calories = total_calories - 2500
        print(f"WARNING: Caloric intake exceeds 2500 kcal by {excess_calories:.1f} kcal!")
        print("   Consider reducing portion sizes or choosing lower-calorie options.")
        warning_issued = True
    
    if total_fat > 90:
        excess_fat = total_fat - 90
        print(f"WARNING: Fat intake exceeds 90g by {excess_fat:.1f} g!")
        print("   Consider choosing leaner protein sources and reducing fried foods.")
        warning_issued = True
    
    if not warning_issued:
        print("Daily intake is within recommended limits.")
    
    print()
    
    # Step 5: Return the totals as a dictionary for potential further use
    return {
        'calories': total_calories,
        'protein': total_protein,
        'carbohydrates': total_carbs,
        'fat': total_fat
    }


# Example usage of the nutrition tracker
print("=" * 60)
print("NUTRITION DATA TRACKER DEMONSTRATION")
print("=" * 60)

# Create some food items
breakfast = food_item("Oatmeal with banana", 350, 10, 65, 7)
morning_snack = food_item("Apple", 60, 0.3, 15, 0.5)
lunch = food_item("Chicken sandwich", 450, 35, 40, 15)
afternoon_snack = food_item("Greek yogurt", 130, 12, 9, 4)
dinner = food_item("Pasta with meatballs", 680, 30, 75, 28)
evening_snack = food_item("Ice cream (2 scoops)", 300, 5, 35, 18)

# Store all food items consumed in a day
daily_consumption = [breakfast, morning_snack, lunch, 
                     afternoon_snack, dinner, evening_snack]

# Display what was eaten
print("\nFood items consumed today:")
for i, food in enumerate(daily_consumption, 1):
    print(f"{i}. {food}")

print()

# Analyze the daily intake
results = analyze_daily_intake(daily_consumption)

print("=" * 60)