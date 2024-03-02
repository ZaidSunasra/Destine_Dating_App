from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import phonenumbers
from pyisemail import is_email

global dashboard_frame, profile_button, match_button, chat_button, setting_button  # For Switching between sections
global resized_signup_img  # For image in signup page
global setting_icon, setting_icon_white, chat_icon, chat_icon_white, match_icon, match_icon_white, profile_icon, profile_icon_white  # For changing button color
global name_entry, signup_warning, pass_entry, confirm_pass_entry, phone_no_entry, email_entry, user_name_entry, gender  # For signing up user
global profile_age_entry, religion_selected, sport_selected, hobby_selected, music_selected  # For saving preference
global delete_icon, logout_icon, warning  # For images in setting section
global forgot, forgot_username_entry, check_contact_entry, check_email_entry, new_password_entry, confirm_password_entry  # For forgot password frame
global match_list, no_record_label  # For matching


def hide_password():
    show.configure(file="Images/show.png")
    password_entry.configure(show="*")
    show_button.configure(command=show_password)


def show_password():
    show.configure(file="Images/hide.png")
    password_entry.configure(show="")
    show_button.configure(command=hide_password)


def clear():
    username_entry.delete(0, END)
    password_entry.delete(0, END)


def current_frame():
    profile_button.configure(bg="white", fg="#666f80", image=profile_icon)
    match_button.configure(bg="white", fg="#666f80", image=match_icon)
    chat_button.configure(bg="white", fg="#666f80", image=chat_icon)
    setting_button.configure(bg="white", fg="#666f80", image=setting_icon)


def profile_section():
    global profile_icon_white, profile_age_entry, religion_selected, sport_selected, hobby_selected, music_selected

    profile_section_frame = Frame(dashboard_frame, bg="white", width=1236, height=app.winfo_height())
    profile_section_frame.place(x=300, y=0)

    profile_heading_label = Label(profile_section_frame, text="Enter Your Choice", font=("Proxima Nova", 40, "bold"), fg="#fb6d6c", bg="white")
    profile_heading_label.place(x=380, y=30)

    query = "USE destine"
    my_database_cursor.execute(query)

    query = "SELECT Age FROM user_preference WHERE Username=%s"
    my_database_cursor.execute(query, (username_entry.get(), ))
    age_value = my_database_cursor.fetchone()
    profile_age_label = Label(profile_section_frame, text="Age", font=("Proxima Nova", 14), bg="white", fg="#666f80")
    profile_age_label.place(x=380, y=200)
    profile_age_entry = Entry(profile_section_frame, font=("Proxima Nova", 14), bg="white", fg="#666f80", bd=0)
    profile_age_entry.place(x=600, y=200)
    profile_age_entry.insert(0, "%s" % age_value)
    highlight_frame = Frame(profile_section_frame, bg="#c3c8d3", width=224, height=2)
    highlight_frame.place(x=600, y=225)

    query = "SELECT Religion FROM user_preference WHERE Username=%s"
    my_database_cursor.execute(query, (username_entry.get(), ))
    religion_value = my_database_cursor.fetchone()
    profile_religion_label = Label(profile_section_frame, text="Religion", font=("Proxima Nova", 14), bg="white", fg="#666f80")
    profile_religion_label.place(x=380, y=270)
    religion_selected = StringVar()
    religion_selected.set("%s" % religion_value)
    profile_religion_option = OptionMenu(profile_section_frame, religion_selected, "Muslim", "Hindu", "Christian", "Sikh", "Jain")
    profile_religion_option.place(x=600, y=270)
    profile_religion_option.configure(width=17, bg="white", fg="#666f80", font=("Proxima Nova", 14), bd=0, activeforeground="white", activebackground="#fb6d6c")

    query = "SELECT Sport FROM user_preference WHERE Username=%s"
    my_database_cursor.execute(query, (username_entry.get(),))
    sport_value = my_database_cursor.fetchone()
    profile_sport_label = Label(profile_section_frame, text="Fav. Sport", font=("Proxima Nova", 14), bg="white", fg="#666f80")
    profile_sport_label.place(x=380, y=340)
    sport_selected = StringVar()
    sport_selected.set("%s" % sport_value)
    profile_sport_option = OptionMenu(profile_section_frame, sport_selected, "Football", "Cricket", "Basketball", "Volleyball", "Badminton")
    profile_sport_option.place(x=600, y=340)
    profile_sport_option.configure(width=17, bg="white", fg="#666f80", font=("Proxima Nova", 14), bd=0, activeforeground="white", activebackground="#fb6d6c")

    query = "SELECT Hobby FROM user_preference WHERE Username=%s"
    my_database_cursor.execute(query, (username_entry.get(), ))
    hobby_value = my_database_cursor.fetchone()
    profile_hobby_label = Label(profile_section_frame, text="Hobby", font=("Proxima Nova", 14), bg="white", fg="#666f80")
    profile_hobby_label.place(x=380, y=410)
    hobby_selected = StringVar()
    hobby_selected.set("%s" % hobby_value)
    profile_hobby_option = OptionMenu(profile_section_frame, hobby_selected, "Art", "Cooking", "Dancing & Singing", "Watching Movies", "Playing Games", "Listening Songs")
    profile_hobby_option.place(x=600, y=410)
    profile_hobby_option.configure(width=17, bg="white", fg="#666f80", font=("Proxima Nova", 14), bd=0, activeforeground="white", activebackground="#fb6d6c")

    query = "SELECT Music FROM user_preference WHERE Username=%s"
    my_database_cursor.execute(query, (username_entry.get(), ))
    music_value = my_database_cursor.fetchone()
    profile_music_label = Label(profile_section_frame, text="Music", font=("Proxima Nova", 14), bg="white", fg="#666f80")
    profile_music_label.place(x=380, y=480)
    music_selected = StringVar()
    music_selected.set("%s" % music_value)
    profile_music_option = OptionMenu(profile_section_frame, music_selected, "Rock Music", "Lofi", "Rap", "Country Music", "Classical Music")
    profile_music_option.place(x=600, y=480)
    profile_music_option.configure(width=17, bg="white", fg="#666f80", font=("Proxima Nova", 14), bd=0, activeforeground="white", activebackground="#fb6d6c")

    save_button = Button(profile_section_frame, text="Save", bg="#666f80", fg="white", font=("Proxima Nova", 20, "bold"), width=7, command=save_preference)
    save_button.place(x=500, y=575)

    current_frame()
    profile_icon_white = ImageTk.PhotoImage(Image.open("Images/profile_white.png"))
    profile_button.configure(bg="#fb6d6c", fg="white", image=profile_icon_white)


def save_preference():
    update = "UPDATE user_preference SET Age=%s, Religion=%s, Sport=%s, Hobby=%s, Music=%s WHERE Username=%s"
    my_database_cursor.execute(update, (profile_age_entry.get(), religion_selected.get(), sport_selected.get(), hobby_selected.get(), music_selected.get(), username_entry.get(),))
    my_database.commit()


def match_section():
    global match_icon_white, match_list, no_record_label

    match_section_frame = Frame(dashboard_frame, bg="white", width=1236, height=app.winfo_height())
    match_section_frame.place(x=300, y=0)

    match_title_label = Label(match_section_frame, text="Your Match", font=("Proxima Nova", 40, "bold"), fg="#fb6d6c", bg="white")
    match_title_label.place(x=500, y=30)

    find_match_button = Button(match_section_frame, text="Find Match", bg="#fb6d6c", font=("Proxima Nova", 20, "bold"), fg="#666f80", width=11, command=find_match)
    find_match_button.place(x=900, y=750)

    match_list = ttk.Treeview(match_section_frame, height=20)
    style = ttk.Style()
    style.configure("Treeview.Heading", foreground="#fb6d6c", background="white", font=("Proxima Nova", 18, "bold"))
    match_list["columns"] = ("1", "2", "3", "4", "5", "6", "7")
    match_list["show"] = "headings"
    match_list.column("1", anchor=CENTER, width=150)
    match_list.column("2", anchor=CENTER, width=150)
    match_list.column("3", anchor=CENTER, width=150)
    match_list.column("4", anchor=CENTER, width=150)
    match_list.column("5", anchor=CENTER, width=150)
    match_list.column("6", anchor=CENTER, width=150)
    match_list.column("7", anchor=CENTER, width=150)
    match_list.heading("1", text="Name")
    match_list.heading("2", text="Gender")
    match_list.heading("3", text="Age")
    match_list.heading("4", text="Religion")
    match_list.heading("5", text="Sport")
    match_list.heading("6", text="Hobby")
    match_list.heading("7", text="Music")

    match_list.place(x=100, y=150)

    no_record_label = Label(match_section_frame, text="", bg="white", fg="#fb6d6c", font=("Proxima Nova", 18, "bold"))
    no_record_label.place(x=100, y=750)

    current_frame()
    match_icon_white = ImageTk.PhotoImage(Image.open("Images/match_white.png"))
    match_button.configure(bg="#fb6d6c", fg="white", image=match_icon_white)


def find_match():
    for row in match_list.get_children():
        match_list.delete(row)

    query = "USE destine"
    my_database_cursor.execute(query)
    query = "SELECT Gender FROM user_info WHERE Username=%s"
    my_database_cursor.execute(query, (username_entry.get(),))
    gender_val = my_database_cursor.fetchone()
    gender_value = "%s" % gender_val

    query = "SELECT Name, Gender, Age, Religion, Sport, Hobby, Music FROM user_info, user_preference WHERE Gender<>%s and Religion=%s and Sport=%s and Hobby=%s and Music=%s and user_info.Username = user_preference.Username"
    my_database_cursor.execute(query, (gender_value, religion_selected.get(), sport_selected.get(), hobby_selected.get(), music_selected.get()))
    rows = my_database_cursor.fetchall()
    if my_database_cursor.rowcount > 0:
        for row in rows:
            match_list.insert("", "end", values=row)

    query = "SELECT Name, Gender, Age, Religion, Sport, Hobby, Music FROM user_info, user_preference WHERE Gender<>%s and Religion=%s and Sport<>%s and Hobby=%s and Music=%s and user_info.Username = user_preference.Username"
    my_database_cursor.execute(query, (gender_value, religion_selected.get(), sport_selected.get(), hobby_selected.get(), music_selected.get()))
    rows = my_database_cursor.fetchall()
    if my_database_cursor.rowcount > 0:
        for row in rows:
            match_list.insert("", "end", values=row)

    query = "SELECT Name, Gender, Age, Religion, Sport, Hobby, Music FROM user_info, user_preference WHERE Gender<>%s and Religion=%s and Sport=%s and Hobby<>%s and Music=%s and user_info.Username = user_preference.Username"
    my_database_cursor.execute(query, (gender_value, religion_selected.get(), sport_selected.get(), hobby_selected.get(), music_selected.get()))
    rows = my_database_cursor.fetchall()
    if my_database_cursor.rowcount > 0:
        for row in rows:
            match_list.insert("", "end", values=row)

    query = "SELECT Name, Gender, Age, Religion, Sport, Hobby, Music FROM user_info, user_preference WHERE Gender<>%s and Religion=%s and Sport=%s and Hobby=%s and Music<>%s and user_info.Username = user_preference.Username"
    my_database_cursor.execute(query, (gender_value, religion_selected.get(), sport_selected.get(), hobby_selected.get(), music_selected.get()))
    rows = my_database_cursor.fetchall()
    if my_database_cursor.rowcount > 0:
        for row in rows:
            match_list.insert("", "end", values=row)

    query = "SELECT Name, Gender, Age, Religion, Sport, Hobby, Music FROM user_info, user_preference WHERE Gender<>%s and Religion<>%s and Sport=%s and Hobby=%s and Music=%s and user_info.Username = user_preference.Username"
    my_database_cursor.execute(query, (gender_value, religion_selected.get(), sport_selected.get(), hobby_selected.get(), music_selected.get()))
    rows = my_database_cursor.fetchall()
    if my_database_cursor.rowcount > 0:
        for row in rows:
            match_list.insert("", "end", values=row)

    if len(match_list.get_children()) == 0:
        no_record_label.configure(text="No Match Found")


def chat_section():
    global chat_icon_white

    chat_section_frame = Frame(dashboard_frame, bg="white", width=1236, height=app.winfo_height())
    chat_section_frame.place(x=300, y=0)
    current_frame()
    chat_icon_white = ImageTk.PhotoImage(Image.open("Images/chat_white.png"))
    chat_button.configure(bg="#fb6d6c", fg="white", image=chat_icon_white)


def setting_section():
    global setting_icon_white, delete_icon, logout_icon

    setting_section_frame = Frame(dashboard_frame, bg="white", width=1236, height=app.winfo_height())
    setting_section_frame.place(x=300, y=0)

    setting_label = Label(setting_section_frame, text="Setting", font=("Proxima Nova", 40, "bold"), fg="#fb6d6c", bg="white")
    setting_label.place(x=500, y=30)

    delete_account_label = Label(setting_section_frame, text="Delete Account", font=("Proxima Nova", 20, "bold"), fg="#fb6d6c", bg="white")
    delete_account_label.place(x=200, y=150)
    delete_icon = ImageTk.PhotoImage(Image.open("Images/delete.png"))
    delete_account_button = Button(setting_section_frame, image=delete_icon, compound=LEFT, text="Delete", bg="#fb6d6c", font=("Proxima Nova", 20, "bold"), fg="#666f80", width=200, command=delete_account)
    delete_account_button.place(x=800, y=150)

    logout_label = Label(setting_section_frame, text="Sign Out", font=("Proxima Nova", 20, "bold"), fg="#fb6d6c", bg="white")
    logout_label.place(x=200, y=250)
    logout_icon = ImageTk.PhotoImage(Image.open("Images/logout.png"))
    logout_button = Button(setting_section_frame, image=logout_icon, compound=LEFT, text="Logout", bg="#fb6d6c", font=("Proxima Nova", 20, "bold"), fg="#666f80", width=200, command=loginpage)
    logout_button.place(x=800, y=250)

    current_frame()
    setting_icon_white = ImageTk.PhotoImage(Image.open("Images/setting_white.png"))
    setting_button.configure(bg="#fb6d6c", fg="white", image=setting_icon_white)


def delete_account():
    global warning

    warning = Toplevel(app)
    warning.geometry("400x200")
    warning.resizable(height=FALSE, width=FALSE)
    warning.configure(bg="white")
    delete_account_label = Label(warning, text="This will delete your Account \n This action can't be undone", fg="#fb6d6c", bg="white", font=("Proxima Nova", 18, "bold"))
    delete_account_label.place(x=30, y=30)
    confirm_delete_button = Button(warning, text="Go Ahead", fg="white", bg="#fd6d6c", font=("Proxima Nova", 16, "bold"), command=confirm_delete)
    confirm_delete_button.place(x=150, y=110)
    warning.mainloop()


def confirm_delete():
    query = "USE destine"
    my_database_cursor.execute(query)
    query = "DELETE FROM user_preference WHERE Username=%s"
    my_database_cursor.execute(query, (username_entry.get(),))
    query = "DELETE FROM user_info WHERE Username=%s"
    my_database_cursor.execute(query, (username_entry.get(),))
    my_database.commit()
    warning.destroy()
    loginpage()


def dashboard():
    query = "USE destine"
    my_database_cursor.execute(query)
    query = "SELECT * FROM user_info WHERE Username=%s and Password=%s"
    my_database_cursor.execute(query, (username_entry.get(), password_entry.get()))
    row = my_database_cursor.fetchone()
    if row is None:
        messagebox.showinfo("Error", "Invalid Username or Password")

    else:

        global dashboard_frame, profile_button, match_button, chat_button, setting_button, setting_icon, chat_icon, match_icon, profile_icon

        dashboard_frame = Frame(app, bg="white", height=app.winfo_height(), width=app.winfo_width())
        dashboard_frame.place(x=0, y=0)

        option_frame = Frame(dashboard_frame, height=app.winfo_height(), width=300, bg="#c3c8d3")
        option_frame.place(x=0, y=0)

        app_name_dashboard = Label(option_frame, text="Destine", font=("Edwardian Script ITC", 60, "bold"), bg="#c3c8d3", fg="#fb6d6c", width="6")
        app_name_dashboard.place(x=10, y=35)

        profile_icon = ImageTk.PhotoImage(Image.open("Images/profile.png"))
        profile_button = Button(option_frame, image=profile_icon, compound=TOP, text="Profile", font=("Proxima Nova", 14, "bold"), fg="#666f80", bg="white", height=125, width=170, command=profile_section)
        profile_button.place(x=50, y=150)

        match_icon = ImageTk.PhotoImage(Image.open("Images/match.png"))
        match_button = Button(option_frame, image=match_icon, compound=TOP, text="Your Match", font=("Proxima Nova", 14, "bold"), fg="#666f80", bg="white", height=125, width=170, command=match_section)
        match_button.place(x=50, y=300)

        chat_icon = ImageTk.PhotoImage(Image.open("Images/chat.png"))
        chat_button = Button(option_frame, image=chat_icon, compound=TOP, text="Chats", font=("Proxima Nova", 14, "bold"), fg="#666f80", bg="white", height=125, width=170, command=chat_section)
        chat_button.place(x=50, y=450)

        setting_icon = ImageTk.PhotoImage(Image.open("Images/setting.png"))
        setting_button = Button(option_frame, image=setting_icon, compound=TOP, text="Setting", font=("Proxima Nova", 14, "bold"), fg="#666f80", bg="white", height=125, width=170, command=setting_section)
        setting_button.place(x=50, y=600)


def forgot_password():
    global forgot, forgot_username_entry, check_contact_entry, check_email_entry, new_password_entry, confirm_password_entry

    forgot = Toplevel(app)
    forgot.geometry("550x400")
    forgot.resizable(height=FALSE, width=FALSE)
    forgot.title("Forgot Password")
    forgot.iconbitmap("Images/favicon.ico")
    forgot.configure(bg="white")

    forgot_username_label = Label(forgot, text="Enter Username:", fg="#666f80", bg="white", font=("Proxima Nova", 14))
    forgot_username_label.place(x=50, y=50)
    forgot_username_entry = Entry(forgot, bg="white", fg="#666f80", font=("Proxima Nova", 14), bd=0)
    forgot_username_entry.place(x=275, y=50)
    forgot_underline_frame = Frame(forgot, bg="#c3c8d3", height=2, width=225)
    forgot_underline_frame.place(x=275, y=75)

    check_contact_label = Label(forgot, text="Enter Contact No:", fg="#666f80", bg="white", font=("Proxima Nova", 14))
    check_contact_label.place(x=50, y=100)
    check_contact_entry = Entry(forgot, bg="white", fg="#666f80", font=("Proxima Nova", 14), bd=0)
    check_contact_entry.place(x=275, y=100)
    forgot_underline_frame = Frame(forgot, bg="#c3c8d3", height=2, width=225)
    forgot_underline_frame.place(x=275, y=125)

    check_email_label = Label(forgot, text="Enter Email ID:", fg="#666f80", bg="white", font=("Proxima Nova", 14))
    check_email_label.place(x=50, y=150)
    check_email_entry = Entry(forgot, bg="white", fg="#666f80", font=("Proxima Nova", 14), bd=0)
    check_email_entry.place(x=275, y=150)
    forgot_underline_frame = Frame(forgot, bg="#c3c8d3", height=2, width=225)
    forgot_underline_frame.place(x=275, y=175)

    new_password_label = Label(forgot, text="Enter New Password:", fg="#666f80", bg="white", font=("Proxima Nova", 14))
    new_password_label.place(x=50, y=200)
    new_password_entry = Entry(forgot, bg="white", fg="#666f80", font=("Proxima Nova", 14), bd=0)
    new_password_entry.place(x=275, y=200)
    forgot_underline_frame = Frame(forgot, bg="#c3c8d3", height=2, width=225)
    forgot_underline_frame.place(x=275, y=225)

    confirm_password_label = Label(forgot, text="Confirm New Password:", fg="#666f80", bg="white", font=("Proxima Nova", 14))
    confirm_password_label.place(x=50, y=250)
    confirm_password_entry = Entry(forgot, bg="white", fg="#666f80", font=("Proxima Nova", 14), bd=0)
    confirm_password_entry.place(x=275, y=250)
    forgot_underline_frame = Frame(forgot, bg="#c3c8d3", height=2, width=225)
    forgot_underline_frame.place(x=275, y=275)

    forgot_password_button = Button(forgot, text="Save", bg="#666f80", fg="white", font=("Proxima Nova", 20, "bold"), width=7, command=save_password)
    forgot_password_button.place(x=200, y=310)


def save_password():
    if forgot_username_entry.get() == "" or check_contact_entry.get == "" or check_email_entry.get() == "" or new_password_entry.get() == "" or confirm_password_entry.get() == "":
        forgot.destroy()
        messagebox.showinfo("Error", "All fields required.")
    elif confirm_password_entry.get() != new_password_entry.get():
        forgot.destroy()
        messagebox.showinfo("Error", "Password Mismatch")

    query = "USE destine"
    my_database_cursor.execute(query)
    query = "SELECT * FROM user_info WHERE Username=%s and Contact=%s and Email=%s"
    my_database_cursor.execute(query, (forgot_username_entry.get(), check_contact_entry.get(), check_email_entry.get()))
    row = my_database_cursor.fetchone()
    if row is not None:
        update = "UPDATE user_info SET Password=%s WHERE Username=%s"
        my_database_cursor.execute(update, (confirm_password_entry.get(), forgot_username_entry.get()))
        my_database.commit()
        messagebox.showinfo("Success", "Password Changed")
        forgot.destroy()
    else:
        messagebox.showinfo("Error", "Incorrect Credentials")
        forgot.destroy()


def signupform():
    global resized_signup_img, name_entry, signup_warning, pass_entry, confirm_pass_entry, phone_no_entry, email_entry, user_name_entry, gender

    signupform_frame = Frame(app, bg="white", height=app.winfo_height(), width=app.winfo_width())
    signupform_frame.place(x=0, y=0)

    close_button = Button(signupform_frame, text="<  Back to Login Page", bg="#fb6d6c", fg="white", font=("Proxima Nova", 14, "bold"), width=20, command=loginpage)
    close_button.place(x=50, y=50)

    signup_img = Image.open("Images/signup.jpg")
    resize = signup_img.resize((500, 500), Image.LANCZOS)
    resized_signup_img = ImageTk.PhotoImage(resize)
    signup_img_label = Label(signupform_frame, image=resized_signup_img, width=500, height=500, borderwidth=0)
    signup_img_label.place(x=100, y=150)

    border_frame = Frame(signupform_frame, bg="#666f80")
    border_frame.place(x=800, y=150)
    signupform_label = Label(border_frame, width=68, height=35, bg="white")
    signupform_label.pack(padx=5, pady=5)

    name_label = Label(signupform_label, text="Name:", fg="#666f80", font=("Proxima Nova", 14), bg="white")
    name_label.place(x=30, y=50)
    name_entry = Entry(signupform_label, font=("Proxima Nova", 14), fg="#666f80", bd=0)
    name_entry.place(x=210, y=50)
    highlight_frame = Frame(signupform_label, bg="#c3c8d3", height=2, width=222)
    highlight_frame.place(x=210, y=74)

    email_label = Label(signupform_label, text="Email ID:", fg="#666f80", font=("Proxima Nova", 14), bg="white")
    email_label.place(x=30, y=100)
    email_entry = Entry(signupform_label, font=("Proxima Nova", 14), bd=0, fg="#666f80")
    email_entry.place(x=210, y=100)
    highlight_frame = Frame(signupform_label, bg="#c3c8d3", height=2, width=222)
    highlight_frame.place(x=210, y=124)

    phone_no_label = Label(signupform_label, text="Contact No:", fg="#666f80", font=("Proxima Nova", 14), bg="white")
    phone_no_label.place(x=30, y=150)
    phone_no_entry = Entry(signupform_label, font=("Proxima Nova", 14), bd=0, fg="#666f80")
    phone_no_entry.place(x=210, y=150)
    highlight_frame = Frame(signupform_label, bg="#c3c8d3", height=2, width=222)
    highlight_frame.place(x=210, y=174)

    gender_label = Label(signupform_label, text="Gender:", fg="#666f80", font=("Proxima Nova", 14), bg="white")
    gender_label.place(x=30, y=200)
    gender = StringVar()
    Radiobutton(signupform_label, text="Male", variable=gender, value="Male", bg="white", fg="#666f80", font=("Proxima Nova", 14)).place(x=210, y=200)
    Radiobutton(signupform_label, text="Female", variable=gender, value="Female", bg="white", fg="#666f80", font=("Proxima Nova", 14)).place(x=310, y=200)

    user_name_label = Label(signupform_label, text="User Name:", fg="#666f80", font=("Proxima Nova", 14), bg="white")
    user_name_label.place(x=30, y=250)
    user_name_entry = Entry(signupform_label, font=("Proxima Nova", 14), bd=0, fg="#666f80")
    user_name_entry.place(x=210, y=250)
    highlight_frame = Frame(signupform_label, bg="#c3c8d3", height=2, width=222)
    highlight_frame.place(x=210, y=274)

    pass_label = Label(signupform_label, text="Enter Password:", fg="#666f80", font=("Proxima Nova", 14), bg="white")
    pass_label.place(x=30, y=300)
    pass_entry = Entry(signupform_label, show="*", font=("Proxima Nova", 14), bd=0, fg="#666f80")
    pass_entry.place(x=210, y=300)
    highlight_frame = Frame(signupform_label, bg="#c3c8d3", height=2, width=222)
    highlight_frame.place(x=210, y=324)

    confirm_pass_label = Label(signupform_label, text="Re-enter Password:", fg="#666f80", font=("Proxima Nova", 14), bg="white")
    confirm_pass_label.place(x=30, y=350)
    confirm_pass_entry = Entry(signupform_label, show="*", font=("Proxima Nova", 14), bd=0, fg="#666f80")
    confirm_pass_entry.place(x=210, y=350)
    highlight_frame = Frame(signupform_label, bg="#c3c8d3", height=2, width=222)
    highlight_frame.place(x=210, y=374)

    signup_warning = Label(signupform_label, text="", font=("Proxima Nova", 12), bg="white", fg="#fb6d6c")
    signup_warning.place(x=30, y=400)

    sign_button = Button(signupform_label, text="Sign Up", bg="#666f80", fg="white", font=("Proxima Nova", 20, "bold"), width=7, command=create_account)
    sign_button.place(x=225, y=450)


def create_account():
    query = "SELECT * FROM user_info WHERE Username=%s"
    my_database_cursor.execute(query, (user_name_entry.get(),))
    row = my_database_cursor.fetchone()

    query = "SELECT * FROM user_info WHERE Contact=%s"
    my_database_cursor.execute(query, (phone_no_entry.get(),))
    row1 = my_database_cursor.fetchone()

    query = "SELECT * FROM user_info WHERE Email=%s"
    my_database_cursor.execute(query, (email_entry.get(),))
    row2 = my_database_cursor.fetchone()

    string_phone_no = "+91" + phone_no_entry.get()
    phone_no = phonenumbers.parse(string_phone_no)

    email = email_entry.get()

    if name_entry.get() == "" or pass_entry.get() == "" or confirm_pass_entry.get == "" or email_entry.get == "" or phone_no_entry.get() == "" or user_name_entry.get == "" or gender.get == "":
        messagebox.showinfo("Error", "All fields required")

    elif pass_entry.get() != confirm_pass_entry.get():
        messagebox.showinfo("Error", "Password Not matching")

    elif row is not None:
        messagebox.showinfo("Error", "Username already exist. Please use different username")

    elif phonenumbers.is_valid_number(phone_no) is False:
        messagebox.showinfo("Error", "Invalid phone number")

    elif is_email(email) is False:
        messagebox.showinfo("Error", "Invalid email address")

    elif row1 is not None:
        messagebox.showinfo("Error", "Contact already used")

    elif row2 is not None:
        messagebox.showinfo("Error", "Email already used")

    else:
        query = "INSERT INTO user_info(Name,Email,Contact,Gender,Username,Password) VALUES(%s,%s,%s,%s,%s,%s)"
        my_database_cursor.execute(query, (name_entry.get(), email_entry.get(), phone_no_entry.get(), gender.get(), user_name_entry.get(), pass_entry.get()))
        query = "INSERT INTO user_preference(Username, Age, Religion, Sport, Hobby, Music) VALUES(%s, %s, %s, %s, %s, %s)"
        my_database_cursor.execute(query, (user_name_entry.get(), "0", "Not Selected", "Not Selected", "Not Selected", "Not Selected"))
        my_database.commit()
        signupform()
        signup_warning.config(text="Registration Successful")


def loginpage():
    start_frame.tkraise()
    clear()


# General main frame setting
app = Tk()
app.state('zoomed')
app.title("Destine Dating App")
app.resizable(height=FALSE, width=FALSE)
app.configure(bg="white")
app.iconbitmap("Images/favicon.ico")

my_database = mysql.connector.connect(host="localhost", user="root", passwd="", database="destine",)
my_database_cursor = my_database.cursor()
# my_database_cursor.execute("CREATE DATABASE destine")
# my_database_cursor.execute("CREATE TABLE user_info(Name VARCHAR (255), Email VARCHAR (255), Contact BIGINT, Gender VARCHAR (10), Username VARCHAR (255) PRIMARY KEY, Password VARCHAR (255))")
# my_database_cursor.execute("CREATE TABLE user_preference(ID int AUTO_INCREMENT PRIMARY KEY, Username VARCHAR (255), FOREIGN KEY (Username) REFERENCES user_info (Username), Age TINYINT, Religion VARCHAR (255), Sport VARCHAR (255), Hobby VARCHAR (255), Music VARCHAR (255))")

start_frame = Frame(app, bg="white", height=app.winfo_height(), width=app.winfo_width())
start_frame.place(x=0, y=0)

# Image
login_img = ImageTk.PhotoImage(Image.open("Images/login.jpg"))
login_img_label = Label(start_frame, image=login_img, bg="white")
login_img_label.place(x=100, y=200)

# App name
app_name = Label(start_frame, text="Destine", font=("Edwardian Script ITC", 92, "bold"), bg="white", fg="#fb6d6c", width=8)
app_name.place(x=750, y=100)

# Temp frame for giving border color to app form
temp_frame = Frame(start_frame, bg="#666f80")
temp_frame.place(x=800, y=300)

# Label for app form
login_form_label = Label(temp_frame, width=70, height=24, bd=0, bg="white")
login_form_label.pack(pady=5, padx=5)

# Username label & entry
username_label = Label(login_form_label, text="Username:", fg="#666f80", font=("Proxima Nova", 20), bg="white")
username_label.place(x=30, y=30)
username_entry = Entry(login_form_label, width=18, font=("Proxima Nova", 20), bg="white", bd=0, fg="#666f80")
username_entry.place(x=180, y=30)
underline_frame = Frame(login_form_label, bg="#c3c8d3", height=2, width=273)
underline_frame.place(x=180, y=65)

# Password label & entry
password_label = Label(login_form_label, text="Password:", fg="#666f80", font=("Proxima Nova", 20), bg="white")
password_label.place(x=30, y=100)
password_entry = Entry(login_form_label, width=18, font=("Proxima Nova", 20), show="*", bg="white", bd=0, fg="#666f80")
password_entry.place(x=180, y=100)
underline_frame = Frame(login_form_label, bg="#c3c8d3", height=2, width=273)
underline_frame.place(x=180, y=135)

# Show & Hide Password
show = PhotoImage(file="Images/show.png")
show_button = Button(login_form_label, image=show, bg="white", borderwidth=0, command=show_password)
show_button.place(x=400, y=82)

# App button
login_button = Button(login_form_label, text="Login", bg="#666f80", fg="white", font=("Proxima Nova", 20, "bold"), width=7, command=dashboard)
login_button.place(x=200, y=220)

# Forgot Password Button
forgot_password = Button(login_form_label, text="Forgot Password?", fg="#fb6d6c", bg="white", activebackground="#fb6d6c", activeforeground="white", font=("Proxima Nova", 14), borderwidth=0, command=forgot_password)
forgot_password.place(x=285, y=139)

# Signup form
signup_button_label = Label(login_form_label, text="Don't have an account?", fg="#666f80", bg="white", font=("Proxima Nova", 14))
signup_button_label.place(x=115, y=315)
signup_button = Button(login_form_label, text="Sign Up", fg="#fb6d6c", bg="white", activebackground="#fb6d6c", activeforeground="white", font=("Proxima Nova", 18, "bold", "underline"), borderwidth=0, command=signupform)
signup_button.place(x=315, y=300)

print(app.winfo_height())
print(app.winfo_width())

app.mainloop()
