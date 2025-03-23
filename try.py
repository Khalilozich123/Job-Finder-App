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