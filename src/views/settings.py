import flet as ft
from models import validate_username, save_user_data


def settings_view(page: ft.Page, user_state: dict):
    name_input = ft.TextField(
        label="Ваше ім'я",
        value=user_state.get("username"),
        width=300
    )
    status_msg = ft.Text()

    async def go_home(e):
        await page.push_route("/")

    def on_save_click(e):
        success, message = validate_username(name_input.value)
        if success:
            user_state["username"] = name_input.value.strip()
            save_user_data(user_state)
            status_msg.value = "Збережено успішно!"
            status_msg.color = ft.Colors.GREEN
        else:
            status_msg.value = message
            status_msg.color = ft.Colors.RED

        page.update()

    return ft.View(
        route="/settings",
        controls=[
            ft.AppBar(
                title=ft.Text("Налаштування"),
                bgcolor=ft.Colors.GREEN,
                actions=[
                    ft.Row(
                        controls=[
                            ft.TextButton("Головна", style=ft.ButtonStyle(color=ft.Colors.WHITE), on_click=go_home),
                            ft.TextButton("Налаштування", style=ft.ButtonStyle(color=ft.Colors.WHITE))
                        ]
                    )
                ]
            ),
            ft.Column([
                name_input,
                ft.ElevatedButton("Зберегти зміни", on_click=on_save_click),
                status_msg,
                ft.TextButton("Повернутися назад", on_click=go_home)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        ]
    )