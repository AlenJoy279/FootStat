import os

def get_monthly_html_files(directory):

    dates = ["March 2020", "April 2020", "May 2020", "June 2020", "July 2020",
             "August 2020", "September 2020", "October 2020", "November 2020", "December 2020", "January 2021",
             "February 2021", "March 2021", "April 2021", "May 2021", "June 2021", "July 2021",
             "August 2021", "September 2021", "October 2021", "November 2021", "December 2021", "January 2022",
             "February 2022", "March 2022", "April 2022", "May 2022", "June 2022", "July 2022",
             "August 2022", "September 2022", "October 2022", "November 2022", "December 2022"]

    monthly_plots = [] # add all monthly plots, these will be ordered chronologically

    for date in dates:
        for file in os.listdir(directory):
            if file == "Sentiments " + date: # if file date is equal to the date being checked, then open file and copy its data
                file_path = os.path.join(directory, file)
                with open(file_path, "r") as f:
                    html_code = f.read()
                    monthly_plots.append(html_code)
    return monthly_plots

def get_yearly_html_files(directory): # search throuhg files in path, read files and copy what is in them
    yearly = []
    for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            with open(file_path, "r") as f:
                html_code = f.read()
                yearly.append(html_code)
    return yearly

