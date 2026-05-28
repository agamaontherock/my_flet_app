import flet as ft
from models import load_user_data
from views import home_view, settings_view

def main(page: ft.Page):
    page.title = "Маршрутизація"
    page.theme_mode = ft.ThemeMode.LIGHT

    user_state = load_user_data()

    def route_change():
        page.views.clear()
        page.views.append(home_view(page, user_state))
        if page.route == "/settings":
            page.views.append(settings_view(page, user_state))
        page.update()


    async def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)