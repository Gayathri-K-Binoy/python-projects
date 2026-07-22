import random

print("RANDOM RECIPE GENERATOR ")
flavors=["lemon","peach","herb","cheese","spicy","sweet and sour"]
methods=["baked","grilled","roasted","stir-fried"]
proteins=["tofu","chicken",'fish','beef','eggs']
veggies=["spinach","bell peppers","carrot","mushrooms","tomato"]
carbs=["quinoa","pasta","rice","bread","potatoes"]



while True:
    flavor=random.choice(flavors)
    method=random.choice(methods)
    protein=random.choice(proteins)
    veggie=random.choice(veggies)
    carb=random.choice(carbs)
    print(f"\nYour random recipe: {flavor} {method} {protein} with {veggie} and {carb}")

    if not input("\nGenerate another recipe? (y/n): ").lower().startswith("y"):
        print("Goodbye!")
        break