
# LOVE CALCULATOR

def calculate_love_score(
    name1 = input("Enter the name 1"), 
    name2 = input("Enter the name 2")):
    # Combine both names and convert to lowercase
    combined_names = (name1 + name2).lower()

    # Count letters in "TRUE"
    true_count = sum(combined_names.count(letter) for letter in "true")

    # Count letters in "LOVE"
    love_count = sum(combined_names.count(letter) for letter in "love")

    # Combine the counts to form the love score
    love_score = int(f"{true_count}{love_count}")

    print(f"Love Score = {love_score}")
    return love_score

calculate_love_score()




