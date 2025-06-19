def calculate_gpa(scores):
    total_points = 0

    for score in scores:
        if 70 <= score <= 100:
            total_points += 5
        elif 60 <= score < 70:
            total_points += 4
        elif 50 <= score < 60:
            total_points += 3
        elif 45 <= score < 50:
            total_points += 2
        elif 0 <= score < 45:
            total_points += 0
        else:
            print(f"Invalid score: {score}")
            return None  # stops if a score is invalid

    gpa = total_points / len(scores)
    return gpa


# 🟢 INPUT PART
try:
    # Ask user to input scores separated by commas
    raw_input = input("Enter your course scores (0–100) separated by commas: ")
    
    # Split input into a list of integers
    scores = [int(score.strip()) for score in raw_input.split(',')]
    
    # Calculate GPA
    gpa = calculate_gpa(scores)
    
    if gpa is not None:
        print(f"✅ Your GPA is: {gpa:.2f}")
except ValueError:
    print("❌ Please enter only numbers separated by commas (e.g. 78, 65, 90).")
