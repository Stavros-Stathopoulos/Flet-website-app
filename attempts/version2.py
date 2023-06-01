import flet as ft

class webPage:
    def __init__(self, page: ft.Page):
        #self.page = page
        self.driver_func()

    def driver_func(self):
        ft.Column(
            ft.Row(
            [
                ft.Container(
                    ft.Image(src = f"/up_2017_logo_en.png", width=400, height=400, fit=ft.ImageFit.CONTAIN),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    width=300,
                    height=100,
                    border_radius=5,
                ),
                ft.Container(
                    ft.Text("Αναζήτηση στον τηλεφωνικό κατάλογο\n του Πανεπιστημίου Πατρών",size=27, text_align="start", color=ft.colors.BLACK),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    width=700,
                    height=100,
                    border_radius=10,
                ),
                ft.Container(
                    
                    mode = ft.Switch(label="Dark Mode", on_change=self.theme),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    width=300,
                    height=100,
                    border_radius=10,
                ),

            ]
            ),
            spacing=10,
            height=200,
            width=float("inf"),
            scroll=ft.ScrollMode.ALWAYS,
            
        )
    def theme(self, e):
        self.theme_mode = (ft.ThemeMode.DARK 
                           if self.theme_mode == ft.ThemeMode.LIGHT 
                           else ft.ThemeMode.LIGHT)
        self.dark_mode.label = "Dark Mode" if self.theme_mode == ft.ThemeMode.LIGHT else "Light Mode"
        self.update()

if __name__ == "__main__":
    def main(page: ft.Page):
        page.title = "Τηλεφωνικός κατάλογος Upatras"
        page.padding = 0
        page.scroll = "HIDDEN"
        page.theme_mode = ft.ThemeMode.LIGHT
        page.bgcolor = ft.colors.WHITE
        page.add(webPage(page)) 
        page.update()
    ft.app(target=main, assets_dir="images")