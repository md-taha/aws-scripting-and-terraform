import csv

def students_above_threshold(filename, threshold):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        print(f"Students with grade above {threshold}:")
        for row in reader:
            if float(row['grade']) > threshold:
                print(f" - {row['name']}")

if __name__ == "__main__":
    filename = input("Enter CSV filename (e.g., students.csv): ")
    threshold = float(input("Enter grade threshold: "))
    students_above_threshold(filename, threshold)

