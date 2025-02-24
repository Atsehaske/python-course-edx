import sys
import csv

def main():
    ''' main function '''
    before, after = arg_checks()
    students_list = read(before)
    write(after, students_list)

def write(after, students_list):
        ''' writes data to file '''
        fieldnames=['first', 'last', 'house']
        students_dict = dict(zip(fieldnames, students_list))
        with open(after, 'w+', newline='') as file:
            csvwriter = csv.DictWriter(file, fieldnames=fieldnames, delimiter = ',')
            csvwriter.writeheader()
            for student in students_list:
                csvwriter.writerow(student)

def read(before):
    ''' reads csv file and prepares data '''
    students = []
    try:
        with open(before) as file:
             reader = csv.DictReader(file)
             for row in reader:
                 last, first = row["name"].split(", ")
                 students.append({"first": first, "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit("Could not read "+before)
    return students

def arg_checks():
    ''' check if args are correct '''
    try:
        if len(sys.argv) < 3:
            e = "Too few command-line arguments"
            raise Exception
        if len(sys.argv) > 3:
            e = "Too many command-line arguments"
            raise Exception
    except Exception:
        sys.exit(e)
    return sys.argv[1], sys.argv[2]

if __name__ == "__main__":
    main()
