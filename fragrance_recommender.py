print("===================================")
print("   AI Fragrance Recommender")
print("===================================")

print("\nWhat type of fragrance do you like?")
print("1. Fresh")
print("2. Sweet")
print("3. Woody")
print("4. Floral")

choice = input("\nEnter your choice (1-4): ")

if choice == "1":
    print("\nRecommended fragrance family:")
    print("- Citrus")
    print("- Aquatic")
    print("- Green")

elif choice == "2":
    print("\nRecommended fragrance family:")
    print("- Vanilla")
    print("- Caramel")
    print("- Tonka Bean")

elif choice == "3":
    print("\nRecommended fragrance family:")
    print("- Sandalwood")
    print("- Cedarwood")
    print("- Vetiver")

elif choice == "4":
    print("\nRecommended fragrance family:")
    print("- Rose")
    print("- Jasmine")
    print("- Orange Blossom")

else:
    print("\nInvalid choice. Please run the program again.")
