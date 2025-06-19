def convert_score_to_point(score):
    if 70 <= score <= 100:
        return 5
    elif 60 <= score <= 69:
        return 4
    elif 50 <= score <= 59:
        return 3
    elif 45 <= score <= 49:
        return 2
    elif 40 <= score <= 44:
        return 1
    elif 0 <= score <= 39:
        return 0
    else:
        raise ValueError("Invalid score. Score must be between 0 and 100.")

def get_class_of_degree(cgpa):
    if 4.50 <= cgpa <= 5.00:
        return "First Class"
    elif 3.50 <= cgpa <= 4.49:
        return "Second Class Upper"
    elif 2.40 <= cgpa <= 3.49:
        return "Second Class Lower"
    elif 1.50 <= cgpa <= 2.39:
        return "Third Class"
    elif 1.00 <= cgpa <= 1.49:
        return "Pass"
    elif 0.00 <= cgpa <= 0.99:
        return "Fail"
    else:
        return "Invalid CGPA"

def main():
    print("Welcome to the CGPA Calculator!")
    
    points = []
    for i in range(1, 6):
        while True:
            try:
                score = float(input(f"Enter score for course {i} (0-100): "))
                point = convert_score_to_point(score)
                points.append(point)
                break
            except ValueError as ve:
                print(f"Error: {ve}. Please try again.")

    cgpa = sum(points) / len(points)
    degree_class = get_class_of_degree(cgpa)

    print("\n--- CGPA Result ---")
    print(f"CGPA: {cgpa:.2f}")
    print(f"Class of Degree: {degree_class}")

if __name__ == "__main__":
    main()
