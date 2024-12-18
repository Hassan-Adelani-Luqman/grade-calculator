#The Assignment class represents a single assignment. It stores details like the name, type, score, and weight, and calculates the contribution of the assignment to the final grade.
class Assignment:
    def __init__(self, name, type, score, weight):
        self.name = name
        self.type = type
        self.score = score
        self.weight = weight
        self.weighted_score = self.calculate_weighted_score()

    def calculate_weighted_score(self):
        return (self.score / 100) * self.weight
    


#The Student class manages a list of assignments and performs some actions
class Student:
    def __init__(self, name):
        self.name = name
        self.assignments = []
        
    # Adding assignments.
    def add_assignment(self, name, type, score, weight):
        if type not in ['FA', 'SA']:
            print(f"Invalid type for assignment {name}. Must be 'FA' or 'SA'.")
            return
        self.assignments.append(Assignment(name, type, score, weight))


# calculates the total contribution of all Formative and Summative assignments.
# It also checks that the weights don’t exceed the allowed limits (60% for Formative, 40% for Summative).
    def calculate_totals(self):
        formative_total = sum(a.weighted_score for a in self.assignments if a.type == 'FA')
        summative_total = sum(a.weighted_score for a in self.assignments if a.type == 'SA')
        formative_weight = sum(a.weight for a in self.assignments if a.type == 'FA')
        summative_weight = sum(a.weight for a in self.assignments if a.type == 'SA')

        if formative_weight > 60 or summative_weight > 40:
            print("Weights exceeded: Formative (60%), Summative (40%)")
        return formative_total, summative_total


# The program checks if the student has met the required scores in both Formative (≥30%) and Summative (≥20%) groups.
# If either requirement isn’t met, the student fails.
    def check_progression(self):
        formative_total, summative_total = self.calculate_totals()
        passed = formative_total >= 30 and summative_total >= 20
        status = "Passed" if passed else "Failed"
        print(f"Formative Total: {formative_total:.2f}%, Summative Total: {summative_total:.2f}%")
        print(f"Status: {status}")
        return status


# The program identifies Formative assignments with scores below 50%.
# It lists these assignments so the student knows what to resubmit.
    def check_resubmissions(self):
        resubmissions = [a for a in self.assignments if a.type == 'FA' and a.score < 50]
        if resubmissions:
            print("Eligible for Resubmission:")
            for a in resubmissions:
                print(f"  {a.name} - Score: {a.score}%")
        else:
            print("No assignments eligible for resubmission.")


# The program sorts assignments based on their scores in ascending order.
# It then displays the list as a formatted table.
    def display_transcript(self, order='ascending'):
        reverse = order == 'descending'
        sorted_assignments = sorted(self.assignments, key=lambda a: a.score, reverse=reverse)
        print("\nTranscript Breakdown:")
        print("Assignment          Type            Score(%)    Weight (%)")
        print("-----------------------------------------------------------")
        for a in sorted_assignments:
            print(f"{a.name:<18} {a.type:<15} {a.score:<12} {a.weight:<10}")
        print("-----------------------------------------------------------")


# Example usage:
if __name__ == "__main__":
    student = Student("Hassan Ade")

    # Adding assignments
    student.add_assignment("OOP", "FA", 45, 15)
    student.add_assignment("PLD 1", "FA", 90, 10)
    student.add_assignment("Live Coding", "FA", 45, 10)
    student.add_assignment("Individual Lab", "FA", 80, 15)
    student.add_assignment("Pre-reading", "FA", 48, 10)
    student.add_assignment("PLD 2", "SA", 34, 20)
    student.add_assignment("PLD 3", "SA", 95, 20)

    # Checking progression
    student.check_progression()

    # Checking resubmission eligibility
    student.check_resubmissions()

    # Displaying transcript
    student.display_transcript(order='ascending')
