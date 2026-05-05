import sys

def generate_welcome_letter():
    try:
        with open('employees.tsv', 'r') as tsv_file:
            lines = tsv_file.readlines()
        
        for line in lines[1:]:
            if line.strip():
                name, surname, stored_email = line.strip().split('\t')
                
                welcome_letter = (
                    f"Dear {name}, welcome to our team! We are sure that it will be "
                    f"a pleasure to work with you. That's a precondition for the "
                    f"professionals that our company hires."
                )
                print(welcome_letter)
        
        
    except FileNotFoundError:
        return "Error"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    generate_welcome_letter()