import os

def clear_folder(dir1, try_clear=False):
    """
    This function clears the contents of a specified folder.
    """
    if try_clear is True:
        if os.path.isdir(dir1) is False:
            print(f"{dir1} is not a valid directory")
            return
        if os.path.exists(dir1) is False:
            print(f"{dir1} does not exist")
            return
        for file_name in os.listdir(dir1):
            file_path = os.path.join(dir1, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
            except Exception as e:
                print(f"An error occurred while trying to clear {dir1}: {e}")
    else:
        print("try_clear is set to False, not clearing folder.")

def count_words_in_file(file_path):
    """
    This function counts the number of words in a specified file.
    """
    try:
        with open(file_path,'r',encoding='utf8') as file:
            word_list = file.read().split()
            word_count = len(word_list)
            return word_count
    except Exception as e:
        print(f"An error occurred while trying to count words in {file_path}: {e}")

SUCCESS = True
COUNTER_FILE = 0
LINE_NUMBER = 0

def main():
    global SUCCESS, COUNTER_FILE, LINE_NUMBER

    try:
        clear_folder("my_folder", try_clear=True)
    except Exception as e:
        print(f"An error occurred while trying to clear the folder: {e}")
        SUCCESS = False

    if SUCCESS:
        try:
            word_count = count_words_in_file("my_file.txt")
            print(f"Number of words in file: {word_count}")
            COUNTER_FILE += 1
        except Exception as e:
            print(f"An error occurred while trying to count words in file: {e}")
            SUCCESS = False

if __name__ == "__main__":
    main()