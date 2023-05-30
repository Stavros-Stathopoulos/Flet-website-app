import flet as ft


if __name__ == "__main__":
    def main(page: ft.Page):
        
        page.title = "Τηλεφωνικός κατάλογος Upatras"
        page.padding = 0
        page.scroll = "HIDDEN"
        page.theme_mode = ft.ThemeMode.LIGHT
        page.bgcolor = ft.colors.WHITE
        appbar_items = [
            ft.PopupMenuItem(text ="Ελληνικά"),
            ft.PopupMenuItem(text ="English"),
            ft.PopupMenuItem(text ="Πανεπιστήμιο Πατρών"),]
        appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.LOCAL_PHONE_ROUNDED),
            leading_width=100,
            title=ft.Text("Τηλεφωνικός κατάλογος Πανεπιστημίου Πατρών",size=32, text_align="start", color=ft.colors.WHITE),
            center_title=True,
            actions=[
                ft.Container(
                    content=ft.PopupMenuButton(
                        items = appbar_items
                    ),
                    margin=ft.margin.only(left=50, right=25)
                )
            ],
            toolbar_height=65,
            
            bgcolor="#7F0F0F",
        )
        page.add(appbar)
        page.add(
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
                    
                    ft.Switch(label="Dark Mode"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    width=300,
                    height=100,
                    border_radius=10,
                ),

            
                ],
                alignment=ft.MainAxisAlignment.CENTER,   
        )
        )

        txt_name = ft.TextField(label="Όνομα", border=ft.InputBorder.NONE, filled=True, hint_text= "Όνομα")
        txt_phone = ft.TextField(label="Τηλέφωνο", border=ft.InputBorder.NONE, filled=True, hint_text= "Τηλέφωνο")
        txt_email = ft.TextField(label="Email", border=ft.InputBorder.NONE, filled=True, hint_text= "Email", color="#3E4E50",)
        print(txt_name)
        print(txt_phone)
        print(txt_email)
        btn_submit = ft.ElevatedButton(text="Submit")
        page.add(txt_name,txt_email, txt_phone,  btn_submit)
       
    ft.app(target=main, view=ft.WEB_BROWSER, assets_dir="images")
