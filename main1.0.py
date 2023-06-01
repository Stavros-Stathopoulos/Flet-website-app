import flet as ft
import make_a_request as req
'''
    file: main1.0.py
    created by: Stavros Stathopoulos
    date: 01/06/2023
    version: 1.0
    place: Patras, Greece
    description:
    
    This is the main file of the application.
    It is responsible for the creation of the application's window and the creation of the application's controls.
    The application's controls are created in the build() method.
    The application's window is created in the main() method.
    the file tools/make_a_request.py is responsible for the communication with the server.
    there are three ways of communication with the server:
        1. by name
        2. by email
        3. by phone number
    the make_a_request file returns a dictionary file with the following structure:
        {
            "status": True/False,
            "name": "name",
            "email": "email",
            "phone": "phone",
            "department": "department"
        }
    if the status is True, then the server found a result.
    if the status is False, then the server did not find a result.
    the name, email, phone and department are the results of the search.
    if the status is False, then the name, email, phone and department are empty.
    the main1.0.py file is responsible for the creation of the application's window and the creation of the application's controls.
    in the main1.0.py file there is a class called App.
    the App class inherits from the UserControl class.
    the UserControl class is a class that is responsible for the creation of the application's controls.
    the UserControl class is located in the flet.py file.
    the UserControl class is responsible for the creation of the application's controls.
    when the app is running in desktop mode, the application's window has minimum width 850px and height 425px.
    these are the minimum dimensions of the application's window,
    because the application is designed to run on a mobile device.
    but the application can run on a desktop device, with bigger screen, so the application's window can be adjusted.
    
    
    the App class has the following methods:
        __init__(self, controller):
            this method is the constructor of the App class.
            the constructor takes one argument, the controller.
            the controller is the object that is responsible for the communication with the server.
            the controller is an object of the Controller class.
        
        showMessage(self, e, message=""):
            this method is responsible for the display of a message.    
            the method takes two arguments:
                e: the event that triggered the method
                message: the message that will be displayed
            the method returns nothing.
            
        showReply(self, e, reply):
            this method is responsible for the display of the results of the search.
            the method takes two arguments:
                e: the event that triggered the method
                reply: the reply of the server
            the method returns nothing.
            
        build(self):
            this method is responsible for the creation of the application's controls.
            the method takes no arguments.
            the method returns a list of the application's controls.
            
        submit_handler(self, e):
            this method is responsible for the submission of the search.
            the method takes one argument:
                e: the event that triggered the method
            the method returns nothing.
        
        theme_change(self, e):
            this method is responsible for the change of the application's theme.
            the method takes one argument:
                e: the event that triggered the method
            the method returns nothing.
            
    the Controller class has the following methods:
        __init__(self):
            this method is the constructor of the Controller class.
            the constructor takes no arguments.
            
        startApp(self):
            this method is responsible for the start of the application.
            the method takes no arguments.
            the method returns nothing.
            
    
    def main():
        this function is responsible for the creation of the application's window.
        the function takes no arguments.
        the function returns nothing.
        
    
    
'''

class App(ft.UserControl):
    def __init__(self, controller):
        super().__init__(self)
        self.reply = {"status": False}
        self.controller = controller

    def showMessage(self, e, message=""):

        self.message.value = message
        self.message.color = "red"
        self.message.update()
        return

    def showReply(self, e, reply):
        if self.reply["results"] is True:
            self.name_row.value = self.reply["name"]
            self.name_row.label = "Όνομα: "
            self.name_row.border = ft.InputBorder.UNDERLINE
            self.name_row.icon = ft.icons.PERSON_SHARP
            self.name_row.update()
            self.email_row.value =self.reply["email"]
            self.email_row.label = "Email: "
            self.email_row.border = ft.InputBorder.UNDERLINE
            self.email_row.icon = ft.icons.EMAIL_SHARP
            self.email_row.update()
            self.phone_row.value =self.reply["phone"]
            self.phone_row.label = "Τηλέφωνο: "
            self.phone_row.border = ft.InputBorder.UNDERLINE
            self.phone_row.icon = ft.icons.PHONE_SHARP
            self.phone_row.update()
            self.department_row.value = self.reply["department"]
            self.department_row.label = "Τμήμα: "
            self.department_row.border = ft.InputBorder.UNDERLINE
            self.department_row.icon = ft.icons.SCHOOL_SHARP
            self.department_row.update()
            self.update()
        else:
            self.showMessage(None, message="Δεν βρέθηκαν αποτελέσματα.")
            self.update()
        return

    def submit_handler(self, e):
        if self.name_input.value != "":
            self.reply = req.makeRequest(fname=self.name_input.value)
            self.name_input.value = ""
            self.showReply(None, self.reply)
            self.update()

        elif self.email_input.value != "":
            self.reply = req.makeRequest(email=self.email_input.value)
            self.email_input.value = ""
            self.showReply(None, self.reply)
            self.update()
        elif self.phone_input.value != "":
            self.reply = req.makeRequest(phone_input=self.phone_input.value)
            self.phone_input.value = ""
            self.showReply(None, self.reply)
            self.update()
        else:
            self.showMessage(None, message="Δεν δώσατε κάποιο όνομα, email ή τηλέφωνο.")
            return

    def theme_change(self, e):
        self.page.theme_mode = (
            ft.ThemeMode.DARK if self.page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )
        self.dark_mode.icon = (ft.icons.MODE_NIGHT_OUTLINED if self.page.theme_mode == ft.ThemeMode.LIGHT else
                               ft.icons.WB_SUNNY_OUTLINED)
        self.dark_mode.icon_color = ft.colors.BLACK if self.page.theme_mode == ft.ThemeMode.LIGHT else ft.colors.WHITE
        self.page.bgcolor = "#eeeeee" if self.page.theme_mode == ft.ThemeMode.LIGHT else "#222222"
        self.dark_mode.update()
        self.page.update()
        return

    def build(self):
        self.controls = []
        menu = ft.PopupMenuButton(icon=ft.icons.HOME,
                                  items=[

                                      ft.PopupMenuItem(
                                          text="Πανεπιστήμιο Πατρών",
                                          on_click=lambda e: self.page.launch_url(
                                              url="https://www.upatras.gr/en",
                                              web_popup_window=False,
                                              web_window_name="_blank")),
                                      ft.PopupMenuItem(
                                          text="Τμήμα Ηλεκτρολόγων Μηχανικών \nκαι Τεχνολογίας Υπολογιστών",
                                          on_click=lambda e: self.page.launch_url(
                                              url="https://www.ece.upatras.gr/",
                                              web_popup_window=False,
                                              web_window_name="_blank")),
                                      ft.PopupMenuItem(
                                          text="Επικοινωνία",
                                          on_click=lambda e: self.page.launch_url(
                                              url="https://www.upatras.gr/contact",
                                              web_popup_window=False,
                                              web_window_name="_blank"))
                                  ])
        self.dark_mode = ft.IconButton(icon=ft.icons.MODE_NIGHT_OUTLINED,
                                       icon_color=ft.colors.BLACK,
                                       on_click=self.theme_change)
        self.controls.append(ft.Container(content=ft.Row(
            controls=[
                ft.Container(content=menu, width=50, height=50),
                ft.Text("   Αναζήτηση Μέλους του Πανεπιστημίου Πατρών", size=20),
                ft.Container(content=self.dark_mode, width=50, height=50)],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY), bgcolor="#8B0000"))

        self.controls.append(ft.Row(controls=[ft.Container(
            content=ft.Image(src=f"/images/up_2017_logo_en.png", width=300, height=300, fit=ft.ImageFit.CONTAIN),
            width=300,
            height=140,
            margin=0,
            padding=0,
            alignment=ft.alignment.center,
            on_click=lambda e: self.page.launch_url(url="https://www.upatras.gr/en", web_popup_window=False,
                                                    web_window_name="_blank")
        )], alignment=ft.MainAxisAlignment.SPACE_EVENLY))
        self.controls.append(ft.Row(controls=[ft.Text("Αναζήτηση στον τηλεφωνικό κατάλογο του Πανεπιστημίου Πατρών",
                                                      size=25, selectable=True)],
                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY))

        self.controls.append(ft.Divider(color="black"))
        self.controls.append(
            ft.Row(controls=[ft.Text("Εισάγετε το όνομα, το τηλέφωνο ή το email το μέλος που αναζητείτε",
                                     size=15, selectable=True)],
                   alignment=ft.MainAxisAlignment.SPACE_EVENLY))
        self.name_input = ft.TextField(label="Όνομα",
                                       width=300,
                                       height=80,
                                       icon=ft.icons.PERSON_SHARP,
                                       border=ft.InputBorder.UNDERLINE,
                                       on_submit=self.submit_handler)
        self.controls.append(ft.Row(controls=[self.name_input], alignment=ft.MainAxisAlignment.SPACE_EVENLY))
        self.phone_input = ft.TextField(label="Τηλέφωνο",
                                        width=300,
                                        height=70,
                                        icon=ft.icons.PHONE_SHARP,
                                        border=ft.InputBorder.UNDERLINE,
                                        on_submit=self.submit_handler)
        self.controls.append(ft.Row(controls=[self.phone_input], alignment=ft.MainAxisAlignment.SPACE_EVENLY))
        self.email_input = ft.TextField(label="Email",
                                        width=300,
                                        height=70,
                                        icon=ft.icons.MAIL_SHARP,
                                        border=ft.InputBorder.UNDERLINE,
                                        on_submit=self.submit_handler)
        self.controls.append(ft.Row(controls=[self.email_input], alignment=ft.MainAxisAlignment.SPACE_EVENLY))
        self.message = ft.Text("")
        self.controls.append(ft.Row(controls=[self.message], alignment=ft.MainAxisAlignment.SPACE_EVENLY))

        self.controls.append(ft.Row(controls=[ft.ElevatedButton(icon=ft.icons.SEARCH_SHARP,
                                                                text="Αναζήτηση",
                                                                width=200,
                                                                height=50,
                                                                bgcolor="#8B0000",
                                                                icon_color="#eeeeee",
                                                                color="#eeeeee",
                                                                on_click=self.submit_handler)],
                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY))

        self.controls.append(ft.Divider(color="black"))
        self.name_row = ft.TextField(label="", border=ft.InputBorder.NONE, read_only=True)
        self.phone_row = ft.TextField(label="", border=ft.InputBorder.NONE, read_only=True)
        self.email_row = ft.TextField(label="", border=ft.InputBorder.NONE, read_only=True)
        self.department_row = ft.TextField(label="", border=ft.InputBorder.NONE, read_only=True, multiline=True)

        self.controls.append(ft.Row(controls=[self.name_row], alignment=ft.MainAxisAlignment.SPACE_EVENLY))
        self.controls.append(ft.Row(controls=[self.phone_row], alignment=ft.MainAxisAlignment.SPACE_EVENLY))
        self.controls.append(ft.Row(controls=[self.email_row], alignment=ft.MainAxisAlignment.SPACE_EVENLY))
        self.controls.append(ft.Row(controls=[self.department_row], alignment=ft.MainAxisAlignment.SPACE_EVENLY))

        return ft.Column(self.controls)


class Controller:
    def __init__(self, page):
        self.page = page
        self.startApp()

    def startApp(self):
        if self.page.controls:
            self.page.controls.clear()
        self.page.add(App(self))


def main(page: ft.Page):
    page.title = "Τηλεφωνικός κατάλογος Πανεπιστημίου Πατρών"
    page.window_min_height = 850
    page.window_min_width = 425
    page.theme_mode = ft.ThemeMode.LIGHT
    page.selectable = True
    page.scroll = "HIDDEN"
    page.bgcolor = "#eeeeee" if page.theme_mode == ft.ThemeMode.LIGHT else "#222222"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.SPACE_EVENLY
    page.padding = 1

    Controller(page)


ft.app(target=main,
       assets_dir="assets",
       view=ft.WEB_BROWSER,
       route_url_strategy="hash")
