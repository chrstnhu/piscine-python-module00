# A cookbook is a dictionary that stores (recipe name, ingredients, meal, prep_time)
cookbook = {
    'Sandwich': {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": "10"
    },
    'Cake': {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": "60"
    },
    'Salad': {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": "15"
    }
}

# List of type of meal
mealType = ["breakfast", "brunch", "dinner", "lunch", "supper", "midnight Snack", "snack", "dessert"]

# A function that prints all the recipe in string
def printCookBook():
    """
    This function prints all the cookbook
    """
    for recipe_name, recipe in cookbook.items():
        ingredients = ", ".join(recipe['ingredients'][:-1])
        last_ingredient = recipe['ingredients'][-1]
        
        # Affichage des ingrédients
        print(f"The {recipe_name}'s ingredients are {ingredients} and {last_ingredient}.")
        print(f"It is a {recipe['meal']} and it takes {recipe['prep_time']} minutes of preparation.")


# A function that prints all recipe names.
def printRecipeName():
    """
    This function prints the names of all the recipes.
    """
    
    for keyName in cookbook:
        print("Name:" , keyName)

# A function that takes a recipe name and prints its details.
def printDetails(string = None):
    """
    This function print the details of a recipe.
    """

    # Enter a recipe name
    while string == "" or string is None:
        print("Please enter a recipe name to get its details: ")
        string = input(">> ")

    # Print details
    if string in cookbook:
        recipe = cookbook[string]
        print("\nRecipe for", string, ":")
        print("\tIngredients list: ['", "', '".join(recipe['ingredients']), "']")
        print("\tTo be eaten for", recipe['meal'])
        print("\tTaken", recipe['prep_time'], "minutes of cooking.")
    else:
        print("Invalid name, check name with option 4")


# A function that takes a recipe name and delete it.
def deleteRecipe(string = None):
    """
    This function delete a recipe.
    """

    # Enter a recipe name
    while string == "" or string is None:
        print("Please insert a recipe name: ")
        string = input(">> ")

    # Delete the name
    if string in cookbook:
        cookbook.pop(string)
        print("Delete", string, "recipe")
    else:
        print("Invalid name, check name with option 4")


# A function that adds a recipe from user input
def addRecipe():
    """
    This function add a new recipe from user input
    """

    # Add recipe (key)
    print("Enter a name:")
    name = input()
    while name == "":
        name = input("Need a name: ")

    # Add list of ingredient
    ingredients = []
    print("Enter ingredients: ")
    element = input()
    while element == "":
        element = input("Need a ingredient: ")
    while element != "":
        ingredients.append(element)
        element = input()

    # Add meal type
    print("Enter a meal type:")
    meal = input()
    while meal not in mealType:
        print(f"Invalid type name: {meal}. Please try again with", mealType)
        meal = input()

    # Add preparation time
    print("Enter a prepation time:")
    prep_time = input()
    while not prep_time.isdigit():
        prep_time = input("Insert a valid time: ")

    cookbook[name] = {
        'ingredients' : ingredients,
        'meal' : meal,
        'prep_time' : prep_time
    }
        

def printOption():
    print("""List of available options:
                1: Add a recipe
                2: Delete a recipe
                3: Print a recipe
                4: Print the cookbook
                5: Quit""")

# In terminal
if __name__ == "__main__":
    print("Welcome to the Python Cookbook !")
    printOption()
    while True:
        print("\nPlease select an option: ")
        option = input(">> ")
        if option == '1':
            addRecipe()
        elif option == '2':
            deleteRecipe()
        elif option == '3':
            printDetails()
        elif option == '4':
            printRecipeName()
        elif option == '5':
            print("Cookbook closed. Goodbye !")
            break
        else:
            print("Sorry, this option does not exist.")
            printOption()