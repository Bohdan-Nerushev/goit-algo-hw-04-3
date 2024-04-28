def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            lines = [el.strip() for el in fh.readlines()]
            if not lines:
                return None, None  # Empty file
            count = 0
            total = 0
            for line in lines:
                try:
                    salary = int(line.split(',')[1])
                    total += salary
                    count += 1
                except (IndexError, ValueError):
                    pass  # Ignore lines with incorrect format or missing salary
            if count == 0:
                return 0, 0  # No valid salaries found
            average = total / count
            return total, average
    except (FileNotFoundError, PermissionError):
        return None, None  # File not found or permission error

# Example usage
path = 'C:/Users/Lenovo/Desktop/qwert.txt'  # Provide the full path here
total, average = total_salary(path)
print(f"Total salary: {total}, Average salary: {average}")
