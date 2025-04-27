import csv
import argparse

def students_above_threshold(filename, threshold):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        print(f"Students with grade above {threshold}:")
        for row in reader:
            if float(row['grade']) > threshold:
                print(f" - {row['name']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List students above a grade threshold.")
    parser.add_argument('--filename', type=str, required=True, help='CSV filename (e.g., students.csv)')
    parser.add_argument('--threshold', type=float, required=True, help='Grade threshold')

    args = parser.parse_args()
    
    students_above_threshold(args.filename, args.threshold)

