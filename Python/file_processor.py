import os

def process_file():
    # Step 1: Ask user for input filename
    filename = input("Enter the input filename (e.g., input.txt): ").strip()

    # Step 2: Check if file exists
    if not os.path.exists(filename):
        print(f"⚠ '{filename}' not found. Creating a new one with sample text...")
        with open(filename, "w") as f:
            f.write("Python is powerful.\n")
            f.write("File handling is important.\n")
            f.write("Practice makes perfect.\n")
            f.write("Learning by doing is fun.\n")
            f.write("Errors help us grow.\n")
        print(f"✅ Sample '{filename}' created. Please run the program again.")
        return  # Exit so user can rerun with real input

    try:
        # Step 3: Read existing file
        with open(filename, "r") as infile:
            content = infile.read()

        # Step 4: Modify content (example: uppercase + reverse)
        modified = content.upper()[::-1]

        # Step 5: Ask user for output filename
        output_file = input("Enter the output filename (e.g., output.txt): ").strip()
        if not output_file:
            output_file = "output.txt"  # default

        with open(output_file, "w") as outfile:
            outfile.write("=== MODIFIED CONTENT ===\n")
            outfile.write(modified)

        print(f"✅ Processing complete! Results written to '{output_file}'")

    except PermissionError:
        print(f"⚠ Permission denied: Cannot read/write '{filename}'.")
    except Exception as e:
        print(f"⚠ An unexpected error occurred: {e}")
    finally:
        print("🔹 Program finished.")

# Run the program
process_file()
