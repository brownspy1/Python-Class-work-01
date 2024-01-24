import os


def create_python_files(num_files=38, folder_path='./'):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Generate and create .py files
    for i in range(1, num_files + 1):
        file_name = f"file_{i}.py"
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, 'w') as file:
            file.write(f'# This Program by m.mahadi \n program number {i}")')

        print(f"File '{file_name}' created at '{file_path}'")


if __name__ == "__main__":
    create_python_files()
