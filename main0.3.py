import flet as ft
import make_a_request as req


def main(page: ft.Page):
    def createTextinput(label, hint_text, on_submit):
        return ft.TextField(label=label,
                            width=300,
                            height=50,
                            hint_text=hint_text,
                            on_submit=on_submit)

    def createButton(icon, on_click, data):
        return ft.IconButton(icon=icon,
                             on_click=on_click,
                             data=data)

    def createText(text, size, font, selectable):
        return ft.Text(text, size=size, font_family=font, selectable=selectable)

    def theme_changed(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        dark_mode.icon = (
            ft.icons.MODE_NIGHT_OUTLINED if page.theme_mode == ft.ThemeMode.LIGHT else ft.icons.LIGHT_MODE_OUTLINED
        )
        page.bgcolor = "#eeeeee" if page.theme_mode == ft.ThemeMode.LIGHT else "#222222"
        page.update()

    def search_name(e):

        if nameBox.value == "":
            return

        result = req.makeRequest(fname=nameBox.value)
        print(result)
        if result["results"] is False:
            answear = ft.Text("Δε βρέθηκαν εγγραφές.", size=20, selectable=True)
            page.add(space, answear)
            return

        else:
            answer = ft.Text("Αποτελέσματα αναζήτησης:\n Όνομα: {}\n Τηλέφωνο: {}\n Email: {}".format(result["name"],
                                                                                                      result["phone"],
                                                                                                      result["email"]),
                             size=20, selectable=True, color="#222222" if page.theme_mode == ft.ThemeMode.LIGHT else "#eeeeee")
            page.add(
                ft.Container(
                    content=answer,
                    width=500,
                    height=200,
                    bgcolor=page.bgcolor,
                    padding=10,
                    margin=10,
                )
            )
            page.update()
            print("search_name", nameBox.value, result)

    def search_email(e):
        if emailBox.value == "":
            return
        result = req.makeRequest(email=emailBox.value)
        answer = ft.Text(
            "Αποτελέσματα αναζήτησης:\n Όνομα: {}\n Τηλέφωνο: {}\n Email: {}".format(result["name"], result["phone"],
                                                                                     result["Email"]), size=23,
            selectable=True)
        page.add(space, answer)
        page.update()
        print("search_email", emailBox.value, result)

    def search_phone(e):
        if phoneBox.value == "":
            return
        result = req.makeRequest(phone=phoneBox.value)
        answer = ft.Text(
            "Αποτελέσματα αναζήτησης:\n Όνομα: {}\n Τηλέφωνο: {}\n Email: {}".format(result["name"], result["phone"],
                                                                                     result["Email"]), size=23,
            selectable=True)
        page.add(space, answer)
        page.update()
        print("search_phone", phoneBox.value, result)

    def launch_ece_site(e):
        page.launch_url(url="https://www.ece.upatras.gr/", web_popup_window=False, web_window_name="_blank")

    def launch_up_site(e):
        page.launch_url(url="https://www.upatras.gr/", web_popup_window=False, web_window_name="_blank")

    def launch_contact_site(e):
        page.launch_url(url="https://www.upatras.gr/contact/", web_popup_window=False, web_window_name="_blank")

    page.selectable = True
    page.title = "Τηλεφωνικός κατάλογος Upatras"
    page.padding = 0
    page.scroll = "HIDDEN"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#eeeeee"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {
        "Times-New-Roman": "/fonts/Times-New-Roman.ttf",
    }
    nameBox = createTextinput(label="Όνομα", hint_text="Όνομα", on_submit=search_name)
    emailBox = createTextinput(label="Email", hint_text="Email", on_submit=search_email)
    phoneBox = createTextinput(label="Τηλέφωνο", hint_text="Τηλέφωνο", on_submit=search_phone)

    searchButtonName = createButton(icon=ft.icons.SEARCH_SHARP, on_click=search_name, data=0)
    searchButtonEmail = createButton(icon=ft.icons.SEARCH_SHARP, on_click=search_email, data=0)
    searchButtonPhone = createButton(icon=ft.icons.SEARCH_SHARP, on_click=search_phone, data=0)
    dark_mode = createButton(icon=ft.icons.MODE_NIGHT_OUTLINED, on_click=theme_changed, data=0)

    page.appbar = ft.AppBar(leading=ft.PopupMenuButton(icon=ft.icons.HOME,
                                                       items=[
                                                           ft.PopupMenuItem(text="Πανεπιστήμιο Πατρών",
                                                                            on_click=launch_up_site),
                                                           ft.PopupMenuItem(
                                                               text="Τμήμα Ηλεκτρολόγων Μηχανικών \nκαι Τεχνολογίας "
                                                                    "Υπολογοιστών",
                                                               on_click=launch_ece_site),
                                                           ft.PopupMenuItem(text="Επικοινωνία",
                                                                            on_click=launch_contact_site)

                                                       ]),
                            title=ft.Text("Τηλεφωνικός κατάλογος Πανεπιστημίου Πατρών",
                                          color=ft.colors.WHITE),
                            center_title=True,
                            actions=[dark_mode],
                            bgcolor="#8B0000")

    logoimage = ft.Image(
        src=f"/images/up_2017_logo_en.png",
        width=300,
        height=300,
        fit="contain",
    )
    logo = ft.Container(content=logoimage,
                        width=300,
                        height=300,
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        border_radius=10,
                        on_click=launch_up_site,
                        )

    space = ft.Container(margin=10,
                         padding=15,
                         alignment=ft.alignment.center,
                         width=page.width / 3.1,
                         height=50,
                         border_radius=0, )

    welcome = createText(text="Αναζήτηση στον τηλεφωνικό κατάλογο του Πανεπιστημίου Πατρών", size=20,
                         font="Times-New-Roman", selectable=True)
    text = createText(text="Αναζήτηση με όνομα, email ή τηλέφωνο", size=20, font="Times-New-Roman", selectable=True)
    start_row = ft.Row(controls=[logo,
                                 welcome,
                                 ],
                       alignment=ft.MainAxisAlignment.SPACE_AROUND)
    searchNameRow = ft.Row(controls=[space,
                                     nameBox,
                                     searchButtonName, ],
                           alignment=ft.MainAxisAlignment.NONE
                           )
    searchEmailRow = ft.Row(controls=[space,
                                      emailBox,
                                      searchButtonEmail, ],
                            alignment=ft.MainAxisAlignment.NONE)
    searchPhoneRow = ft.Row(controls=[space,
                                      phoneBox,
                                      searchButtonPhone, ],
                            alignment=ft.MainAxisAlignment.NONE)

    first_row = ft.Row(controls=[space,
                                 text, ],
                       alignment=ft.MainAxisAlignment.START)

    '''page.add(
             start_row,
             first_row, 
              searchNameRow,
             searchEmailRow, 
             searchPhoneRow, 
             snack,)
'''

    page.on_resize = lambda e: page.update()
    page.add(
        ft.ResponsiveRow(
            [
                start_row
            ],
        ),
        ft.ResponsiveRow(
            [
                first_row
            ],
            run_spacing={"xs": 10},
        ),
        ft.ResponsiveRow(
            controls=[
                searchNameRow,

            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        ft.ResponsiveRow(
            [
                searchEmailRow,
            ],
        ),
        ft.ResponsiveRow(
            [
                searchPhoneRow
            ],
        ),

    )

    page.MainAxisAlignment = ft.MainAxisAlignment.CENTER


ft.app(target=main,
       assets_dir="assets",
       view=ft.WEB_BROWSER,
       route_url_strategy="hash",
       web_renderer="HTML",
       upload_dir="uploads")
