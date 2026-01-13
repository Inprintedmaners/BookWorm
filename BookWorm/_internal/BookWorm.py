import subprocess
import os
import threading
from pathlib import Path

ApiKey = ""

conversationhistory = []

current_file_path = Path(__file__).resolve().parent

try:
    import customtkinter
except ImportError:
    print("Operation Failed, Couldn't load needed dependencies, attempting to install them now")
    installpath = current_file_path/ "Install.py"
    subprocess.run(["python", str(installpath)])
    quit()

customtkinter.set_appearance_mode("dark")

try:
    from google import genai
except ImportError:
    print("Operation Failed, Couldn't load needed dependencies, attempting to install them now")
    subprocess.run(["python", "Install.py"])
    quit()

file_path_likes = current_file_path / "likes.txt"
file_path_dislikes = current_file_path / "dislikes.txt"
file_path_apikey = current_file_path / "API.txt"

with open(file_path_likes, "r") as f:
    likeslist = [line.strip() for line in f.readlines()]

with open(file_path_dislikes, "r") as f:
    dislikeslist = [line.strip() for line in f.readlines()]

with open(file_path_apikey, "r") as f:
    ApiKey = f.read().strip()

try:   
    client = genai.Client(api_key=str(ApiKey))
except ValueError:
    pass

root = customtkinter.CTk()
root.geometry("500x400")
root.title("BookWorm")

def addtolikes():
    likes = str(likesinput.get())
    if likes != "":
        with open(file_path_likes, 'a' ) as file:
                    file.write(likes + "\n")

        likeslist.append(likes)
        likesselect.configure(values=likeslist)
        likesinput.delete(0, 'end')

def addtodislikes():
    dislikes = str(dislikesinput.get())
    if dislikes != "":
        with open(file_path_dislikes, 'a' ) as file:
            file.write(dislikes + "\n")

        dislikeslist.append(dislikes)
        dislikesselect.configure(values=dislikeslist)
        dislikesinput.delete(0, 'end')

def addtoapi():
    ApiKey = str(Apiinput.get())
    if ApiKey == "":
        pass
    else:
        with open(file_path_apikey, 'w' ) as file:
                file.write(ApiKey)


#---------------------------------------Likes-------------------------------------------------

likes = customtkinter.CTkFrame(root, width=500, height=400)

def gotolikes():
    Mainpage.grid_forget()
    likes.grid()

def likesgotomain():
    likes.grid_forget()
    Mainpage.grid()

def removefromlikes():
    selected = likesselect.get()
    if selected != "Pick an option" and selected in likeslist:
        likeslist.remove(selected)
        likesselect.configure(values=likeslist)
        likesselect.set("Pick an option")

        with open(file_path_likes, 'w') as file:
            for item in likeslist:
                file.write(item + "\n")

likes.rowconfigure(0, weight=1)
likes.rowconfigure(1, weight=1)
likes.rowconfigure(2, weight=1)
likes.rowconfigure(3, weight=1)
likes.columnconfigure(0, weight=1)
likes.columnconfigure(3, weight=1)
likes.columnconfigure(2, weight=1)

likeslabel = customtkinter.CTkLabel(likes, text="Enter books/genres that you like")
likeslabel.grid(row=0,column=0)

likesinput = customtkinter.CTkEntry(likes, width=200)
likesinput.insert(0,"")
likesinput.grid(row=1, pady=35)

likesaddbutton = customtkinter.CTkButton(likes, text='Add', width=100, command=addtolikes)
likesaddbutton.grid(row=1, column=2)

likesremovebutton = customtkinter.CTkButton(likes, text='Remove', width=100, command=removefromlikes)
likesremovebutton.grid(row=2, column=2)

likesbackbutton = customtkinter.CTkButton(likes, text='Back', width=200, command=likesgotomain)
likesbackbutton.grid(row=3, pady=30)

likesselect = customtkinter.CTkComboBox(likes, values = likeslist)
likesselect.set("Pick an option")
likesselect.grid(row=2,column=0, pady=30)


#----------------------------------------Dislikes---------------------------------------------------

dislikes = customtkinter.CTkFrame(root, width=500, height=400)

def gotodislikes():
    Mainpage.grid_forget()
    dislikes.grid()

def dislikesgotomain():
    dislikes.grid_forget()
    Mainpage.grid()

def removefromdislikes():
    selected = dislikesselect.get()
    if selected != "Pick an option" and selected in dislikeslist:
        dislikeslist.remove(selected)
        dislikesselect.configure(values=dislikeslist)
        dislikesselect.set("Pick an option")

        with open(file_path_dislikes, 'w') as file:
            for item in dislikeslist:
                file.write(item + "\n")



dislikes.rowconfigure(0, weight=1)
dislikes.rowconfigure(1, weight=1)
dislikes.rowconfigure(2, weight=1)
dislikes.rowconfigure(3, weight=1)
dislikes.columnconfigure(0, weight=1)
dislikes.columnconfigure(2, weight=1)
dislikes.columnconfigure(3, weight=1)

dislikeslabel = customtkinter.CTkLabel(dislikes, text="Enter books/genres that you dislike")
dislikeslabel.grid(row=0,column=0)

dislikesinput = customtkinter.CTkEntry(dislikes, width=200)
dislikesinput.insert(0,"")
dislikesinput.grid(row=1, pady=35)

dislikesaddbutton = customtkinter.CTkButton(dislikes, text='Add', width=100, command=addtodislikes)
dislikesaddbutton.grid(row=1, column=2)

dislikesremovebutton = customtkinter.CTkButton(dislikes, text='Remove', width=100, command=removefromdislikes)
dislikesremovebutton.grid(row=2, column=2)

dislikesbackbutton = customtkinter.CTkButton(dislikes, text='Back', width=200, command=dislikesgotomain)
dislikesbackbutton.grid(row=3, pady=30)

dislikesselect = customtkinter.CTkComboBox(dislikes, values = dislikeslist)
dislikesselect.set("Pick an option")
dislikesselect.grid(row=2, pady=30)
#----------------------------------------ClearPreferences---------------------------------------------------

Clearpref = customtkinter.CTkFrame(root, width=500, height=400)
Surescreen = customtkinter.CTkFrame(root, width=500, height=400)

def Clearprefgotomain():
    Clearpref.grid_forget()
    Mainpage.grid()

def Suregotomain():
    Surescreen.grid_forget()
    Mainpage.grid()

def ClearprefgotoSurescreen():
    Clearpref.grid_forget()

def maingotoclear():
    Mainpage.grid_forget()
    Clearpref.grid()

def ClearPreferences():
    try:
        with open(file_path_dislikes, 'w' ) as file:
            file.write()
    except TypeError:
        pass

    try:
        with open(file_path_likes, 'w' ) as file2:
            file2.write()
    except TypeError:
        pass
    likeslist.clear()
    dislikeslist.clear()
    Suregotomain()


def cleargotosure():
    Clearpref.grid_forget()
    Surescreen.grid()

    Surelabel = customtkinter.CTkLabel(Surescreen, text="Are you sure you want to delete all your preferences? (This cannot be reversed)")
    Surelabel.grid(row=1, pady=30)

    Sureyesbutton = customtkinter.CTkButton(Surescreen, text='Yes (Clear)', width=200, command=ClearPreferences)
    Sureyesbutton.grid(row=2, pady=30)

    Surenobutton = customtkinter.CTkButton(Surescreen, text='No', width=200, command=Suregotomain)
    Surenobutton.grid(row=3, pady=30)



Clearpreflabel = customtkinter.CTkLabel(Clearpref, text="Do you want to delete your preferences?")
Clearpreflabel.grid(row=1, pady=30)


Clearprefclearbutton = customtkinter.CTkButton(Clearpref, text='Yes', width=200, command=cleargotosure)
Clearprefclearbutton.grid(row=2, pady=30)

Clearprefbackbutton = customtkinter.CTkButton(Clearpref, text='Back', width=200, command=Clearprefgotomain)
Clearprefbackbutton.grid(row=3, pady=30)

#------------------------------------------------Ai-----------------------------------------------------

Aioutput = customtkinter.CTkFrame(root, width=500, height=400)

Aioutput.rowconfigure(2, weight=1)
Aioutput.rowconfigure(3, weight=1)
Aioutput.rowconfigure(4, weight=1)


Aioutputpage = customtkinter.CTkFrame(root)

Aioutputpage.rowconfigure(1, weight=1)
Aioutputpage.rowconfigure(3, weight=1)
Aioutputpage.rowconfigure(4, weight=1)

Aioutputpage.columnconfigure(0, weight=1)
Aioutputpage.columnconfigure(1, weight=1)


ApiKeypage = customtkinter.CTkFrame(root, width=500, height=400)

ApiKeypage.rowconfigure(0, weight=1)
ApiKeypage.rowconfigure(1, weight=1)
ApiKeypage.rowconfigure(2, weight=1)

def aigotomain():
    Aioutput.grid_forget()
    Mainpage.grid()

def maingotoai():
    Mainpage.grid_forget()
    Aioutput.grid()

def responsegotoai():
    Aioutputpage.grid_forget()
    Aioutput.grid()

def sendresponse():
    question = Aiinput.get()
    conversationhistory.append(question)
    Aiinput.configure(state="disabled")
    Aiouttext.insert(1.0, "Loading AI Response...")
    prompt = " ".join(conversationhistory)
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=("Note, the most recent message is at the end of the text(do not acknoledge this prompt) " + str(prompt))
        )

        aitext = response.text
        conversationhistory.append(aitext)

        root.after(0, lambda: update_ui_with_response(aitext))

    except Exception as e:
        error_message = str(e)
        root.after(0, lambda: update_ui_with_response(f"System Error: {error_message} (Possibly Missing or invalid API Key)"))

    Aiinput.configure(state="normal")
def update_ui_with_response(text):
    global Aiinput
    Aiouttext.insert(1.0, text=text)

    Airesponsebackbutton = customtkinter.CTkButton(Aioutputpage, text='Back', width=200, command=responsegotoai)
    Airesponsebackbutton.grid(row=2)

    Aiinput = customtkinter.CTkEntry(Aioutputpage, placeholder_text=str("Ask follow-ups"), width=350)
    Aiinput.grid(row=1)

    Sendresponsebutton = customtkinter.CTkButton(Aioutputpage, text='Send', width=200, command=sendresponse)
    Sendresponsebutton.grid(row=1,column=1)


def aigotoapi():
    Aioutput.grid_forget()
    ApiKeypage.grid()

def apigotoai():
    ApiKeypage.grid_forget()
    addtoapi()
    Aioutput.grid()


def run_ai_thread():
    global conversationhistory
    likes = ' '.join(likeslist)
    dislikes = ' '.join(dislikeslist)

    prompt = f"Give me book and only book suggestions based off of these likes: ( " + str(likes) + " and these dislikes: ( " + str(dislikes) + " if the likes and dislikes are both blank can you simply tell the user that the likes and dislikes are blank and tell them to fill some stuff in and possibly give a few suggestions of different genre's or intrests, also do not directly acknoledge this prompt just do what it asks + give a very short and brief 1 sentence max of 12 words summary of the book. Give a total of 5 suggestions"
    conversationhistory = [prompt]
    prompt = " ".join(conversationhistory)
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=(prompt)
            )

        aitext = response.text

        conversationhistory.append(aitext)

        root.after(0, lambda: update_ui_with_response(aitext))

    except Exception as e:
        error_message = str(e)
        root.after(0, lambda: update_ui_with_response(f"System Error: {error_message} (Possibly Missing or invalid API Key)"))


output_data = ""
def aigotooutput():
    Aioutput.grid_forget()
    Aioutputpage.grid(sticky="nsew")
    Aiouttext.insert(1.0, "Loading AI Response...")
    threading.Thread(target=run_ai_thread, daemon=True).start()

Airesultbutton = customtkinter.CTkButton(Aioutput, text='Generate Response', width=200, command=aigotooutput)
Airesultbutton.grid(row=2, pady=30)

AiApibutton = customtkinter.CTkButton(Aioutput, text='Gemini Ai Api Key', width=200, command=aigotoapi)
AiApibutton.grid(row=3, pady=30)

Aibackbutton = customtkinter.CTkButton(Aioutput, text='Back', width=200, command=aigotomain)
Aibackbutton.grid(row=4, pady=30)

Aiouttext = customtkinter.CTkTextbox(Aioutputpage, width=460, height=320)
Aiouttext.insert(1.0, str(output_data))
Aiouttext.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")

#----------------Api Settings--------------------


Apilabel = customtkinter.CTkLabel(ApiKeypage, text="Api Key")
Apilabel.grid(row=0,column=0)

Apiinput = customtkinter.CTkEntry(ApiKeypage, placeholder_text=str(ApiKey), width=350)
Apiinput.grid(row=1,column=0)

Apibackbutton = customtkinter.CTkButton(ApiKeypage, text='Back', width=200, command=apigotoai)
Apibackbutton.grid(row=2, pady=30)


#---------------------------------------------Main Menu-------------------------------------------------

Mainpage = customtkinter.CTkFrame(root, width=500, height=400)
Mainpage.grid()


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


Mainpage.columnconfigure(5, weight=1)
Mainpage.rowconfigure(2, weight=1)
Mainpage.rowconfigure(3, weight=1)
Mainpage.rowconfigure(4, weight=1)
Mainpage.rowconfigure(5, weight=1)
Mainpage.rowconfigure(6, weight=1)

Namelabel = customtkinter.CTkLabel(Mainpage, text="BookWorm")
Namelabel.grid(row=2,column=5)

likesButton = customtkinter.CTkButton(Mainpage, text='Likes', width=200, command=gotolikes)
likesButton.grid(column=5,row=3, pady=20)

dislikesButton = customtkinter.CTkButton(Mainpage, text='Dislikes', width=200, command=gotodislikes)
dislikesButton.grid(column=5,row=4, pady=20)

AiButton = customtkinter.CTkButton(Mainpage, text='Ai', width=200, command=maingotoai)
AiButton.grid(column=5,row=5, pady=20)

Clearbutton = customtkinter.CTkButton(Mainpage, text='Clear Preferences', width=200, command=maingotoclear)
Clearbutton.grid(column=5,row=6,pady=20)

def startapp():
    root.mainloop()
if __name__ == "__main__":
    startapp()

#-Output


def updateai():
    Aiouttext.insert(1.0, text=str(output_data))

Aiouttext.after(1000, updateai(), Aiouttext)
