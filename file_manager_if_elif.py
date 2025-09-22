import os
import shutil

def list_files(directory):
    if not os.path.exists(directory):
        print("Directory does not exist!")
        return
    files = os.listdir(directory)
    if not files:
        print("No files found in the directory")
    else:
        print("\nFiles and Folders:")
        for file in files:
            print(file)

def rename_file(directory, old_name, new_name):
    old_path = os.path.join(directory, old_name)
    new_path = os.path.join(directory, new_name)
    if not os.path.exists(old_path):
        print("File does not exist!")
        return
    os.rename(old_path, new_path)
    print("File renamed successfully!")

def delete_path(directory, name):
    path = os.path.join(directory, name)
    if os.path.isfile(path):
        os.remove(path)
        print("File deleted successfully!")
    elif os.path.isdir(path):
        shutil.rmtree(path)
        print("Directory deleted successfully!")
    else:
        print("The specified path does not exist.")

def create_directory(directory, folder_name):
    path = os.path.join(directory, folder_name)
    os.makedirs(path, exist_ok=True)
    print("Directory created successfully!")

def main():
    while True:
        print("\n--- File Management System ---")
        print("1. List Files")
        print("2. Rename File")
        print("3. Delete File/Directory")
        print("4. Create Directory")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            directory = input("Enter directory path: ")
            list_files(directory)
        elif choice == "2":
            directory = input("Enter directory path: ")
            old_name = input("Enter old file name: ")
            new_name = input("Enter new file name: ")
            rename_file(directory, old_name, new_name)
        elif choice == "3":
            directory = input("Enter directory path: ")
            name = input("Enter file or directory name to delete: ")
            delete_path(directory, name)
        elif choice == "4":
            directory = input("Enter directory path: ")
            folder_name = input("Enter new folder name: ")
            create_directory(directory, folder_name)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

