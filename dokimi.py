import flet as ft
import make_a_request as req

class Result(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.controller = controller

class Controller:
    def __init__(self, page):
        self.device = None
        self.page = page
        self.start_app(None)

    def start_app(self, e):
        if self.page.controls:
            self.page.controls.pop()
        self.page.add(PageHeader(self))
        self.page.add(App(self))

    def startResponse(self):
        if self.page.controls:
            self.page.controls.pop()
        self.page.add(PageHeader(self))
        self.page.add(Requests(self))

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
