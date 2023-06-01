import flet as ft
import make_a_request as req


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
            self.name_row.value = "Όνομα: " + self.reply["name"]
            self.name_row.update()
            self.email_row.value = "Email: " + self.reply["email"]
            self.email_row.update()
            self.phone_row.value = "Τηλέφωνο: " + self.reply["phone"]
            self.phone_row.update()
            self.department_row.value = "Τμήμα: " + self.reply["department"]
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

        self.controls.append(ft.Divider(color="black"))
        self.name_row = ft.Text("", size=20, selectable=True)
        self.phone_row = ft.Text("", size=20, selectable=True)
        self.email_row = ft.Text("", size=20, selectable=True)
        self.department_row = ft.Text("", size=20, selectable=True)

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
