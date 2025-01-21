import flet as ft

class ProfileView:
    def __init__(self, page: ft.Page, handle_logout):
        self.page = page
        self.handle_logout = handle_logout

    def get_view(self):
        return ft.View(
            route='/profile',
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text("Profile age", size=30, weight=ft.FontWeight.BOLD),
                        ft.Text(
                            "This is the profile page",
                            size=18,
                            weight=ft.FontWeight.W_500,
                        ),
                        ft.ElevatedButton(text="Logout", on_click=self.handle_logout),
                    ],
                )
            ]
        )
