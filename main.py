from WeatherRequest import WeatherRequest
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk



# First line, initialize main parent window
root = tk.Tk()



# Configure root
root.title('Weather')
root.geometry('550x200')
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.configure(bg='#4c02cc')
root.attributes('-alpha', 0.9)



# Background image function
def set_background_image(frame_name):
    """Sets the background image"""

    background_image = ImageTk.PhotoImage(file=r'C:\Users\Bla125\PythonDev\WeatherApp\istockphoto-531889697-170667a.jpg')
    background_label = ttk.Label(frame_name, image=background_image)
    background_label.image = background_image # Avoid garbage collection
    background_label.place(x=0,y=0,relwidth=1,relheight=1)



# Search box frame
search_box = ttk.LabelFrame(root, text='Search')
search_box.grid(row=0, sticky=tk.N + tk.E + tk.S + tk.W, padx=5, pady=5)
search_box.columnconfigure(0, weight=1)
search_box_var = tk.StringVar()
ttk.Entry(search_box, textvariable=search_box_var).grid(sticky=tk.E + tk.W, padx=5)




# Main subframe that holds all frames in tabs
main_subframe = ttk.Notebook(root)
main_subframe.grid(row=1, sticky=tk.N + tk.E + tk.S + tk.W, padx=5, pady=5)
main_subframe.enable_traversal()


##########################################################
# Today subframe which holds everything in the today tab #
##########################################################
today_frame = ttk.Frame(main_subframe)
main_subframe.add(today_frame, text='Today', underline=0)
set_background_image(today_frame)

# Labels containing the weather info for the today subframe 
td_temp_label = ttk.Label(today_frame, text='')
td_temp_label.grid(sticky=tk.W, padx=5, pady=5)
td_phrase_label = ttk.Label(today_frame, text='')
td_phrase_label.grid(sticky=tk.W, padx=5, pady=5)
td_temp_hilo_label = ttk.Label(today_frame, text='')
td_temp_hilo_label.grid(sticky=tk.W, padx=5, pady=5)



############################################################
# Hourly subframe which holds everything in the hourly tab #
############################################################
hourly_frame = ttk.Frame(main_subframe)
main_subframe.add(hourly_frame, text='Hourly', underline=0)
set_background_image(hourly_frame)

# Labels containing the info for the hourly subframe
hr_time1_label = ttk.Label(hourly_frame, text='')
hr_time1_label.grid(row=0, column=0, padx=1, pady=1)
hr_temp1_label = ttk.Label(hourly_frame, text='')
hr_temp1_label.grid(row=0, column=1, padx=1, pady=1)
hr_cond1_label = ttk.Label(hourly_frame, text='')
hr_cond1_label.grid(row=0, column=2, padx=1, pady=1)
hr_precip1_label = ttk.Label(hourly_frame, text='')
hr_precip1_label.grid(row=0, column=3, padx=1, pady=1)

hr_time2_label = ttk.Label(hourly_frame, text='')
hr_time2_label.grid(row=1, column=0, padx=1, pady=1)
hr_temp2_label = ttk.Label(hourly_frame, text='')
hr_temp2_label.grid(row=1, column=1, padx=1, pady=1)
hr_cond2_label = ttk.Label(hourly_frame, text='')
hr_cond2_label.grid(row=1, column=2, padx=1, pady=1)
hr_precip2_label = ttk.Label(hourly_frame, text='')
hr_precip2_label.grid(row=1, column=3, padx=1, pady=1)

hr_time3_label = ttk.Label(hourly_frame, text='')
hr_time3_label.grid(row=2, column=0, padx=1, pady=1)
hr_temp3_label = ttk.Label(hourly_frame, text='')
hr_temp3_label.grid(row=2, column=1, padx=1, pady=1)
hr_cond3_label = ttk.Label(hourly_frame, text='')
hr_cond3_label.grid(row=2, column=2, padx=1, pady=1)
hr_precip3_label = ttk.Label(hourly_frame, text='')
hr_precip3_label.grid(row=2, column=3, padx=1, pady=1)

hr_time4_label = ttk.Label(hourly_frame, text='')
hr_time4_label.grid(row=3, column=0, padx=1, pady=1)
hr_temp4_label = ttk.Label(hourly_frame, text='')
hr_temp4_label.grid(row=3, column=1, padx=1, pady=1)
hr_cond4_label = ttk.Label(hourly_frame, text='')
hr_cond4_label.grid(row=3, column=2, padx=1, pady=1)
hr_precip4_label = ttk.Label(hourly_frame, text='')
hr_precip4_label.grid(row=3, column=3, padx=1, pady=1)

hr_time5_label = ttk.Label(hourly_frame, text='')
hr_time5_label.grid(row=4, column=0, padx=1, pady=1)
hr_temp5_label = ttk.Label(hourly_frame, text='')
hr_temp5_label.grid(row=4, column=1, padx=1, pady=1)
hr_cond5_label = ttk.Label(hourly_frame, text='')
hr_cond5_label.grid(row=4, column=2, padx=1, pady=1)
hr_precip5_label = ttk.Label(hourly_frame, text='')
hr_precip5_label.grid(row=4, column=3, padx=1, pady=1)



############################################################
# Ten day frame which holds everything in the five day tab #
############################################################
five_day_frame = ttk.Frame(main_subframe)
main_subframe.add(five_day_frame, text='5 Day', underline=0)
set_background_image(five_day_frame)

fd_day1_label = ttk.Label(five_day_frame, text='')
fd_day1_label.grid(row=0, column=0, padx=1, pady=1)
fd_temp1_hi_label = ttk.Label(five_day_frame, text='')
fd_temp1_hi_label.grid(row=1, column=0, padx=1, pady=1)
fd_temp1_lo_label = ttk.Label(five_day_frame, text='')
fd_temp1_lo_label.grid(row=2, column=0, padx=1, pady=1)
fd_cond1_label = ttk.Label(five_day_frame, text='')
fd_cond1_label.grid(row=3, column=0, padx=1, pady=1)
fd_precip1_label = ttk.Label(five_day_frame, text='')
fd_precip1_label.grid(row=4, column=0, padx=1, pady=1)

fd_day2_label = ttk.Label(five_day_frame, text='')
fd_day2_label.grid(row=0, column=1, padx=1, pady=1)
fd_temp2_hi_label = ttk.Label(five_day_frame, text='')
fd_temp2_hi_label.grid(row=1, column=1, padx=1, pady=1)
fd_temp2_lo_label = ttk.Label(five_day_frame, text='')
fd_temp2_lo_label.grid(row=2, column=1, padx=1, pady=1)
fd_cond2_label = ttk.Label(five_day_frame, text='')
fd_cond2_label.grid(row=3, column=1, padx=1, pady=1)
fd_precip2_label = ttk.Label(five_day_frame, text='')
fd_precip2_label.grid(row=4, column=1, padx=1, pady=1)

fd_day3_label = ttk.Label(five_day_frame, text='')
fd_day3_label.grid(row=0, column=2, padx=1, pady=1)
fd_temp3_hi_label = ttk.Label(five_day_frame, text='')
fd_temp3_hi_label.grid(row=1, column=2, padx=1, pady=1)
fd_temp3_lo_label = ttk.Label(five_day_frame, text='')
fd_temp3_lo_label.grid(row=2, column=2, padx=1, pady=1)
fd_cond3_label = ttk.Label(five_day_frame, text='')
fd_cond3_label.grid(row=3, column=2, padx=1, pady=1)
fd_precip3_label = ttk.Label(five_day_frame, text='')
fd_precip3_label.grid(row=4, column=2, padx=1, pady=1)

fd_day4_label = ttk.Label(five_day_frame, text='')
fd_day4_label.grid(row=0, column=3, padx=1, pady=1)
fd_temp4_hi_label = ttk.Label(five_day_frame, text='')
fd_temp4_hi_label.grid(row=1, column=3, padx=1, pady=1)
fd_temp4_lo_label = ttk.Label(five_day_frame, text='')
fd_temp4_lo_label.grid(row=2, column=3, padx=1, pady=1)
fd_cond4_label = ttk.Label(five_day_frame, text='')
fd_cond4_label.grid(row=3, column=3, padx=1, pady=1)
fd_precip4_label = ttk.Label(five_day_frame, text='')
fd_precip4_label.grid(row=4, column=3, padx=1, pady=1)

fd_day5_label = ttk.Label(five_day_frame, text='')
fd_day5_label.grid(row=0, column=4, padx=1, pady=1)
fd_temp5_hi_label = ttk.Label(five_day_frame, text='')
fd_temp5_hi_label.grid(row=1, column=4, padx=1, pady=1)
fd_temp5_lo_label = ttk.Label(five_day_frame, text='')
fd_temp5_lo_label.grid(row=2, column=4, padx=1, pady=1)
fd_cond5_label = ttk.Label(five_day_frame, text='')
fd_cond5_label.grid(row=3, column=4, padx=1, pady=1)
fd_precip5_label = ttk.Label(five_day_frame, text='')
fd_precip5_label.grid(row=4, column=4, padx=1, pady=1)



#######################
# Search bar function #
#######################
def search_weather(*args):
    """Search for the weather in the input location and update weather labels"""

    # Get the input entered into the search bar
    search = search_box_var.get()
    print('Beginning search')

    # Call the WeatherRequest class and get_weather_info method to begin obtaining the weather info
    weather_info = WeatherRequest.get_weather_info(search)
    print('End search')

    # Update the labels to show the weather info
    # Today labels
    td_temp_label.configure(text=weather_info['today_temp'])
    td_phrase_label.configure(text=weather_info['today_phrase'])
    td_temp_hilo_label.configure(text=weather_info['today_temp_hilo'])

    # Hourly labels
    hr_time1_label.configure(text=weather_info['hr_time1'])
    hr_temp1_label.configure(text=weather_info['hr_temp1'])
    hr_cond1_label.configure(text=weather_info['hr_cond1'])
    hr_precip1_label.configure(text=weather_info['hr_precip1'])

    hr_time2_label.configure(text=weather_info['hr_time2'])
    hr_temp2_label.configure(text=weather_info['hr_temp2'])
    hr_cond2_label.configure(text=weather_info['hr_cond2'])
    hr_precip2_label.configure(text=weather_info['hr_precip2'])

    hr_time3_label.configure(text=weather_info['hr_time3'])
    hr_temp3_label.configure(text=weather_info['hr_temp3'])
    hr_cond3_label.configure(text=weather_info['hr_cond3'])
    hr_precip3_label.configure(text=weather_info['hr_precip3'])

    hr_time4_label.configure(text=weather_info['hr_time4'])
    hr_temp4_label.configure(text=weather_info['hr_temp4'])
    hr_cond4_label.configure(text=weather_info['hr_cond4'])
    hr_precip4_label.configure(text=weather_info['hr_precip4'])
    
    hr_time5_label.configure(text=weather_info['hr_time5'])
    hr_temp5_label.configure(text=weather_info['hr_temp5'])
    hr_cond5_label.configure(text=weather_info['hr_cond5'])
    hr_precip5_label.configure(text=weather_info['hr_precip5'])

    # Five day labels
    fd_day1_label.configure(text=weather_info['fd_day1'])
    fd_temp1_hi_label.configure(text=weather_info['fd_temp1_hi'])
    fd_temp1_lo_label.configure(text=weather_info['fd_temp1_lo'])
    fd_cond1_label.configure(text=weather_info['fd_cond1'])
    fd_precip1_label.configure(text=weather_info['fd_precip1'])

    fd_day2_label.configure(text=weather_info['fd_day2'])
    fd_temp2_hi_label.configure(text=weather_info['fd_temp2_hi'])
    fd_temp2_lo_label.configure(text=weather_info['fd_temp2_lo'])
    fd_cond2_label.configure(text=weather_info['fd_cond2'])
    fd_precip2_label.configure(text=weather_info['fd_precip2'])

    fd_day3_label.configure(text=weather_info['fd_day3'])
    fd_temp3_hi_label.configure(text=weather_info['fd_temp3_hi'])
    fd_temp3_lo_label.configure(text=weather_info['fd_temp3_lo'])
    fd_cond3_label.configure(text=weather_info['fd_cond3'])
    fd_precip3_label.configure(text=weather_info['fd_precip3'])

    fd_day4_label.configure(text=weather_info['fd_day4'])
    fd_temp4_hi_label.configure(text=weather_info['fd_temp4_hi'])
    fd_temp4_lo_label.configure(text=weather_info['fd_temp4_lo'])
    fd_cond4_label.configure(text=weather_info['fd_cond4'])
    fd_precip4_label.configure(text=weather_info['fd_precip4'])

    fd_day5_label.configure(text=weather_info['fd_day5'])
    fd_temp5_hi_label.configure(text=weather_info['fd_temp5_hi'])
    fd_temp5_lo_label.configure(text=weather_info['fd_temp5_lo'])
    fd_cond5_label.configure(text=weather_info['fd_cond5'])
    fd_precip5_label.configure(text=weather_info['fd_precip5'])

# When the return(enter) key is pressed inside the search bar, call the search_weather function
root.bind_class('TEntry', '<Return>', search_weather)



# Last line, start the mainloop which runs the application
root.mainloop()