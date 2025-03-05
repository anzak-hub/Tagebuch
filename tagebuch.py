from datetime import datetime


class Tagebuch:
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
            file_name = "tagebuch_sites/" + date_time_str + ".txt"

            # Open a file in write mode
            with open(file_name, 'w') as file:          

                # Write some text to the file
                file.write(text_ + "\n")

    


if __name__ == "__main__":
    tagebuch = Tagebuch()
    tagebuch.make_input()