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
        
if __name__ == "__main__":
    tagebuch = Tagebuch("tagebuch_sites/")
    tagebuch.make_input()

    tagebuch.get_all_tagebuch_inputs()