import password_recovery

def main():
    # Get the password and k from the user.
    password = input("Enter the password: ")
    k = int(input("Enter the number of letters that were inserted: "))

    # Create a PasswordRecovery object.
    password_recovery = password_recovery.PasswordRecovery(password, k)

    # Count the number of unsuccessful attempts.
    unsuccessful_attempts = password_recovery.count_unsuccessful_attempts()

    # Print the number of unsuccessful attempts.
    print(unsuccessful_attempts)

if __name__ == "__main__":
    main()
