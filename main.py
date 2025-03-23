from tkinter import *
from tkinter import messagebox
import ast
import webbrowser

root = Tk()
root.title('Job Finder')
root.geometry('925x500+300+200')
root.config(bg='#fff')
root.resizable(False, False)


# this function compare the Entry of the user and the database
def sign_in():

    username = user.get()
    code = password.get()
    file = open('user data.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    if username in r.keys() and code == r[username]:
        # This functions create banking finance window

        def BF():

            
            Banking_Finance = Tk()
            Banking_Finance.title("Banking Finance")
            Banking_Finance.config(bg='#F1F1F1')
            Banking_Finance.geometry('925x500+300+200')
            Banking_Finance.resizable(False, False)
            def home():
                Banking_Finance.destroy()
                
            job = []
            camp = []
            experience = []
            location = []
            Skills = []
            link = []

            global j, job1, camp1, experience1, skills1, job2, camp2, experience2, skills2, button1, button2

            with open('BF Data.txt', 'r') as file:
                i = 0
                while i < 100:
                    job.append(file.readline())
                    camp.append(file.readline())
                    experience.append(file.readline())
                    location.append(file.readline())
                    Skills.append(file.readline())
                    link.append(file.readline())
                    file.readline()
                    i = i + 1
            j = 0

            # this function change the content of the page (it load the previous content)
            def back():
                global j
                j = j - 2
                job1.config(text=job[j])
                camp1.config(text=camp[j])
                experience1.config(text=experience[j])
                skills1.config(text=Skills[j])
                button1.config(command=lambda: webbrowser.open(link[j]))

                job2.config(text=job[j + 1])
                camp2.config(text=camp[j + 1])
                experience2.config(text=experience[j + 1])
                skills2.config(text=Skills[j + 1])
                button2.config(command=lambda: webbrowser.open(link[j + 1]))

            # this function change the content of the page (it load the next content)
            def next_page():
                global j
                global job1, camp1, experience1, skills1, job2, camp2, experience2, skills2, button1, button2
                j = j + 2
                if j != 0:
                    button = Button(Banking_Finance, bg='light grey', text='Previous Page', command=back)
                    button.place(x=10, y=470)

                job1.config(text=job[j])
                camp1.config(text=camp[j])
                experience1.config(text=experience[j])
                skills1.config(text=Skills[j])
                button1.config(command=lambda: webbrowser.open(link[j]))

                job2.config(text=job[j + 1])
                camp2.config(text=camp[j + 1])
                experience2.config(text=experience[j + 1])
                skills2.config(text=Skills[j + 1])
                button2.config(command=lambda: webbrowser.open(link[j + 1]))

            Frame(Banking_Finance, width=915, height=220, bg='black').place(x=5, y=5)
            Frame(Banking_Finance, width=915, height=220, bg='black').place(x=5, y=240)
            Frame(Banking_Finance, width=911, height=216, bg='#F1F1F1').place(x=7, y=7)
            Frame(Banking_Finance, width=911, height=216, bg='#F1F1F1').place(x=7, y=242)

            Label(Banking_Finance, text='Job name :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10, y=10)
            job1 = Label(Banking_Finance, text=job[0], bg='#F1F1F1', font=('Calibri(body)', 10))
            job1.place(x=90, y=10)

            Label(Banking_Finance, text='Company name :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10, y=50)
            camp1 = Label(Banking_Finance, text=camp[0], bg='#F1F1F1', font=('Calibri(body)', 10))
            camp1.place(x=125, y=50)

            Label(Banking_Finance, text='Experience required :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10,
                                                                                                                  y=90)
            experience1 = Label(Banking_Finance, text=experience[0], bg='#F1F1F1', font=('Calibri(body)', 10))
            experience1.place(x=155, y=90)

            Label(Banking_Finance, text='Skills required :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10,
                                                                                                              y=130)
            skills1 = Label(Banking_Finance, text=Skills[0], bg='#F1F1F1', font=('Calibri(body)', 10))
            skills1.place(x=120, y=130)

            button1 = Button(Banking_Finance, text='More info', font=('Calibri(body)', 10),
                             command=lambda: webbrowser.open(link[0]))
            button1.place(x=850, y=194)

            Label(Banking_Finance, text='Job name :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10, y=249)
            job2 = Label(Banking_Finance, text=job[1], bg='#F1F1F1', font=('Calibri(body)', 10))
            job2.place(x=90, y=249)

            Label(Banking_Finance, text='Company name :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10, y=289)
            camp2 = Label(Banking_Finance, text=camp[1], bg='#F1F1F1', font=('Calibri(body)', 10))
            camp2.place(x=125, y=289)

            Label(Banking_Finance, text='Experience required :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10,
                                                                                                                  y=329)
            experience2 = Label(Banking_Finance, text=experience[1], bg='#F1F1F1', font=('Calibri(body)', 10))
            experience2.place(x=155, y=329)

            Label(Banking_Finance, text='Skills required :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10,
                                                                                                              y=369)
            skills2 = Label(Banking_Finance, text=Skills[1], bg='#F1F1F1', font=('Calibri(body)', 10))
            skills2.place(x=120, y=369)

            button2 = Button(Banking_Finance, text='More info', command=lambda: webbrowser.open(link[1]))
            button2.place(x=850, y=430)

            Next_page = Button(Banking_Finance, text='Next Page', bg='light grey', command=next_page)
            Next_page.place(x=850, y=470)

            Main_menu = Button(Banking_Finance, text='Home',command=home, bg='light grey')
            Main_menu.place(x=425, y=470)

            Banking_Finance.mainloop()

        def IT():
            Information_Technology = Tk()
            Information_Technology.title("Information Technology")
            Information_Technology.config(bg='#F1F1F1')
            Information_Technology.geometry('925x500+300+200')
            Information_Technology.resizable(False, False)
            def home():
                Information_Technology.destroy()
            job = []
            camp = []
            experience = []
            location = []
            Skills = []
            link = []

            global j, job1, camp1, experience1, skills1, job2, camp2, experience2, skills2, button1, button2

            with open('It Data.txt', 'r') as file:
                i = 0
                while i < 100:
                    job.append(file.readline())
                    camp.append(file.readline())
                    experience.append(file.readline())
                    location.append(file.readline())
                    Skills.append(file.readline())
                    link.append(file.readline())
                    file.readline()
                    i = i + 1
            j = 0

            # this function change the content of the page (it load the previous content)
            def back():
                global j
                j = j - 2
                job1.config(text=job[j])
                camp1.config(text=camp[j])
                experience1.config(text=experience[j])
                skills1.config(text=Skills[j])
                button1.config(command=lambda: webbrowser.open(link[j]))

                job2.config(text=job[j + 1])
                camp2.config(text=camp[j + 1])
                experience2.config(text=experience[j + 1])
                skills2.config(text=Skills[j + 1])
                button2.config(command=lambda: webbrowser.open(link[j + 1]))

            # this function change the content of the page (it load the next content)
            def next_page():
                global j
                global job1, camp1, experience1, skills1, job2, camp2, experience2, skills2, button1, button2
                j = j + 2
                if j != 0:
                    button = Button(Information_Technology, bg='light grey', text='Previous Page', command=back)
                    button.place(x=10, y=470)

                job1.config(text=job[j])
                camp1.config(text=camp[j])
                experience1.config(text=experience[j])
                skills1.config(text=Skills[j])
                button1.config(command=lambda: webbrowser.open(link[j]))

                job2.config(text=job[j + 1])
                camp2.config(text=camp[j + 1])
                experience2.config(text=experience[j + 1])
                skills2.config(text=Skills[j + 1])
                button2.config(command=lambda: webbrowser.open(link[j + 1]))

            Frame(Information_Technology, width=915, height=220, bg='black').place(x=5, y=5)
            Frame(Information_Technology, width=915, height=220, bg='black').place(x=5, y=240)
            Frame(Information_Technology, width=911, height=216, bg='#F1F1F1').place(x=7, y=7)
            Frame(Information_Technology, width=911, height=216, bg='#F1F1F1').place(x=7, y=242)

            Label(Information_Technology, text='Job name :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10, y=10)
            job1 = Label(Information_Technology, text=job[0], bg='#F1F1F1', font=('Calibri(body)', 10))
            job1.place(x=90, y=10)

            Label(Information_Technology, text='Company name :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10, y=50)
            camp1 = Label(Information_Technology, text=camp[0], bg='#F1F1F1', font=('Calibri(body)', 10))
            camp1.place(x=125, y=50)

            Label(Information_Technology, text='Experience required :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10,
                                                                                                                  y=90)
            experience1 = Label(Information_Technology, text=experience[0], bg='#F1F1F1', font=('Calibri(body)', 10))
            experience1.place(x=155, y=90)

            Label(Information_Technology, text='Skills required :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10,
                                                                                                              y=130)
            skills1 = Label(Information_Technology, text=Skills[0], bg='#F1F1F1', font=('Calibri(body)', 10))
            skills1.place(x=120, y=130)

            button1 = Button(Information_Technology, text='More info', font=('Calibri(body)', 10),
                             command=lambda: webbrowser.open(link[0]))
            button1.place(x=850, y=194)

            Label(Information_Technology, text='Job name :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10, y=249)
            job2 = Label(Information_Technology, text=job[1], bg='#F1F1F1', font=('Calibri(body)', 10))
            job2.place(x=90, y=249)

            Label(Information_Technology, text='Company name :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10, y=289)
            camp2 = Label(Information_Technology, text=camp[1], bg='#F1F1F1', font=('Calibri(body)', 10))
            camp2.place(x=125, y=289)

            Label(Information_Technology, text='Experience required :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10,
                                                                                                                  y=329)
            experience2 = Label(Information_Technology, text=experience[1], bg='#F1F1F1', font=('Calibri(body)', 10))
            experience2.place(x=155, y=329)

            Label(Information_Technology, text='Skills required :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10,
                                                                                                              y=369)
            skills2 = Label(Information_Technology, text=Skills[1], bg='#F1F1F1', font=('Calibri(body)', 10))
            skills2.place(x=120, y=369)

            button2 = Button(Information_Technology, text='More info', command=lambda: webbrowser.open(link[1]))
            button2.place(x=850, y=430)

            Button(Information_Technology, text='Next Page', bg='light grey', command=next_page).place(x=850, y=470)
            
            Main_menu = Button(Information_Technology, text='Home',command=home, bg='light grey')
            Main_menu.place(x=425, y=470)
            Information_Technology.mainloop()

        def ME():
            
            Manufacturing_Engineering = Tk()
            Manufacturing_Engineering.title("Manufacturing Engineering")
            Manufacturing_Engineering.config(bg='#F1F1F1')
            Manufacturing_Engineering.geometry('925x500+300+200')
            Manufacturing_Engineering.resizable(False, False)
            def home():
                Manufacturing_Engineering.destroy()
            job = []
            camp = []
            experience = []
            location = []
            Skills = []
            link = []

            global j, job1, camp1, experience1, skills1, job2, camp2, experience2, skills2, button1, button2

            with open('ME Data.txt', 'r') as file:
                i = 0
                while i < 100:
                    job.append(file.readline())
                    camp.append(file.readline())
                    experience.append(file.readline())
                    location.append(file.readline())
                    Skills.append(file.readline())
                    link.append(file.readline())
                    file.readline()
                    i = i + 1
            j = 0

            # this function change the content of the page (it load the previous content)
            def back():
                global j
                j = j - 2
                job1.config(text=job[j])
                camp1.config(text=camp[j])
                experience1.config(text=experience[j])
                skills1.config(text=Skills[j])
                button1.config(command=lambda: webbrowser.open(link[j]))

                job2.config(text=job[j + 1])
                camp2.config(text=camp[j + 1])
                experience2.config(text=experience[j + 1])
                skills2.config(text=Skills[j + 1])
                button2.config(command=lambda: webbrowser.open(link[j + 1]))

            # this function change the content of the page (it load the next content)
            def next_page():
                global j
                global job1, camp1, experience1, skills1, job2, camp2, experience2, skills2, button1, button2
                j = j + 2
                if j != 0:
                    button = Button(Manufacturing_Engineering, bg='light grey', text='Previous Page', command=back)
                    button.place(x=10, y=470)

                job1.config(text=job[j])
                camp1.config(text=camp[j])
                experience1.config(text=experience[j])
                skills1.config(text=Skills[j])
                button1.config(command=lambda: webbrowser.open(link[j]))

                job2.config(text=job[j + 1])
                camp2.config(text=camp[j + 1])
                experience2.config(text=experience[j + 1])
                skills2.config(text=Skills[j + 1])
                button2.config(command=lambda: webbrowser.open(link[j + 1]))

            Frame(Manufacturing_Engineering, width=915, height=220, bg='black').place(x=5, y=5)
            Frame(Manufacturing_Engineering, width=915, height=220, bg='black').place(x=5, y=240)
            Frame(Manufacturing_Engineering, width=911, height=216, bg='#F1F1F1').place(x=7, y=7)
            Frame(Manufacturing_Engineering, width=911, height=216, bg='#F1F1F1').place(x=7, y=242)

            Label(Manufacturing_Engineering, text='Job name :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10, y=10)
            job1 = Label(Manufacturing_Engineering, text=job[0], bg='#F1F1F1', font=('Calibri(body)', 10))
            job1.place(x=90, y=10)

            Label(Manufacturing_Engineering, text='Company name :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10, y=50)
            camp1 = Label(Manufacturing_Engineering, text=camp[0], bg='#F1F1F1', font=('Calibri(body)', 10))
            camp1.place(x=125, y=50)

            Label(Manufacturing_Engineering, text='Experience required :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10,
                                                                                                                  y=90)
            experience1 = Label(Manufacturing_Engineering, text=experience[0], bg='#F1F1F1', font=('Calibri(body)', 10))
            experience1.place(x=155, y=90)

            Label(Manufacturing_Engineering, text='Skills required :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10,
                                                                                                              y=130)
            skills1 = Label(Manufacturing_Engineering, text=Skills[0], bg='#F1F1F1', font=('Calibri(body)', 10))
            skills1.place(x=120, y=130)

            button1 = Button(Manufacturing_Engineering, text='More info', font=('Calibri(body)', 10),
                             command=lambda: webbrowser.open(link[0]))
            button1.place(x=850, y=194)

            Label(Manufacturing_Engineering, text='Job name :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10, y=249)
            job2 = Label(Manufacturing_Engineering, text=job[1], bg='#F1F1F1', font=('Calibri(body)', 10))
            job2.place(x=90, y=249)

            Label(Manufacturing_Engineering, text='Company name :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10, y=289)
            camp2 = Label(Manufacturing_Engineering, text=camp[1], bg='#F1F1F1', font=('Calibri(body)', 10))
            camp2.place(x=125, y=289)

            Label(Manufacturing_Engineering, text='Experience required :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10,
                                                                                                                  y=329)
            experience2 = Label(Manufacturing_Engineering, text=experience[1], bg='#F1F1F1', font=('Calibri(body)', 10))
            experience2.place(x=155, y=329)

            Label(Manufacturing_Engineering, text='Skills required :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10,
                                                                                                              y=369)
            skills2 = Label(Manufacturing_Engineering, text=Skills[1], bg='#F1F1F1', font=('Calibri(body)', 10))
            skills2.place(x=120, y=369)

            button2 = Button(Manufacturing_Engineering, text='More info', command=lambda: webbrowser.open(link[1]))
            button2.place(x=850, y=430)

            Button(Manufacturing_Engineering, text='Next Page', bg='light grey', command=next_page).place(x=850, y=470)
            
            Main_menu = Button(Manufacturing_Engineering, text='Home',command=home, bg='light grey')
            Main_menu.place(x=425, y=470)
            Manufacturing_Engineering.mainloop()

        def SOB():
            
            SCM_Operations_BPO = Tk()
            SCM_Operations_BPO.title("SCM & Operations BPO")
            SCM_Operations_BPO.config(bg='#F1F1F1')
            SCM_Operations_BPO.geometry('925x500+300+200')
            SCM_Operations_BPO.resizable(False, False)
            def home():
                SCM_Operations_BPO.destroy()
            job = []
            camp = []
            experience = []
            location = []
            Skills = []
            link = []

            global j, job1, camp1, experience1, skills1, job2, camp2, experience2, skills2, button1, button2

            with open('SOB Data.txt', 'r') as file:
                i = 0
                while i < 100:
                    job.append(file.readline())
                    camp.append(file.readline())
                    experience.append(file.readline())
                    location.append(file.readline())
                    Skills.append(file.readline())
                    link.append(file.readline())
                    file.readline()
                    i = i + 1
            j = 0

            # this function change the content of the page (it load the previous content)
            def back():
                global j
                j = j - 2
                job1.config(text=job[j])
                camp1.config(text=camp[j])
                experience1.config(text=experience[j])
                skills1.config(text=Skills[j])
                button1.config(command=lambda: webbrowser.open(link[j]))

                job2.config(text=job[j + 1])
                camp2.config(text=camp[j + 1])
                experience2.config(text=experience[j + 1])
                skills2.config(text=Skills[j + 1])
                button2.config(command=lambda: webbrowser.open(link[j + 1]))

            # this function change the content of the page (it load the next content)
            def next_page():
                global j
                global job1, camp1, experience1, skills1, job2, camp2, experience2, skills2, button1, button2
                j = j + 2
                if j != 0:
                    button = Button(SCM_Operations_BPO, bg='light grey', text='Previous Page', command=back)
                    button.place(x=10, y=470)

                job1.config(text=job[j])
                camp1.config(text=camp[j])
                experience1.config(text=experience[j])
                skills1.config(text=Skills[j])
                button1.config(command=lambda: webbrowser.open(link[j]))

                job2.config(text=job[j + 1])
                camp2.config(text=camp[j + 1])
                experience2.config(text=experience[j + 1])
                skills2.config(text=Skills[j + 1])
                button2.config(command=lambda: webbrowser.open(link[j + 1]))

            Frame(SCM_Operations_BPO, width=915, height=220, bg='black').place(x=5, y=5)
            Frame(SCM_Operations_BPO, width=915, height=220, bg='black').place(x=5, y=240)
            Frame(SCM_Operations_BPO, width=911, height=216, bg='#F1F1F1').place(x=7, y=7)
            Frame(SCM_Operations_BPO, width=911, height=216, bg='#F1F1F1').place(x=7, y=242)

            Label(SCM_Operations_BPO, text='Job name :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10, y=10)
            job1 = Label(SCM_Operations_BPO, text=job[0], bg='#F1F1F1', font=('Calibri(body)', 10))
            job1.place(x=90, y=10)

            Label(SCM_Operations_BPO, text='Company name :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10, y=50)
            camp1 = Label(SCM_Operations_BPO, text=camp[0], bg='#F1F1F1', font=('Calibri(body)', 10))
            camp1.place(x=125, y=50)

            Label(SCM_Operations_BPO, text='Experience required :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10,
                                                                                                                  y=90)
            experience1 = Label(SCM_Operations_BPO, text=experience[0], bg='#F1F1F1', font=('Calibri(body)', 10))
            experience1.place(x=155, y=90)

            Label(SCM_Operations_BPO, text='Skills required :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10,
                                                                                                              y=130)
            skills1 = Label(SCM_Operations_BPO, text=Skills[0], bg='#F1F1F1', font=('Calibri(body)', 10))
            skills1.place(x=120, y=130)

            button1 = Button(SCM_Operations_BPO, text='More info', font=('Calibri(body)', 10),
                             command=lambda: webbrowser.open(link[0]))
            button1.place(x=850, y=194)

            Label(SCM_Operations_BPO, text='Job name :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10, y=249)
            job2 = Label(SCM_Operations_BPO, text=job[1], bg='#F1F1F1', font=('Calibri(body)', 10))
            job2.place(x=90, y=249)

            Label(SCM_Operations_BPO, text='Company name :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10, y=289)
            camp2 = Label(SCM_Operations_BPO, text=camp[1], bg='#F1F1F1', font=('Calibri(body)', 10))
            camp2.place(x=125, y=289)

            Label(SCM_Operations_BPO, text='Experience required :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10,
                                                                                                                  y=329)
            experience2 = Label(SCM_Operations_BPO, text=experience[1], bg='#F1F1F1', font=('Calibri(body)', 10))
            experience2.place(x=155, y=329)

            Label(SCM_Operations_BPO, text='Skills required :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10,
                                                                                                              y=369)
            skills2 = Label(SCM_Operations_BPO, text=Skills[1], bg='#F1F1F1', font=('Calibri(body)', 10))
            skills2.place(x=120, y=369)

            button2 = Button(SCM_Operations_BPO, text='More info', command=lambda: webbrowser.open(link[1]))
            button2.place(x=850, y=430)

            Button(SCM_Operations_BPO, text='Next Page', bg='light grey', command=next_page).place(x=850, y=470)
            
            Main_menu = Button(SCM_Operations_BPO, text='Home',command=home, bg='light grey')
            Main_menu.place(x=425, y=470)
            SCM_Operations_BPO.mainloop()
        def SM():
            Sales_Marketing = Tk()
            Sales_Marketing.title("Sales & Marketing")
            Sales_Marketing.config(bg='#F1F1F1')
            Sales_Marketing.geometry('925x500+300+200')
            Sales_Marketing.resizable(False, False)
            def home():
                Sales_Marketing.destroy()
            job = []
            camp = []
            experience = []
            location = []
            Skills = []
            link = []

            global j, job1, camp1, experience1, skills1, job2, camp2, experience2, skills2, button1, button2

            with open('SM Data.txt', 'r') as file:
                i = 0
                while i < 100:
                    job.append(file.readline())
                    camp.append(file.readline())
                    experience.append(file.readline())
                    location.append(file.readline())
                    Skills.append(file.readline())
                    link.append(file.readline())
                    file.readline()
                    i = i + 1
            j = 0

            # this function change the content of the page (it load the previous content)
            def back():
                global j
                j = j - 2
                job1.config(text=job[j])
                camp1.config(text=camp[j])
                experience1.config(text=experience[j])
                skills1.config(text=Skills[j])
                button1.config(command=lambda: webbrowser.open(link[j]))

                job2.config(text=job[j + 1])
                camp2.config(text=camp[j + 1])
                experience2.config(text=experience[j + 1])
                skills2.config(text=Skills[j + 1])
                button2.config(command=lambda: webbrowser.open(link[j + 1]))

            # this function change the content of the page (it load the next content)
            def next_page():
                global j
                global job1, camp1, experience1, skills1, job2, camp2, experience2, skills2, button1, button2
                j = j + 2
                if j != 0:
                    button = Button(Sales_Marketing, bg='light grey', text='Previous Page', command=back)
                    button.place(x=10, y=470)

                job1.config(text=job[j])
                camp1.config(text=camp[j])
                experience1.config(text=experience[j])
                skills1.config(text=Skills[j])
                button1.config(command=lambda: webbrowser.open(link[j]))

                job2.config(text=job[j + 1])
                camp2.config(text=camp[j + 1])
                experience2.config(text=experience[j + 1])
                skills2.config(text=Skills[j + 1])
                button2.config(command=lambda: webbrowser.open(link[j + 1]))

            Frame(Sales_Marketing, width=915, height=220, bg='black').place(x=5, y=5)
            Frame(Sales_Marketing, width=915, height=220, bg='black').place(x=5, y=240)
            Frame(Sales_Marketing, width=911, height=216, bg='#F1F1F1').place(x=7, y=7)
            Frame(Sales_Marketing, width=911, height=216, bg='#F1F1F1').place(x=7, y=242)

            Label(Sales_Marketing, text='Job name :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10, y=10)
            job1 = Label(Sales_Marketing, text=job[0], bg='#F1F1F1', font=('Calibri(body)', 10))
            job1.place(x=90, y=10)

            Label(Sales_Marketing, text='Company name :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10, y=50)
            camp1 = Label(Sales_Marketing, text=camp[0], bg='#F1F1F1', font=('Calibri(body)', 10))
            camp1.place(x=125, y=50)

            Label(Sales_Marketing, text='Experience required :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10,
                                                                                                                  y=90)
            experience1 = Label(Sales_Marketing, text=experience[0], bg='#F1F1F1', font=('Calibri(body)', 10))
            experience1.place(x=155, y=90)

            Label(Sales_Marketing, text='Skills required :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10,
                                                                                                              y=130)
            skills1 = Label(Sales_Marketing, text=Skills[0], bg='#F1F1F1', font=('Calibri(body)', 10))
            skills1.place(x=120, y=130)

            button1 = Button(Sales_Marketing, text='More info', font=('Calibri(body)', 10),
                             command=lambda: webbrowser.open(link[0]))
            button1.place(x=850, y=194)

            Label(Sales_Marketing, text='Job name :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10, y=249)
            job2 = Label(Sales_Marketing, text=job[1], bg='#F1F1F1', font=('Calibri(body)', 10))
            job2.place(x=90, y=249)

            Label(Sales_Marketing, text='Company name :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10, y=289)
            camp2 = Label(Sales_Marketing, text=camp[1], bg='#F1F1F1', font=('Calibri(body)', 10))
            camp2.place(x=125, y=289)

            Label(Sales_Marketing, text='Experience required :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10,
                                                                                                                  y=329)
            experience2 = Label(Sales_Marketing, text=experience[1], bg='#F1F1F1', font=('Calibri(body)', 10))
            experience2.place(x=155, y=329)

            Label(Sales_Marketing, text='Skills required :', font=('Calibri(body)', 10, 'bold'), fg='dark blue').place(x=10,
                                                                                                              y=369)
            skills2 = Label(Sales_Marketing, text=Skills[1], bg='#F1F1F1', font=('Calibri(body)', 10))
            skills2.place(x=120, y=369)

            button2 = Button(Sales_Marketing, text='More info', command=lambda: webbrowser.open(link[1]))
            button2.place(x=850, y=430)

            Button(Sales_Marketing, text='Next Page', bg='light grey', command=next_page).place(x=850, y=470)
            
            Main_menu = Button(Sales_Marketing, text='Home',command=home, bg='light grey')
            Main_menu.place(x=425, y=470)
            Sales_Marketing.mainloop()

        root.destroy()
        screen = Tk()
        screen.title("Job Finder")
        screen.geometry('925x500+300+200')
        screen.config(bg='white')
        screen.resizable(False, False)
        
        image = PhotoImage(file='background.png')
        Label(screen, image=image, bg="white").place(x=250, y=65)
        Label(screen, text='Welcome To Job Finder', bg='#fff', font=('Calibri(body)', 45, 'bold'),fg="#495261").place(x=105, y=0)



        Button(screen, width=20, pady=7, text='Banking Finance', bg='#DE722D', fg='white', border=0,
               command=BF).place(x=45, y=420)
        Button(screen, width=20, pady=7, text='Information Technology', bg='#DE722D', fg='white', border=0,
               command=IT).place(x=205, y=420)
        Button(screen, width=24, pady=7, text='Manufacturing Engineering', bg='#DE722D', fg='white', border=0,
               command=ME).place(x=365, y=420)
        Button(screen, width=20, pady=7, text='Sales & Marketing', bg='#DE722D', fg='white', border=0,
               command=SM).place(x=555,y=420)
        Button(screen, width=20, pady=7, text='SCM & Operations BPO', bg='#DE722D', fg='white', border=0,
               command=SOB).place(x=715, y=420)

        screen.mainloop()
    else:
        messagebox.showerror('Invalid', 'Invalid username or password')


####################################################################################################################
# this party is for register code 
####################################################################################################################
def sign_command():
    window = Toplevel(root)

    window.title('Job Finder')
    window.geometry('925x500+300+200')
    window.config(bg='#fff')
    window.resizable(False, False)

    def signup():
        username = user.get()
        code = password.get()
        confirm_code = confirm_password.get()
        if code == confirm_code:
            try:
                file = open('user data.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)
                dict2 = {username: code}
                r.update(dict2)
                file.truncate(0)
                file.close

                file = open('user data.txt', 'w')
                w = file.write(str(r))
                messagebox.showinfo('sign up', 'Successfully sign up')
            except:
                file = open('user data.txt', 'w')
                pp = str({'Username': 'Password'})
                file.write(pp)
                file.close()
        else:
            messagebox.showerror('Invalid', 'Both Password should match')

    def sign():
        window.destroy()

    pic = PhotoImage(file='register.png')
    Label(window, image=pic, border=0, bg='white').place(x=50, y=90)

    frame = Frame(window, width=350, height=390, bg='#fff')
    frame.place(x=480, y=50)

    heading = Label(frame, text='sign up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    # ========================================================================================================================
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == "":
            user.insert(0, 'Username')

    user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    # ========================
    def on_enter(e):
        password.delete(0, 'end')

    def on_leave(e):
        name = password.get()
        if name == "":
            password.insert(0, 'password')

    password = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    password.place(x=30, y=150)
    password.insert(0, 'password')
    password.bind('<FocusIn>', on_enter)
    password.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    # ========================
    def on_enter(e):
        confirm_password.delete(0, 'end')

    def on_leave(e):
        name = confirm_password.get()
        if name == "":
            password.insert(0, 'confirm_password')

    confirm_password = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    confirm_password.place(x=30, y=220)
    confirm_password.insert(0, 'password')
    confirm_password.bind('<FocusIn>', on_enter)
    confirm_password.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)
    # ========================================================================================================================
    Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35,
                                                                                                              y=280)
    label = Label(frame, text="I have an account ", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=90, y=340)
    sign_in = Button(frame, width=6, text='sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=sign)
    sign_in.place(x=200, y=340)

    window.mainloop()


####################################################################################################################

image = PhotoImage(file='login.png')
Label(root, image=image, bg="white").place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)


# ========================================================================================================================
def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == "":
        user.insert(0, 'Username')


user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)


# ========================
def on_enter(e):
    password.delete(0, 'end')


def on_leave(e):
    name = password.get()
    if name == "":
        password.insert(0, 'password')


password = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
password.place(x=30, y=150)
password.insert(0, 'password')
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)
# ========================================================================================================================
Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=sign_in).place(x=35, y=204)
label = Label(frame, text="Don't have an account ?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)
sign_up = Button(frame, width=6, text='sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8',
                 command=sign_command)
sign_up.place(x=215, y=270)

root.mainloop()
