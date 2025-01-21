import flet as ft

class MainView:
    def __init__(self, handle_login):
        self.handle_login = handle_login

    def get_view(self):
        return ft.View(
            route='/',
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    width=600,
                    controls=[
                        ft.Text("Demo Application", size=30, weight=ft.FontWeight.BOLD),
                        ft.Text(
                            "This application demonstrates how to add authentication and SSO to your Flet app using Descope.",
                            size=18,
                            weight=ft.FontWeight.W_500,
                        ),
                        ft.ElevatedButton(text="Login", on_click=self.handle_login),
                    ],
                )
            ]
        )
