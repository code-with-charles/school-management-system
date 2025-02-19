
import sys
import customtkinter
import tkinter 
from tkinter import *
from tkinter import messagebox
import os
import sqlite3
from tkinter import filedialog
from PIL import Image

import  shutil

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")
window=customtkinter.CTk()
window.title("MorLaw International")
window.geometry("1366x766")
window.resizable(False,True)

def resource_path(relative_path):
    try:
        base_path=sys._MEIPASS
    except Exception:
        base_path=os.path.abspath(".")
    return os.path.join(base_path,relative_path)


       
background_image=customtkinter .CTkImage(light_image=Image.open( resource_path('pics/images (3).jpeg')),
                              dark_image=Image.open(resource_path('pics/images (3).jpeg')),
                              size=(1366,764))
left_frame=customtkinter .CTkImage(light_image=Image.open(resource_path('pics/images (2).jpeg')),
                              dark_image=Image.open(resource_path('pics/images (2).jpeg')),
                              size=(600,764))
schools_logo=customtkinter .CTkImage(light_image=Image.open(resource_path('pics/images (4).jpeg')),
                              dark_image=Image.open(resource_path('pics/images (4).jpeg')),
                              size=(60,50))
background_image_of_log_page=customtkinter .CTkImage(light_image=Image.open(resource_path('pics/download.jpeg')),
                              dark_image=Image.open(resource_path('pics/download.jpeg')),
                              size=(700,690))
background_image_of_school_logo=customtkinter .CTkImage(light_image=Image.open(resource_path('pics/images (3).jpeg')),
                              dark_image=Image.open(resource_path('pics/images (3).jpeg')),
                              size=(720,210))
window_image=customtkinter.CTkImage(light_image=Image.open(resource_path("pics/window.jpeg")),
                                    dark_image=Image.open(resource_path("pics/window.jpeg")),
                                    size=(1366,766))
#icons step ups
facebook_icon=customtkinter.CTkImage(light_image=Image.open(resource_path("pics/New folder/facebook icon.png")),
                                  dark_image=Image.open(resource_path("pics/New folder/facebook icon.png")),
                                  size=(30,30)
                                  )
pintrest_icon=customtkinter.CTkImage(light_image=Image.open(resource_path("pics/New folder/pinterest icon.png")),
                                  dark_image=Image.open(resource_path("pics/New folder/pinterest icon.png")),
                                  size=(30,30))
whatsapp_icon=customtkinter.CTkImage(light_image=Image.open(resource_path("pics/New folder/whatsapp icon.png")),
                                  dark_image=Image.open(resource_path("pics/New folder/whatsapp icon.png")),
                                  size=(30,30))
linkin_icon=customtkinter.CTkImage(light_image=Image.open(resource_path("pics/New folder/linkedin icon.png")),
                                  dark_image=Image.open(resource_path("pics/New folder/linkedin icon.png")),
                                  size=(30,30))


#infomative labels
quality_icon=customtkinter.CTkImage(light_image=Image.open(resource_path("pics/New folder/qualty.png")),
                                  dark_image=Image.open(resource_path("pics/New folder/qualty.png")),
                                  size=(80,60)
                                  )
skills_icon=customtkinter.CTkImage(light_image=Image.open(resource_path("pics/New folder/skills.jpeg")),
                                  dark_image=Image.open(resource_path("pics/New folder/skills.jpeg")),
                                  size=(80,60))
compitence_icon=customtkinter.CTkImage(light_image=Image.open(resource_path("pics/New folder/compitence.jpeg")),
                                  dark_image=Image.open(resource_path("pics/New folder/compitence.jpeg")),
                                  size=(80,60))
forward_icon=customtkinter.CTkImage(light_image=Image.open(resource_path("pics/New folder/icons8-login-64.png")),
                                  dark_image=Image.open(resource_path("pics/New folder/icons8-login-64.png")),
                                  size=(50,50))

# Create a label to display the background image

main_photo_on_window=customtkinter.CTkLabel(window,text="",image=window_image).place(relwidth=1,relheight=1,x=0,y=0)


#Home frame
def home_window():
    app=customtkinter.CTkFrame(window,width=1366,height=766)
    app.place(relx=0.0,rely=0.0)
    top_frame=customtkinter.CTkFrame(app,height=40,fg_color="white",width=1366)
    top_frame.place(relx=0.0)

    school_logo=customtkinter.CTkLabel(top_frame,image=schools_logo,text="")
    school_logo.place(relx=0.0,rely=0.0)

    school_title=customtkinter.CTkLabel(top_frame,text="MorLaw International",
                                        font=("Roboto",15),text_color="blue",)
    school_title.place(relx=0.05,rely=0.0)

    school_title1=customtkinter.CTkLabel(top_frame,text="PUBLIC SCHOOL & JUNIUR COLLEGE",text_color="black",height=2,
                                        font=('Roboto',9))
    school_title1.place(relx=0.05,rely=0.48)
    def staffclick():
        app.destroy()
        app.update()
        staff_log_page()
    staff_but=customtkinter.CTkButton(top_frame,height=30,text="Staff",font=("Helvetica",15),text_color="white",width=30,fg_color='silver',command=staffclick,
                                    )
    staff_but.place(relx=0.81, rely=0.18)
    def parent_click():
        app.destroy()
        app.update()
        parent_log_page()
    parent=customtkinter.CTkButton(top_frame,height=40,text="Parent",font=("Helvetica",15),text_color="white",width=30,fg_color="silver",
                                   command=parent_click
                                    )
    parent.place(relx=0.85, rely=0.02)
    admission=customtkinter.CTkButton(top_frame,height=20,text="Admission-online",font=("Helvetica",15),text_color="white",
                                    )
    admission.place(relx=0.90, rely=0.22)

    #buttons frame 

    buttons_frame=customtkinter.CTkFrame(app,width=1366,height=40,fg_color="blue")
    buttons_frame.place(relx=0.0,rely=0.06)
    home=customtkinter.CTkButton(buttons_frame,text="Home",text_color='white',width=20,height=5,font=("Roboto",11),fg_color="blue")
    home.place(relx=0.005,rely=0.25)
    about=customtkinter.CTkButton(buttons_frame,text="About-Us",text_color='white',width=20,height=5,font=("Roboto",11),fg_color="blue")
    about.place(relx=0.04,rely=0.25)
    Academics=customtkinter.CTkButton(buttons_frame,text="Academics",text_color='white',width=20,height=5,font=("Roboto",11),fg_color="blue")
    Academics.place(relx=0.09,rely=0.25)
    Facilities=customtkinter.CTkButton(buttons_frame,text="Facilities",text_color='white',width=20,height=5,font=("Roboto",11),fg_color="blue")
    Facilities.place(relx=0.15,rely=0.25)
    def onclick():
        app.destroy()
        app.update()
        student_log_page()
    students=customtkinter.CTkButton(buttons_frame,text="Student-Corner",text_color='white',width=20,height=5,font=("Roboto",11),fg_color="blue",
                                     command=onclick)
    students.place(relx=0.20,rely=0.25)
    def news_click():
        app.destroy()
        app.update()
        news_and_events()
    news=customtkinter.CTkButton(buttons_frame,text="News & Events",text_color='white',width=20,height=5,font=("Roboto",11),fg_color="blue",
                                 command=news_click)
    news.place(relx=0.27,rely=0.25)
    def contact_click():
        app.destroy()
        app.update()
        contacts()
    contact=customtkinter.CTkButton(buttons_frame,text="Contact Us",text_color='white',width=20,height=5,font=("Roboto",11),fg_color="blue",
                                    command=contact_click)
    contact.place(relx=0.34,rely=0.25)


    #socila media icons
    linkin=customtkinter.CTkButton(buttons_frame,height=5,width=15,image=linkin_icon,text="",fg_color="blue",hover=False)
    linkin.place(relx=0.87,rely=0.12)
    facebook=customtkinter.CTkButton(buttons_frame,height=5,width=15,image=facebook_icon,text="",fg_color="blue",hover=False)
    facebook.place(relx=0.90,rely=0.12)
    pintrest=customtkinter.CTkButton(buttons_frame,height=5,width=15,image=pintrest_icon,text="",fg_color="blue",hover=False)
    pintrest.place(relx=0.93,rely=0.12)
    whatsapp=customtkinter.CTkButton(buttons_frame,height=5,width=15,image=whatsapp_icon,text="",fg_color="blue",hover=False)
    whatsapp.place(relx=0.96,rely=0.12)





    home_frame=customtkinter.CTkFrame(app,width=1366,height=430,)
    home_frame.place(relx=0.0,rely=0.12)
    font=customtkinter.CTkFont(weight="bold",family="Roboto",size=11)
    #######################inbeteen details###############
    labels=customtkinter.CTkLabel(app,width=1366,height=80,fg_color="black",text='')
    labels.place(relx=0.0,rely=0.68)

    quality=customtkinter.CTkLabel(labels,image=quality_icon,text='')
    quality.place(relx=0.15,rely=0.04)
    ql=customtkinter.CTkLabel(labels,text="QUALITY",font=font,text_color='white')
    ql.place(relx=0.21,rely=0.01)
    ql1=customtkinter.CTkLabel(labels,text="Quality teaching for\nimproved results",text_color='silver',font=("Helvetica",10))
    ql1.place(relx=0.21,rely=0.40)

    skills=customtkinter.CTkLabel(labels,image=skills_icon,text='')
    skills.place(relx=0.30,rely=0.04)
    sk=customtkinter.CTkLabel(labels,text="SKILLS",font=font,text_color='white')
    sk.place(relx=0.37,rely=0.01)
    sk1=customtkinter.CTkLabel(labels,text="Develop fine and\ngross skills",text_color='silver',font=("Helvetica",10))
    sk1.place(relx=0.37,rely=0.40)

    compitence=customtkinter.CTkLabel(labels,image=compitence_icon,text='')
    compitence.place(relx=0.45,rely=0.04)
    cp=customtkinter.CTkLabel(labels,text="COMPETENCY",font=font,text_color='white')
    cp.place(relx=0.52,rely=0.01)
    cp1=customtkinter.CTkLabel(labels,text="Equip students to\nmeet the future",text_color='silver',font=("Helvetica",10))
    cp1.place(relx=0.52,rely=0.40)

    clubs=customtkinter.CTkFrame(app,fg_color="#3B9EBF",width=300,
                                height=250,
                                
                                )

    clubs.place(relx=0.60,rely=0.68)
    clubs_text=customtkinter.CTkLabel(clubs,text="The MorLaw International\nSchool Clubs",font=("Helvetica",11),
                                    text_color="white")
    clubs_text.place(relx=0.0,rely=0.0)


    fac=customtkinter.CTkLabel(clubs,fg_color="#3B9EBF",text="Facilities",font=("Helvetica",26),width=300,
                                text_color="white",
                                anchor="nw"
                                )
    fac.place(relx=0.0,rely=0.15)
    forward=customtkinter.CTkLabel(clubs,image=forward_icon,text='')
    forward.place(relx=0.4,rely=0.13)


    list_clubs=customtkinter.CTkLabel(clubs,fg_color="#E1EEF2",width=300,height=150,text='')
    list_clubs.place(relx=0.0,rely=0.3)

    maths=customtkinter.CTkLabel(list_clubs,text="MATHEMATICS Club ✨",text_color="black",fg_color="#E1EEF2")
    maths.place(relx=0.09,rely=0.0)
    science=customtkinter.CTkLabel(list_clubs,text="SCIENCE Club 🐱‍🚀",text_color="black",fg_color="#E1EEF2")
    science.place(relx=0.09,rely=0.2)
    sports=customtkinter.CTkLabel(list_clubs,text="SPORTS Club 🚲🏎🪂",text_color="black",fg_color="#E1EEF2")
    sports.place(relx=0.09,rely=0.40)
    arts=customtkinter.CTkLabel(list_clubs,text="ART & DESIGN Club 🛹🗽",text_color="black",fg_color="#E1EEF2")
    arts.place(relx=0.09,rely=0.60)


    down_message=customtkinter.CTkLabel(app,text="Welcome to MorLaw Interntional Public & Junior College",height=5,text_color="black",font=font)
    down_message.place(relx=0.3,rely=0.79)
    message=customtkinter.CTkLabel(app,
                                text="MorLaw International is owned and managed by society for educatio and Dr Charles\nas part of Social Service Commission.We offer a host of facilities which would\na sense of confidence and creativity among students.Our facilities at\nMorLaw International are highly trained and hightly qualified in their\nrespective fields,giving stress on skill,compitence and concept based on \nleaning system.You will definately be greateful for ur son or daughter",
                                text_color="black",font=("Helvetica",10),anchor="nw")
    message.place(relx=0.3,rely=0.81)

    global current_image_index
    def update_image():
        global current_image_index
        img=images[current_image_index]
        ctk_img=customtkinter.CTkImage(light_image=img,
                                    dark_image=img,
                                    size=(1366,430))
        image_label.configure(image=ctk_img)
        current_image_index +=1
        
        if current_image_index >=len(images):
            current_image_index=0
        home_frame.after(4000,update_image)
        
        
    image_files=[
   
    
    'pics/backside.jpeg',
    'pics/first.jpeg',
    'pics/front.jpeg',
    'pics/OIP (2).jpeg',
    'pics/OIP (3).jpeg',
    'pics/OIP (4).jpeg',
    'pics/OIP (6).jpeg',
    'pics/OIP.jpeg',
    'pics/download (2).jpeg',
    'pics/download (1).jpeg',
    'pics/download.jpeg',
     
    ]
        
    images=[Image.open(resource_path(img_file)) for img_file in image_files]
    image_label=customtkinter.CTkLabel(home_frame,text="")
    image_label.pack()

    current_image_index=0
    update_image()


    




def student_log_page():
    student_frame=customtkinter.CTkFrame(window,width=900,height=650,fg_color='black',corner_radius=20)
    student_frame.place(relx=0.18,rely=0.05)
    # bg_image=customtkinter.CTkLabel(student_frame,image=window_image,height=100)
    # bg_image.place(relwidth=1,relheight=1,x=0,y=400)
    top_title=customtkinter.CTkLabel(student_frame,text="Students login page:",text_color="white",font=("Helvetica",14),fg_color="blue",anchor="center",corner_radius=20)

    top_title.place(relx=0.72,rely=0.1)
    std=customtkinter.CTkImage(light_image=Image.open(resource_path('pics/people/stdnlog.jpeg')),
                               dark_image=Image.open(resource_path('pics/people/stdnlog.jpeg')),
                               size=(500,650))
    stdl=customtkinter.CTkLabel(student_frame,text='',image=std)
    stdl.place(relx=0.0)
    
   
    def forward_to_home():
        student_frame.destroy()
        window.update()
        home_window()
            
    def registration():
        student_frame.destroy()
        window.update()
        student_registration_form()
    
          
    backbutton=customtkinter.CTkButton(student_frame,text="(↩Back)",font=('Helvetica',10),fg_color="red",text_color="white",command=forward_to_home)
    backbutton.place(relx=0.56,rely=0.01)
    id_number=customtkinter.CTkLabel(student_frame,text="Enter School ID:",text_color="white",font=("Helvetica",14))
    id_number.place(relx=0.7,rely=0.2)
    id_entry=customtkinter.CTkEntry(student_frame,width=200,text_color="green",font=("bold",16),border_color="blue")
    id_entry.place(relx=0.73,rely=0.3)
    password=customtkinter.CTkLabel(student_frame,text="PassWord:",text_color="white",font=("Helvetica",14))
    password.place(relx=0.7,rely=0.4)
    word=customtkinter.CTkLabel(student_frame,text="use your registration as password:",text_color="white",font=("Helvetica",11))
    word.place(relx=0.7,rely=0.44)
    password_entry=customtkinter.CTkEntry(student_frame,width=200,text_color="green",font=("bold",16),border_color="blue")
    password_entry.place(relx=0.73,rely=0.5)
    register=customtkinter.CTkButton(student_frame,text="REGISTER",font=("Helvetica",12),text_color="white",fg_color="red",command=registration)
    register.place(relx=0.56,rely=0.85)
    def forward_to_dashboard():
        def logins(student_id,registration_number):

            conn = sqlite3.connect(get_writable_db_path(resource_path("data_details.db")))
            c = conn.cursor()
            c.execute("SELECT  * FROM data WHERE  STUDENT_ID=?  AND REGISTRATION_NUMBER=? ",(student_id,registration_number))
            results=c.fetchall()
            if results:
                print(b," ",a)
                student_frame.destroy()
                window.update()
                students_dashboard()
            else:
                messagebox.showwarning('warning','Wrong password or student_id')
            conn.commit()
            
            conn.close()
        a=id_entry.get()
        b=password_entry.get()
        if a!='' and b!='':
            logins(a,b)
            
        else:
            messagebox.showwarning('warning',"Some Fields Are Empty")


     

            
        
    login=customtkinter.CTkButton(student_frame,text="LOGIN",font=("Helvetica",12),text_color="white",fg_color="green",command=forward_to_dashboard)
    login.place(relx=0.84,rely=0.85)
    forgot_passoword=customtkinter.CTkButton(student_frame,text="Forgot password",text_color="yellow",font=("Helvetica",12),
                                             fg_color=None,height=6,width=55)
    forgot_passoword.place(relx=0.73,rely=0.95)
    
def staff_log_page():
    staff_frame=customtkinter.CTkFrame(window,width=900,height=650,fg_color='black',corner_radius=20)
    staff_frame.place(relx=0.12,rely=0.1)
    top_title=customtkinter.CTkLabel(staff_frame,text="Staff login page:",text_color="white",font=("Helvetica",14),fg_color="blue",anchor="center",corner_radius=20)

    top_title.place(relx=0.72,rely=0.1)
    std=customtkinter.CTkImage(light_image=Image.open(resource_path('pics/people/stdnlog.jpeg')),
                               dark_image=Image.open(resource_path('pics/people/stdnlog.jpeg')),
                               size=(500,650))
    stdl=customtkinter.CTkLabel(staff_frame,text='',image=std)
    stdl.place(relx=0.0)
    def forward_to_mainwindow():
        staff_frame.destroy()
        window.update()
        home_window()
    
    backbutton=customtkinter.CTkButton(staff_frame,text="(↩Back",font=('Helvetica',10),fg_color="red",text_color="white",command=forward_to_mainwindow)
    backbutton.place(relx=0.56,rely=0.01)
    id_number=customtkinter.CTkLabel(staff_frame,text="Enter Staff ID:",text_color="white",font=("Helvetica",14))
    id_number.place(relx=0.7,rely=0.2)
    id_entry=customtkinter.CTkEntry(staff_frame,width=200,text_color="green",font=("Helvetica",12))
    id_entry.place(relx=0.73,rely=0.3)
    password=customtkinter.CTkLabel(staff_frame,text="PassWord:",text_color="white",font=("Helvetica",14))
    password.place(relx=0.7,rely=0.4)
    password_entry=customtkinter.CTkEntry(staff_frame,width=200,text_color="green",font=("Helvetica",12))
    password_entry.place(relx=0.73,rely=0.5)
    register=customtkinter.CTkButton(staff_frame,text="REGISTER",font=("Helvetica",12),text_color="white",fg_color="red")
    register.place(relx=0.56,rely=0.85)
    login=customtkinter.CTkButton(staff_frame,text="LOGIN",font=("Helvetica",12),text_color="white",fg_color="green")
    login.place(relx=0.84,rely=0.85)
    forgot_passoword=customtkinter.CTkButton(staff_frame,text="Forgot password",text_color="yellow",font=("Heletica",12),
                                             fg_color=None,height=6,width=55)
    forgot_passoword.place(relx=0.73,rely=0.95)


def parent_log_page():
    parent_frame=customtkinter.CTkFrame(window,width=900,height=650,fg_color='black',corner_radius=20)
    parent_frame.place(relx=0.18,rely=0.05)
    # bg_image=customtkinter.CTkLabel(student_frame,image=window_image,height=100)
    # bg_image.place(relwidth=1,relheight=1,x=0,y=400)
    top_title=customtkinter.CTkLabel(parent_frame,text="Parent login page:",text_color="white",font=("Helvetica",14),fg_color="blue",anchor="center",corner_radius=20)

    top_title.place(relx=0.72,rely=0.1)
    std=customtkinter.CTkImage(light_image=Image.open(resource_path('pics/people/stdnlog.jpeg')),
                               dark_image=Image.open(resource_path('pics/people/stdnlog.jpeg')),
                               size=(500,650))
    stdl=customtkinter.CTkLabel(parent_frame,text='',image=std)
    stdl.place(relx=0.0)
    
   
    def forward_to_home():
        parent_frame.destroy()
        window.update()
        home_window()
            
    def registration():
        parent_frame.destroy()
        window.update()
        student_registration_form()
    
          
    backbutton=customtkinter.CTkButton(parent_frame,text="(↩Back)",font=('Helvetica',10),fg_color="red",text_color="white",command=forward_to_home)
    backbutton.place(relx=0.56,rely=0.01)
    id_number=customtkinter.CTkLabel(parent_frame,text="Enter School ID:",text_color="white",font=("Helvetica",14))
    id_number.place(relx=0.7,rely=0.2)
    id_entry=customtkinter.CTkEntry(parent_frame,width=200,text_color="green",font=("bold",16),border_color="blue")
    id_entry.place(relx=0.73,rely=0.3)
    password=customtkinter.CTkLabel(parent_frame,text="PassWord:",text_color="white",font=("Helvetica",14))
    password.place(relx=0.7,rely=0.4)
    password_entry=customtkinter.CTkEntry(parent_frame,width=200,text_color="green",font=("bold",16),border_color="blue")
    password_entry.place(relx=0.73,rely=0.5)
    register=customtkinter.CTkButton(parent_frame,text="REGISTER",font=("Helvetica",12),text_color="white",fg_color="red",command=registration)
    register.place(relx=0.56,rely=0.85)
    login=customtkinter.CTkButton(parent_frame,text="LOGIN",font=("Helvetica",12),text_color="white",fg_color="green")
    login.place(relx=0.84,rely=0.85)
    forgot_passoword=customtkinter.CTkButton(parent_frame,text="Forgot password",text_color="yellow",font=("Heletica",12),
                                             fg_color=None,height=6,width=55)
    forgot_passoword.place(relx=0.73,rely=0.95)
    



 
 
 
 

 
def contacts():
    contact_frame=customtkinter.CTkFrame(window,width=900,height=600,fg_color='white',corner_radius=20)
    contact_frame.place(relx=0.12,rely=0.1)
    top_title=customtkinter.CTkLabel(contact_frame,text="Send Us A Messsage:",text_color="black",font=("Helvetica",23),fg_color="white",anchor="center",corner_radius=20)

    top_title.place(relx=0.65,rely=0.1)
    def forward_to_mainwindow():
        contact_frame.destroy()
        window.update()
        home_window()
    
    backbutton=customtkinter.CTkButton(contact_frame,text="(↩Back",font=('Helvetica',10),fg_color="red",text_color="white",command=forward_to_mainwindow,width=30)
    backbutton.place(relx=0.56,rely=0.01)
    std=customtkinter.CTkImage(light_image=Image.open(resource_path('pics/contact.jpeg')),
                               dark_image=Image.open(resource_path('pics/contact.jpeg')),
                               size=(500,650))
    stdl=customtkinter.CTkLabel(contact_frame,text='',image=std)
    stdl.place(relx=0.0)
    name=customtkinter.CTkLabel(contact_frame,text="Tell us ur Name:",text_color="black",font=("Helvetica",13),fg_color="white",anchor="e",corner_radius=20)

    name.place(relx=0.56,rely=0.2)
    name_entry=customtkinter.CTkEntry(contact_frame,width=200,text_color="green",font=("Helvetica",16),placeholder_text="First & Second name")
    name_entry.place(relx=0.57,rely=0.25)
    email=customtkinter.CTkLabel(contact_frame,text="Enter ur Email:",text_color="black",font=("Helvetica",13),fg_color="white",anchor="e",corner_radius=20)

    email.place(relx=0.56,rely=0.35)
    email_entry=customtkinter.CTkEntry(contact_frame,width=200,text_color="green",font=("Helvetica",16),placeholder_text="Email-Address")
    email_entry.place(relx=0.57,rely=0.40)
    message=customtkinter.CTkLabel(contact_frame,text="Mesage:",text_color="black",font=("Helvetica",13),fg_color="white",anchor="e",corner_radius=20)

    message.place(relx=0.56,rely=0.5)
    def textbox():
        text=customtkinter.CTkTextbox(contact_frame,width=380,height=200,corner_radius=20,fg_color="white",text_color="black",font=('bold',14),
                                      wrap="word",
                                      border_color="blue",border_width=3,)
        text.place(relx=0.56,rely=0.55)
    textbox()
    send=customtkinter.CTkButton(contact_frame,text="Send Message",text_color="white",fg_color="green",)
    send.place(relx=0.73,rely=0.95)
def student_registration_form():
    student_registration_frame=customtkinter.CTkFrame(window,width=1366,height=766)
    student_registration_frame.pack(fill="both",expand=True)
    font1=customtkinter.CTkFont("aerial",20) 
    font3=customtkinter.CTkFont("aerial",11)
    font2=customtkinter.CTkFont("roman",25)
    bg_image=customtkinter.CTkLabel(student_registration_frame,image=window_image)
    bg_image.place(relwidth=1,relheight=1)

    title=customtkinter.CTkLabel(student_registration_frame,
                                text="STUDENT REGISTRATION Form",
                                text_color="white",
                                anchor="center",
                                fg_color="#1b3f4c",
                                font=font2,
                                height=10,
                                compound="top"
                                
                                )
    title.pack(side="top",fill="x",padx=10)
    search_entry=customtkinter.CTkEntry(title,placeholder_text='SEARCH',width=150,placeholder_text_color='grey')
    search_entry.place(relx=0.8)
    search_icon=customtkinter.CTkImage(light_image=Image.open(resource_path('pics/icons8-search-48.png')),
                                    dark_image=Image.open(resource_path('pics/icons8-search-48.png')),
                                    size=(50,40))
    icon=customtkinter.CTkButton(title,text='SEARCH',corner_radius=20,width=20,height=30).place(relx=0.89)
    #fist frame for the all personal details
    personal_details=customtkinter.CTkFrame(student_registration_frame,width=1000,height=300,
                                            fg_color="#075264")
    personal_details.place(relx=0.01,rely=0.15)
    #second frame for vat details
    vat_details=customtkinter.CTkFrame(student_registration_frame,width=1000,height=350,
                                            fg_color="#1a3b33")
    vat_details.place(relx=0.01,rely=0.55)
    #entries for personal details which
    #will be on the -pesonal detals frame-
    customtkinter.CTkLabel(personal_details,text="____@PERSONAL-DETAILS:____",text_color="red",
                        font=font3,anchor="center").place(relx=0.06,rely=0.01)
    fname=customtkinter.CTkLabel(personal_details,text="First-Name:",
                                text_color="#a65f14",font=font1,anchor="w")
    fname.place(relx=0.05,rely=0.1)
    sname=customtkinter.CTkLabel(personal_details,text="Second-Name:",
                                text_color="#a65f14",font=font1,anchor="w")
    sname.place(relx=0.05,rely=0.2)
    id_no=customtkinter.CTkLabel(personal_details,text="ID-Number:",
                                text_color="#a65f14",font=font1,anchor="w")
    id_no.place(relx=0.05,rely=0.3)
    dob=customtkinter.CTkLabel(personal_details,text="DOB:",
                            text_color="#a65f14",font=font1,anchor="w")
    dob.place(relx=0.05,rely=0.4)
    phone=customtkinter.CTkLabel(personal_details,text="Phone-Number",
                                text_color="#a65f14",font=font1,anchor="w")
    phone.place(relx=0.5,rely=0.1)
    father=customtkinter.CTkLabel(personal_details,text="Fathers-Name:",
                                text_color="#a65f14",font=font1,anchor="w")
    father.place(relx=0.5,rely=0.2)
    mother=customtkinter.CTkLabel(personal_details,text="Mothers-Name:",
                                text_color="#a65f14",font=font1,anchor="w")
    mother.place(relx=0.5,rely=0.3)
    gender=customtkinter.CTkLabel(personal_details,text="Gender:",
                                text_color="#a65f14",font=font1,anchor="w")
    gender.place(relx=0.5,rely=0.4)
    #entry boxes for all the values given
    f_entry=customtkinter.CTkEntry(personal_details,width=190,height=10,
                                corner_radius=10,text_color="black",border_color="#224d42")
    f_entry.place(relx=0.25,rely=0.1)
    s_entry=customtkinter.CTkEntry(personal_details,width=190,height=10,
                                corner_radius=10,text_color="black",border_color="#224d42")
    s_entry.place(relx=0.25,rely=0.2)
    id_entry=customtkinter.CTkEntry(personal_details,width=190,height=10,
                                    corner_radius=10,text_color="black",border_color="#224d42")
    id_entry.place(relx=0.25,rely=0.3)
    dob_entry=customtkinter.CTkEntry(personal_details,width=190,height=10,
                                    corner_radius=10,text_color="black",border_color="#224d42")
    dob_entry.place(relx=0.25,rely=0.4)
    ph_entry=customtkinter.CTkEntry(personal_details,width=210,height=10,
                                    corner_radius=10,text_color="black",border_color="#224d42")
    ph_entry.place(relx=0.7,rely=0.1)
    ft_entry=customtkinter.CTkEntry(personal_details,width=210,height=10,
                                    corner_radius=10,text_color="black",border_color="#224d42")
    ft_entry.place(relx=0.7,rely=0.2)
    mt_entry=customtkinter.CTkEntry(personal_details,width=210,height=10,
                                    corner_radius=10,text_color="black",border_color="#224d42")
    mt_entry.place(relx=0.7,rely=0.3)
    g_entry=customtkinter.CTkEntry(personal_details,width=210,height=10,
                                corner_radius=10,text_color="black",border_color="#224d42")
    g_entry.place(relx=0.7,rely=0.4)
    #enty details for the insitutional details
    customtkinter.CTkLabel(vat_details,text="____@INSTITUTIONAL DETAILS:____",text_color="red",
                        font=font3,anchor="center").place(relx=0.06,rely=0.01)
    Email=customtkinter.CTkLabel(vat_details,text="E-MAIL:",
                                text_color="#a65f14",font=font1,anchor="w")
    Email.place(relx=0.05,rely=0.1)
    Registration_number=customtkinter.CTkLabel(vat_details,text="Registration-number:",
                                text_color="#a65f14",font=font1,anchor="w")
    Registration_number.place(relx=0.05,rely=0.2)
    Year_of_study=customtkinter.CTkLabel(vat_details,text="Year-of-study:",
                                text_color="#a65f14",font=font1,anchor="w")
    Year_of_study.place(relx=0.05,rely=0.3)
    program_study=customtkinter.CTkLabel(vat_details,text="Prgram-of-study:",
                            text_color="#a65f14",font=font1,anchor="w")
    program_study.place(relx=0.05,rely=0.4)
    st_id=customtkinter.CTkLabel(vat_details,text="Student-id:",
                                text_color="#a65f14",font=font1,anchor="w")
    st_id.place(relx=0.5,rely=0.1)
    sem=customtkinter.CTkLabel(vat_details,text="Semister:",
                                text_color="#a65f14",font=font1,anchor="w")
    sem.place(relx=0.5,rely=0.2)
    altmail=customtkinter.CTkLabel(vat_details,text="Alternative-Mail:",
                                text_color="#a65f14",font=font1,anchor="w")
    altmail.place(relx=0.5,rely=0.3)
    gender=customtkinter.CTkLabel(personal_details,text="Gender:",
                                text_color="#a65f14",font=font1,anchor="w")
    gender.place(relx=0.5,rely=0.4)
    #entry boxes for all the values given
    mail=customtkinter.CTkEntry(vat_details,width=190,height=10,
                                corner_radius=10,text_color="black",border_color="#224d42")
    mail.place(relx=0.25,rely=0.1)
    def random_regitration_numbers():
        global var
        import random
        generated=''
        for i in range(4):
            generated +=str(random.randint(1,9))
            formarted=(f"ML/{generated}G/24")
        
        var=customtkinter.StringVar()
        var.set(formarted)
    random_regitration_numbers()   
        
    regno=customtkinter.CTkEntry(vat_details,width=190,height=10,state='readonly',textvariable=var,font=("bold",16),
                                corner_radius=10,text_color="black",border_color="#224d42")
    regno.place(relx=0.25,rely=0.2)
    regno.configure(state="readonly")
    yfstudy=customtkinter.CTkEntry(vat_details,width=190,height=10,
                                    corner_radius=10,text_color="black",border_color="#224d42")
    yfstudy.place(relx=0.25,rely=0.3)
    program_study=customtkinter.CTkEntry(vat_details,width=190,height=10,
                                    corner_radius=10,text_color="black",border_color="#224d42")
    program_study.place(relx=0.25,rely=0.4)
    def random_regitration_id():
        global var
        import random
        generated=''
        for i in range(8):
            generated +=str(random.randint(1,9))
            formarted=(f"{generated}")
        
        var=customtkinter.StringVar()
        var.set(formarted)
    random_regitration_id()  
    student_id=customtkinter.CTkEntry(vat_details,width=210,height=10,textvariable=var,state="readonly",
                                    corner_radius=10,text_color="black",border_color="#224d42",font=("bold",16))
    
    student_id.place(relx=0.7,rely=0.1)
    semister=customtkinter.CTkEntry(vat_details,width=210,height=10,
                                    corner_radius=10,text_color="black",border_color="#224d42")
    semister.place(relx=0.7,rely=0.2)
    altmail=customtkinter.CTkEntry(vat_details,width=210,height=10,
                                    corner_radius=10,text_color="black",border_color="#224d42")
    altmail.place(relx=0.7,rely=0.3)
    g_entry=customtkinter.CTkEntry(vat_details,width=210,height=10,
                                corner_radius=10,text_color="black",border_color="#224d42")
    g_entry.place(relx=0.7,rely=0.4)
    #upload frame
    photo=customtkinter.CTkFrame(student_registration_frame,width=290,height=300,fg_color="#bac4c1")
    photo.place(relx=0.78,rely=0.15)
    pic_path=tkinter.StringVar()
    pic_path.set('')
    
    def open_image():
        
        
        filepath=filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title="Upload your photocard",
                                            )
        if filepath:
            upload_img=customtkinter.CTkImage(light_image=Image.open(resource_path(filepath)),
                                          dark_image=Image.open(resource_path(filepath)),
                                          size=(260,250))
            pic_path.set(filepath)
            the_icon.configure(image=upload_img)

    alrt=("some fileds are empty")
    def input_validation():
        entries=[f_entry,s_entry,id_entry,dob_entry,ph_entry,ft_entry,mt_entry,
                 mail,regno,yfstudy,program_study,student_id]
        for i in entries:
            if i.get()=='':
                messagebox.showwarning("Warning",alrt)
               
        pic_data=''
        if pic_path.get() !='':
            # resize_pic=(Image.open(pic_path.get()).resize((100,100)))
            # resize_pic.save(pic_path)
            # read_data=open('temp.png','r')
            # pic_data=read_data.read()
            # read_data.close()
            # pic_data=resize_pic
            pic_data=pic_path.get()
        else:
            read_data=open('pics/backside.jpeg','rb')
            pic_data=read_data
            read_data.close()
        add_data(
             FIRST_NAME=f_entry.get(),
             SECOND_NAME=s_entry.get(),
             ID=id_entry.get(),
             DOB=dob_entry.get(),
             PHONE_NUMBER=ph_entry.get(),
             FATHER_NAME=ft_entry.get(),
             MOTHER_NAME=mt_entry.get(),
             GENDER=g_entry.get(),
             EMAIL=mail.get(),
             REGISTRATION_NUMBER=regno.get(),
             YEAR_OF_STUDY=yfstudy.get(),
             PROGRAM_OF_STUDY=program_study.get(),
             STUDENT_ID=student_id.get(),
             SEMISTER=semister.get(),
             photo=pic_data,
             )
        messagebox.showinfo("info","REGISTRATION DONE !\nPROCEED WITH LOGIN")
             

        
        

            
            
            
            
   

            
    
            
        
        
    log=customtkinter.CTkImage(light_image=Image.open(resource_path("pics/icons8-photo-48.png")),
                            dark_image=Image.open(resource_path('pics/icons8-photo-48.png')),
                            size=(260,250))
    the_icon=customtkinter.CTkLabel(photo,image=log,corner_radius=20,text="")
    the_icon.pack()
    
        
    
    upload_button=customtkinter.CTkButton(photo,text="UPLOAD", text_color='white',command= open_image)
    upload_button.pack()
    functions=customtkinter.CTkFrame(student_registration_frame,width=290,height=350,fg_color="transparent",bg_color="transparent",
                                    )
    functions.place(relx=0.78,rely=0.58)
    # customtkinter.CTkLabel(functions,image=image1).pack()
    save=customtkinter.CTkButton(functions,text="SAVE",text_color="white",fg_color="green")
    save.place(relx=0.30,rely=0.20)
    delete=customtkinter.CTkButton(functions,text='DELETE',text_color="white",fg_color='red',corner_radius=15)
    delete.place(relx=0.30,rely=0.40)
    
    submit=customtkinter.CTkButton(functions,text="SUBMIT",text_color="white",fg_color="blue",command=input_validation)
    submit.place(relx=0.30,rely=0.60)
    def back_to_home():
        student_registration_frame.destroy()
        window.update()
        home_window() 
    back=customtkinter.CTkButton(functions,text='BACK',text_color="white",fg_color='black',corner_radius=15,command=back_to_home)
    back.place(relx=0.30,rely=0.78)



def news_and_events():
    news_frame=customtkinter.CTkFrame(window,width=1000,height=650,fg_color='black',corner_radius=20)
    news_frame.place(relx=0.15,rely=0.05)
    title=customtkinter.CTkLabel(window,text="TODAYS NEWS AND EVENTS",text_color="white",font=("bold",16),fg_color="#3B9EBF",
                                 bg_color="transparent")
    
    title.place(relx=0.46,rely=0.01)
    def forward_to_mainwindow():
        news_frame.destroy()
        window.update()
        home_window()
    
    backbutton=customtkinter.CTkButton(window,text="(↩Back",font=('Helvetica',10),fg_color="red",text_color="white",command=forward_to_mainwindow,width=40)
    backbutton.place(relx=0.0,rely=0.01)
    global current_image_index
    def update_image():
        global current_image_index
        img=images[current_image_index]
        ctk_img=customtkinter.CTkImage(light_image=img,
                                    dark_image=img,
                                    size=(999,649))
        image_label.configure(image=ctk_img)
        current_image_index +=1
        
        if current_image_index >=len(images):
            current_image_index=0
        news_frame.after(3000,update_image)
        
        
    image_files=[
'pics/news/attendancematters2.jpg',
'pics/news/images (2) (1).jpeg',
'pics/news/images (3) (1).jpeg',
'pics/news/images (3).jpeg',
'pics/news/images (6).jpeg',
'pics/news/images (7) (1).jpeg',
'pics/news/images (8).jpeg',
'pics/news/images (9).jpeg',
'pics/news/images (10).jpeg',
'pics/news/images (11).jpeg',
'pics/news/images (12).jpeg',
'pics/news/images (13).jpeg',
'pics/news/images (14).jpeg',
'pics/news/images (15).jpeg',
'pics/news/images (16).jpeg',
'pics/news/images (17).jpeg',
'pics/news/images (18).jpeg',
'pics/news/images (19).jpeg',
'pics/news/images (22).jpeg',
'pics/news/images (21).jpeg',
'pics/news/images (20).jpeg',
   
    

     
    ]
        
    images=[Image.open(resource_path(img_file)) for img_file in image_files]
    image_label=customtkinter.CTkLabel(news_frame,text="")
    image_label.pack()

    current_image_index=0
    update_image()



def students_dashboard():
    dashboard_frame=customtkinter.CTkFrame(window,width=1200,height=766,fg_color='black',corner_radius=20)
    dashboard_frame.place(relx=0.10,rely=0.05)
    dashicon=customtkinter.CTkImage(light_image=Image.open(resource_path('pics/icons/icons8-dashboard-50.png')),
                                    dark_image=Image.open(resource_path('pics/icons/icons8-dashboard-50.png')),
                                    size=(45,50)
                                    )
    accountsetingsicon=customtkinter.CTkImage(light_image=Image.open(resource_path('pics/icons/icons8-account-settings-50.png')),
                                        dark_image=Image.open(resource_path('pics/icons/icons8-account-settings-50.png')),
                                        size=(30,20)
                                        )
    accounticon=customtkinter.CTkImage(light_image=Image.open(resource_path('pics/icons/icons8-account-24.png')),
                                        dark_image=Image.open(resource_path('pics/icons/icons8-account-24.png')),
                                        size=(30,20)
                                        )   
    annoucementicon=customtkinter.CTkImage(light_image=Image.open(resource_path('pics/icons/icons8-announcement-50.png')),
                                        dark_image=Image.open(resource_path('pics/icons/icons8-announcement-50.png')),
                                        size=(30,20)
                                        ) 
    financeicon=customtkinter.CTkImage(light_image=Image.open(resource_path('pics/icons/icons8-coin-wallet-50.png')),
                                        dark_image=Image.open(resource_path('pics/icons/icons8-coin-wallet-50.png')),
                                        size=(30,20)
                                        )
    courseicon=customtkinter.CTkImage(light_image=Image.open(resource_path('pics/icons/icons8-course-50.png')),
                                        dark_image=Image.open(resource_path('pics/icons/icons8-course-50.png')),
                                        size=(30,20)
                                        ) 
    examicon=customtkinter.CTkImage(light_image=Image.open(resource_path('pics/icons/icons8-exam-50.png')),
                                        dark_image=Image.open(resource_path('pics/icons/icons8-exam-50.png')),
                                        size=(30,20)
                                        )
    gradeicon=customtkinter.CTkImage(light_image=Image.open(resource_path('pics/icons/icons8-grades-50.png')),
                                        dark_image=Image.open(resource_path('pics/icons/icons8-grades-50.png')),
                                        size=(30,20)
                                        )
    homeworkicon=customtkinter.CTkImage(light_image=Image.open(resource_path('pics/icons/icons8-homework-50.png')),
                                        dark_image=Image.open(resource_path('pics/icons/icons8-homework-50.png')),
                                        size=(30,20)
                                        )   
    librayicon=customtkinter.CTkImage(light_image=Image.open(resource_path('pics/icons/icons8-library-50.png')),
                                        dark_image=Image.open(resource_path('pics/icons/icons8-library-50.png')),
                                        size=(30,20)
                                        ) 
    logouticon=customtkinter.CTkImage(light_image=Image.open(resource_path('pics/icons/icons8-log-out-50.png')),
                                        dark_image=Image.open(resource_path('pics/icons/icons8-log-out-50.png')),
                                        size=(30,20)
                                        )
    notificationicon=customtkinter.CTkImage(light_image=Image.open(resource_path('pics/icons/icons8-notification-50.png')),
                                        dark_image=Image.open(resource_path('pics/icons/icons8-notification-50.png')),
                                        size=(30,20)
                                        ) 
    schedulesicon=customtkinter.CTkImage(light_image=Image.open(resource_path('pics/icons/icons8-schedule-50.png')),
                                        dark_image=Image.open(resource_path('pics/icons/icons8-schedule-50.png')),
                                        size=(30,20)
                                        ) 

    title=customtkinter.CTkLabel(window,text="Dashboard",text_color="white",font=("bold",16),fg_color="#3B9EBF",
                                 bg_color="transparent")
    
    title.place(relx=0.46,rely=0.01)

       

    def forward_to_mainwindow():
        dashboard_frame.destroy()
        window.update()
        home_window()
    backbutton=customtkinter.CTkButton(dashboard_frame,text="(↩Back",font=('Helvetica',10),fg_color="red",text_color="white",command=forward_to_mainwindow,width=30)
    backbutton.place(relx=0.01,rely=0.01)
    
    dash_frame=customtkinter.CTkFrame(dashboard_frame,fg_color="#152238",width=400,height=750)
    dash_frame.place(relx=0.0,rely=0.0)
    pic=customtkinter.CTkImage(light_image=Image.open(resource_path('pics/dash.png')),
                               dark_image=Image.open(resource_path('pics/dash.png')),
                               size=(1200,764))
    image=customtkinter.CTkLabel(dashboard_frame,text='',image=pic)
    image.place(relx=0.28,rely=0.0)
       
    def dash_buttons():
        font=customtkinter.CTkFont(underline=True,family="Roboto",size=15,weight="bold",slant="roman")
        dashboard=customtkinter.CTkLabel(dashboard_frame,text="Dashboard",font=font,text_color='white',fg_color="#152238")
        dashboard.place(relx=0.05,rely=0.02)
        dash_icon=customtkinter.CTkLabel(dash_frame,text="",image=dashicon,corner_radius=30)
        dash_icon.place(relx=0.0,rely=0.01)
       
        academics=customtkinter.CTkLabel(dashboard_frame,text="Academics",font=font,text_color='white',fg_color="#152238")
        academics.place(relx=0.02,rely=0.15)
        
        schedule=customtkinter.CTkButton(dash_frame,image=schedulesicon,text="schedule",text_color="white",fg_color="#152238",corner_radius=30)
        schedule.place(relx=0.03,rely=0.20)
        
        exam=customtkinter.CTkButton(dash_frame,image=examicon,text="Exam Board",text_color="white",fg_color="#152238",corner_radius=30)
        exam.place(relx=0.03,rely=0.25)
        
        homewrk=customtkinter.CTkButton(dash_frame,image=homeworkicon,text="Home Work",text_color="white",fg_color="#152238",corner_radius=30)
        homewrk.place(relx=0.03,rely=0.30)
        
        grade=customtkinter.CTkButton(dash_frame,image=gradeicon,text="Grade report",text_color="white",fg_color="#152238",corner_radius=30)
        grade.place(relx=0.03,rely=0.35)
        
        enroll=customtkinter.CTkButton(dash_frame,image=courseicon,text="Course plan",text_color="white",fg_color="#152238",corner_radius=30)
        enroll.place(relx=0.03,rely=0.40)
        
        lib=customtkinter.CTkButton(dash_frame,image=librayicon,text="Libraries",text_color="white",fg_color="#152238",corner_radius=30)
        lib.place(relx=0.03,rely=0.45)
        
        cash=customtkinter.CTkButton(dash_frame,image=financeicon,text="Finance",text_color="white",fg_color="#152238",corner_radius=30)
        cash.place(relx=0.03,rely=0.50)
        
        loud=customtkinter.CTkButton(dash_frame,image=annoucementicon,text="Announcements",text_color="white",fg_color="#152238",corner_radius=30)
        loud.place(relx=0.03,rely=0.55)
        
        settings=customtkinter.CTkLabel(dashboard_frame,text="Settings",font=font,text_color='white',fg_color="#152238")
        settings.place(relx=0.02,rely=0.57)
        
        acct=customtkinter.CTkButton(dash_frame,image=accounticon,text="Accounts",text_color="white",fg_color="#152238",corner_radius=30)
        acct.place(relx=0.03,rely=0.62)
        
        actset=customtkinter.CTkButton(dash_frame,image=accountsetingsicon,text="Account Settings",text_color="white",fg_color="#152238",corner_radius=30)
        actset.place(relx=0.03,rely=0.67)
        
        notfication=customtkinter.CTkButton(dash_frame,image=notificationicon,text="Notificatios",text_color="white",fg_color="#152238",corner_radius=30)
        notfication.place(relx=0.03,rely=0.72)
        
        logout=customtkinter.CTkButton(dash_frame,image=logouticon,text="Log-Out",text_color="white",fg_color="#152238",corner_radius=30)
        logout.place(relx=0.03,rely=0.77)
        backbutton=customtkinter.CTkButton(dashboard_frame,text="(↩Back",font=('Helvetica',10),fg_color="red",text_color="white",command=forward_to_mainwindow,width=30)
        backbutton.place(relx=0.03,rely=0.81)
    dash_buttons()



def int_database():
    if os.path.exists(resource_path("data_details.db")):
       pass
    else:
        
        conn = sqlite3.connect(get_writable_db_path(resource_path("data_details.db")))

        c = conn.cursor()


        c.execute(""" CREATE TABLE data
                  (
                             FIRST_NAME text,
                             SECOND_NAME text,
                             ID   text,
                             DOB  text,
                             PHONE_NUMBER text,
                             FATHERS_NAME  text,
                             MOTHERS_NAME  text,
                             GENDER text,
                             EMAIL   text,
                             REGISTRATION_NUMBER text,
                             YEAR_OF_STUDY text,
                             PROGRAM_OF_STUDY text,
                             STUDENT_ID text,
                             SEMISTER text,
                             photo  blob
                )
                """)
        conn.commit()
        conn.close()
    
int_database()
def add_data(FIRST_NAME, SECOND_NAME,ID,
             DOB,PHONE_NUMBER,FATHER_NAME,
             MOTHER_NAME,GENDER,EMAIL,
             REGISTRATION_NUMBER,YEAR_OF_STUDY,PROGRAM_OF_STUDY,
             STUDENT_ID,SEMISTER,photo):
    conn = sqlite3.connect(get_writable_db_path(resource_path("data_details.db")))
    c = conn.cursor()
  
    c.execute(f"""INSERT INTO data (FIRST_NAME,SECOND_NAME,ID,DOB,PHONE_NUMBER,FATHERS_NAME,MOTHERS_NAME,GENDER,EMAIL,REGISTRATION_NUMBER,YEAR_OF_STUDY,PROGRAM_OF_STUDY,STUDENT_ID,SEMISTER,photo)
              VALUES('{FIRST_NAME}','{SECOND_NAME}','{ID}',
              '{DOB}','{PHONE_NUMBER}','{FATHER_NAME}','{MOTHER_NAME}','{GENDER}',
             '{EMAIL}','{REGISTRATION_NUMBER}','{YEAR_OF_STUDY}','{PROGRAM_OF_STUDY}',
             '{STUDENT_ID}','{SEMISTER}',?)""",(photo,))
    conn.commit()
    conn.close()
# a= 'ML/3532G/24'
# b=24487436
def show_data():
    conn = sqlite3.connect(get_writable_db_path(resource_path("data_details.db")))
    c = conn.cursor()
      
    # c.execute("DELETE FROM data WHERE rowid >2" )
    c.execute("SELECT rowid, * FROM data")
    details=c.fetchall()
    for i in details:
        print(i)

    conn.commit()
    
    conn.close()




home_window()
window.mainloop()
