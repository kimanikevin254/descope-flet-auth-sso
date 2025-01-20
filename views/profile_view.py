import flet as ft

class ProfileView:
    def __init__(self, page: ft.Page, handle_logout):
        self.page = page
        self.handle_logout = handle_logout

    def get_view(self):
        return ft.View(
            route='/',
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.CircleAvatar(
                            foreground_image_src=self.page.auth.user.get("picture", ""),
                            bgcolor=ft.Colors.GREY_400,
                            radius=40
                        ),
                        ft.Text(value=self.page.auth.user.get("name", "N/A"), size=20, weight=ft.FontWeight.BOLD),
                        ft.Text(value=self.page.auth.user.get("email", "N/A"), size=18),
                        ft.ElevatedButton(text="Logout", on_click=self.handle_logout),
                    ],
                )
            ]
        )
