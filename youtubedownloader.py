from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""

# file location function

def open_location():
    global Folder_Name

    Folder_Name = filedialog.askdirectory()
    if (len(Folder_Name) > 1):
        locationError.config(text=Folder_Name, fg="green")

    else:
        locationError.config(text="Please Choose A Folder", fg="red")

# downloading video function

def downloadvideo():
    choice = ytdchoices.get()

    url  = ytdEntry.get()

    if len(url) > 1:
        ytdError.config(text="")
        yt = YouTube(url)

        if (choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif (choice== choices[1]):
            select = yt.streams.filter(progressive=True, file_extension="mp4").last()

        elif (choice== choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Add the Link Again", fg="red")
    
    select.download(Folder_Name)
    ytdError.config(text= "Download Completed!!")



root = Tk()

root.title("YT Downloader")
root.geometry("350x400") # window size
root.columnconfigure(0, weight=1)

 # YT Link Label

ytdLabel = Label(root, text="Enter the URL of the Video", font=("jost", 15))
ytdLabel.grid()

# Entry Box

ytdEntryVar = StringVar()
ytdEntry = Entry(root, width=50, textvariable= ytdEntryVar)
ytdEntry.grid()

# Error Handling

ytdError = Label(root, text= "Error Msg", fg="red", font=("jost", 10))
ytdError.grid()

# Saving to File Location

saveLabel = Label(root, text="Save the Video File", font=("jost", 15, "bold"))
saveLabel.grid()

# Save File Button

saveEntry = Button(root, width=10, bg="red", fg= "black", text= "Choose Path", command= open_location)
saveEntry.grid()

# Error Message for Location

locationError = Label(root, text="Error Message of Path", fg = "red", font = ("jost", 10))
locationError.grid()

# Download Quality
ytdQuality = Label(root, text= "Select Quality", font= ("jost", 15))
ytdQuality.grid()

# Quality Box
choices = ["720p", "144p", "Only Audio"]
ytdchoices = ttk.Combobox(root, values= choices)
ytdchoices.grid()

# Download Button
downloadbtn = Button(root, text="Download", width=10, bg="red", fg="black", command=downloadvideo)
downloadbtn.grid()



root.mainloop()

