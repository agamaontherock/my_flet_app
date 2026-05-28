import flet as ft

def home_view(page: ft.Page, user_state: dict):
    async def go_to_settings(e):
        await page.push_route("/settings")

    return ft.View(
        route="/",
        controls=[
            ft.AppBar(
                title=ft.Text("Головна"),
                bgcolor=ft.Colors.GREEN,
                actions=[
                    ft.Row(
                        controls=[
                            ft.TextButton("Головна", style=ft.ButtonStyle(color=ft.Colors.WHITE)),
                            ft.TextButton("Налаштування",
                                          style=ft.ButtonStyle(color=ft.Colors.WHITE),
                                          on_click=go_to_settings)
                        ]
                    )
                ]
            ),
            ft.Column([
                ft.Text(f"Привіт, {user_state.get('username')}!", size=32, weight=ft.FontWeight.BOLD),
            ], alignment=ft.MainAxisAlignment.CENTER, expand=True)
        ]
    )