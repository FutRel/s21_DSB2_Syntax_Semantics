import sys

def create_employees_tsv(file_path):
    try:
        with open(file_path, 'r') as file:
            emails = [line.strip() for line in file if line.strip()]
        
        employees_data = []
        
        for email in emails:
            if '@corp.com' in email:
                local_part = email.split('@')[0]
                
                if '.' in local_part:
                    name_part, surname_part = local_part.split('.', 1)
                    
                    name = name_part.capitalize()
                    surname = surname_part.capitalize()
                    
                    row = f"{name}\t{surname}\t{email}"
                    employees_data.append(row)
        
        with open('employees.tsv', 'w') as tsv_file:
            tsv_file.write("Name\tSurname\tEmail\n")
            for row in employees_data:
                tsv_file.write(f"{row}\n")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    
    email_file_path = sys.argv[1]
    create_employees_tsv(email_file_path)