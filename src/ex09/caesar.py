import sys

def caesar_cipher(text, shift, mode='encode'):
    result = []
    
    for char in text:
        char_code = ord(char)
        
        if (1040 <= char_code <= 1103) or (1025 <= char_code <= 1035) or (1105 <= char_code <= 1115):
            raise ValueError("Language error.")
        
        if 'a' <= char <= 'z':
            current_shift = shift if mode == 'encode' else -shift
            
            pos = ord(char) - ord('a')
            
            new_pos = (pos + current_shift) % 26
            
            new_char = chr(ord('a') + new_pos)
            result.append(new_char)
            
        elif 'A' <= char <= 'Z':
            current_shift = shift if mode == 'encode' else -shift
            pos = ord(char) - ord('A')
            new_pos = (pos + current_shift) % 26
            new_char = chr(ord('A') + new_pos)
            result.append(new_char)
            
        else:
            result.append(char)
    
    return ''.join(result)

def main():
    if len(sys.argv) != 4:
        raise ValueError("Error")
    
    mode = sys.argv[1]
    text = sys.argv[2]
    
    if mode not in ['encode', 'decode']:
        raise ValueError("Error")
    
    try:
        shift = int(sys.argv[3])
    except ValueError:
        raise ValueError("Error")
    
    result = caesar_cipher(text, shift, mode)
    print(result)

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)