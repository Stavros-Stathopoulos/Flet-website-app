import flet as ft
import make_a_request as req


class PageHeader(ft.UserControl):
    def __init__(self, controller):
        super().__init__()
        self.dark_mode = None
        self.controller = controller

    def theme_change(self, e):
        self.page.theme_mode = (
            ft.ThemeMode.DARK if self.page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )
        self.dark_mode.icon = (ft.icons.MODE_NIGHT_OUTLINED if self.page.theme_mode == ft.ThemeMode.LIGHT else
                               ft.icons.WB_SUNNY_OUTLINED)
        self.page.bgcolor = "#eeeeee" if self.page.theme_mode == ft.ThemeMode.LIGHT else "#222222"
        self.page.update()

    def build(self):
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
                                              url="https://www.ece.upatras.gr/contact",
                                              web_popup_window=False,
                                              web_window_name="_blank"))
                                  ])
        self.dark_mode = ft.IconButton(icon=ft.icons.MODE_NIGHT_OUTLINED,
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

        return ft.Column(self.controls)


class Requests(ft.UserControl):
    def __init__(self, controller, input_name=None, input_phone=None, input_email=None):
        super().__init__()
        self.email = None
        self.phone = None
        self.name = None
        self.result = None
        self.controller = controller
        self.start()
        self.request(input_name=input_name, input_phone=input_phone, input_email=input_email)

    def start(self):
        self.controller.start_header(None)
        self.controller.startResponse()

    def request(self, input_name=None, input_phone=None, input_email=None):
        if input_name is not None:
            self.name = input_name
            self.result = req.makeRequest(fname=self.name)
        elif input_phone is not None:
            self.phone = input_phone
            self.result = req.makeRequest(phone_input=self.phone)
        elif input_email is not None:
            self.email = input_email
            self.result = req.makeRequest(email=self.email)
        else:
            return {"results": "False", "Error": "No input was given"}

    def build(self):
        self.controls = []

        if self.result["results"] is True:
            self.controls.append(ft.Row(controls=[ft.Text(f"Όνομα: {self.result['name']}", size=30, selectable=True)],
                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY))
            self.controls.append(
                ft.Row(controls=[ft.Text(f"Τηλέφωνο: {self.result['phone']}", size=30, selectable=True)],
                       alignment=ft.MainAxisAlignment.SPACE_EVENLY))
            self.controls.append(ft.Row(controls=[ft.Text(f"Email: {self.result['email']}", size=30, selectable=True)],
                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY))
            self.controls.append(
                ft.Row(controls=[ft.Text(f"Τμήμα: {self.result['department']}", size=30, selectable=True)],
                       alignment=ft.MainAxisAlignment.SPACE_EVENLY))
            '''self.controls.append(
                ft.Row([ft.FilledButton("Νέα Αναζήτηση", on_click=self.controller.new_search)]))'''
        else:
            self.controls.append(ft.Text("Δε βρέθηκαν εγγραφές.", size=30, selectable=True))
        return ft.Column(self.controls)


class App(ft.UserControl):
    def __init__(self, controller):
        super().__init__(self)
        self.email_input = None
        self.message = None
        self.phone_input = None
        self.name_input = None
        self.dark_mode = None
        self.controller = controller

    def show_message(self, e, message=""):
        self.message.value = message
        self.message.color = "red"
        self.update()
        return

    def submit_handler(self, e):
        if self.page.controls:
            self.page.controls.pop()
        if self.name_input.value != "":
            self.controls.append(ft.FilledButton("Αναζήτηση",
                                                 on_click=self.page.add(Requests(self,
                                                                                 input_name=self.name_input.value,
                                                                                 input_phone=None,
                                                                                 input_email=None))))
        elif self.phone_input.value != "":
            self.controls.append(ft.FilledButton("Αναζήτηση",
                                                 on_click=self.page.add(Requests(self,
                                                                                 input_phone=self.phone_input.value,
                                                                                 input_email=None,
                                                                                 input_name=None))))
        elif self.email_input.value != "":
            self.controls.append(ft.FilledButton("Αναζήτηση",
                                                 on_click=self.page.add(Requests(self,
                                                                                 input_email=self.email_input.value,
                                                                                 input_name=None,
                                                                                 input_phone=None))))
        else:
            self.show_message(None, message="Παρακαλώ εισάγετε το όνομα, το τηλέφωνο ή το email του υπαλλήλου που "
                                            "αναζητείτε")
            print("error")
            return

    def build(self):
        self.controls = []
        self.controls.append(ft.Divider(color="black"))
        self.controls.append(
            ft.Row(controls=[ft.Text("Εισάγετε το όνομα, το τηλέφωνο ή το email το μέλος που αναζητείτε",
                                     size=15, selectable=True)],
                   alignment=ft.MainAxisAlignment.SPACE_EVENLY))
        self.name_input = ft.TextField(label="Όνομα",
                                       width=300,
                                       height=80,
                                       border=ft.InputBorder.UNDERLINE,
                                       on_submit=self.submit_handler)
        self.controls.append(ft.Row(controls=[self.name_input], alignment=ft.MainAxisAlignment.SPACE_EVENLY))
        self.phone_input = ft.TextField(label="Τηλέφωνο",
                                        width=300,
                                        height=70,
                                        border=ft.InputBorder.UNDERLINE,
                                        on_submit=self.submit_handler)
        self.controls.append(ft.Row(controls=[self.phone_input], alignment=ft.MainAxisAlignment.SPACE_EVENLY))
        self.email_input = ft.TextField(label="Email",
                                        width=300,
                                        height=70,
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

        return ft.Column(self.controls)


class Controller:
    def __init__(self, page):
        self.device = None
        self.page = page
        self.response = {}
        self.searchKey = {}
        self.start_app(None)

    def start_app(self, e):
        if self.page.controls:
            self.page.controls.pop()
        self.page.add(PageHeader(self))
        self.page.add(App(self))

    def driver_func(self, e):
        self.page.add(PageHeader(self))
        self.page.add(App(self))


    def restart(self, e):
        if self.page.controls:
            self.page.controls.pop()
        self.start_app(None)

    def new_search(self, e):
        self.restart(None)


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
