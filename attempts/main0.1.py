import flet as ft
def main(page: ft.Page):
    def theme(e):
        page.theme_mode = (ft.ThemeMode.DARK 
                           if page.theme_mode == ft.ThemeMode.LIGHT 
                           else ft.ThemeMode.LIGHT)
        dark_mode.label = "Dark Mode" if page.theme_mode == ft.ThemeMode.LIGHT else "Light Mode"
        page.update()
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll="HIDDEN"
    page.appbar = ft.AppBar(
        ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
        toolbar_height= 60,
        #bgcolor="#GREY",
        
        )
    img = ft.Image(src = f"/up_2017_logo_en.png", width=400, height=400, fit=ft.ImageFit.CONTAIN)
    page.add(img)

    page.title = "Τηλεφωνικός κατάλογος Upatras"
    dark_mode = ft.Switch(label="Dark Mode",on_change=theme )
    page.add(dark_mode)

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.add(ft.Text("Τηλεφωνικός κατάλογος Upatras"))
    txt_name = ft.TextField(label="Όνομα", border=ft.InputBorder.NONE, filled=True, hint_text= "Όνομα")

    txt_phone = ft.TextField(label="Τηλέφωνο", border=ft.InputBorder.NONE, filled=True, hint_text= "Τηλέφωνο")

    txt_email = ft.TextField(label="Email", border=ft.InputBorder.NONE, filled=True, hint_text= "Email")

    btn_submit = ft.ElevatedButton(text="Submit")
    page.add(txt_name,txt_email, txt_phone,  btn_submit)

ft.app(target=main, assets_dir="images")