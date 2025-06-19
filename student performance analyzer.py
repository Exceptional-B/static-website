def analyze_student_performance(name, *scores):
    if not scores:
        print(f"No scores provided for {name}.")
        return False

    total_tests = len(scores)
    average_score = sum(scores) / total_tests
    highest_score = max(scores)
    lowest_score = min(scores)
    passed = average_score >= 50

    print(f"\nPerformance Report for {name}")
    print(f"Total Tests: {total_tests}")
    print(f"Scores: {scores}")
    print(f"Average Score: {round(average_score, 2)}")
    print(f"Highest Score: {highest_score}")
    print(f"Lowest Score: {lowest_score}")
    print("Status: Passed ✅" if passed else "Status: Failed ❌")

    return passed

# Input section
student_name = input("Enter student's name: ")
scores_input = input("Enter scores separated by space: ")

# Convert input to integers
scores = list(map(int, scores_input.split()))

# Run the function
analyze_student_performance(student_name, *scores)
