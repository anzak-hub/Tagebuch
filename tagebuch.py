from datetime import datetime
import os


class Tagebuch:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def make_input(self):
        text_ = input("Enter some info about today: ")
        text_ = text_.strip()
        if text_:

            #get current datetime
            now = datetime.now()
            # Format date and time as string
            date_time_str = now.strftime("%Y-%m-%d %H-%M")
            date_time_str = date_time_str.replace(" ", "-")

            #create the file name
            file_name = self.folder_path + date_time_str + ".txt"

            # Open a file in write mode
            with open(file_name, 'w') as file:          

                # Write some text to the file
                file.write(text_ + "\n")

    def get_all_tagebuch_inputs(self):
        # List all files in the specified folder
        files = os.listdir(self.folder_path)

        for file_name in files:
            print(file_name)
        
        return files

    def get_all_tagebuch_input_per_word(self):
        #search files which contains a certain word
        text_ = input("Enter some info to search: ").strip()

        files_with_text = []

        files = self.get_all_tagebuch_inputs()
        for file_name in files:
            file_name = self.folder_path + file_name
            with open(file_name, 'r') as file:          

                for line in file:
                    if line.find(text_) != -1:
                        #the word is in the file
                        files_with_text.append(file_name)
                        break

        print("serach per words is successful")
        return files_with_text
        
if __name__ == "__main__":
    tagebuch = Tagebuch("tagebuch_sites/")
    tagebuch.make_input()

    tagebuch.get_all_tagebuch_inputs()

    files_with_words = tagebuch.get_all_tagebuch_input_per_word()
    if files_with_words:
        for file_name in files_with_words:
            print(file_name)
