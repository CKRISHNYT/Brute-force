import sys  # Command-line arguments के लिए

def brut3force3(target_Pa55word):  
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{};':,./<>?"
    print("Starting brute force attack...")

    # Calculate password length
    Pa55word_length = len(target_Pa55word)

    # Initialize result variable
    result = [""] * Pa55word_length

    # Brute force logic
    for i in range(Pa55word_length):
        for char in characters:
            print(f"Trying: {char}")
            if char == target_Pa55word[i]:
                result[i] = char
                print(f"Character found: {char}")
                break
    # Join all found characters to form the password
    cracked_password = "".join(result)
    if cracked_password == target_Pa55word:
        print(f"Pa55word found: {cracked_password}")
    else:
        print("Failed to crack the Pa55word. Try again.")

# Command-line usage guide
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python brut3force3.py <target_pa55word>")
        print("\nExamples:")
        print("   python brut3force3.py abc123")
        print("   python brut3force3.py pa55word123")
        print("   python brut3force3.py !@#$%^&*()")
        sys.exit(1)

    target_pa55word = sys.argv[1]
    brut3force3(target_pa55word)