import flet as ft
from player1dev.client import main as player1dev_main

navbar = ft.NavigationBar()
sidebar = ft.NavigationRail()


ft.app(
    target=player1dev_main,
    view=ft.WEB_BROWSER,
    route_url_strategy="path",
)
