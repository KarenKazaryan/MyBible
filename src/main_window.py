import flet as ft
from src.book_list import books


def main(page: ft.Page):
    page.title = "Библия"
    page.theme_mode = 'light'
    page.scroll = "adaptive"
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.START

    page.window_width = 400
    page.window_height = 600
    page.window_resizable = True

    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode=='dark' else 'dark'
        page.update()


    # def navigate(e):
    #     index = page.navigation_bar.selected_index
    #     page.clean()
    #
    #     if index==0: page.add()
    #     elif index==1: page.add()
    #     elif index == 2: page.add()
    #     elif index == 3: page.add()

    page.add(
        ft.Row([
            ft.ElevatedButton('SYNO'),
            ft.IconButton(ft.Icons.BRIGHTNESS_6, on_click=change_theme)
        ]
        )
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.BOOK, label="Книги"),
            ft.NavigationBarDestination(icon=ft.Icons.FORMAT_ALIGN_LEFT, label="Чтение"),
            ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="Поиск"),
            ft.NavigationBarDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                selected_icon=ft.Icons.BOOKMARK,
                label="Закладки",
            ),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Настройки"),
        ]
        # ], on_change=navigate()
    )

    for book in books["ru"]: page.add(ft.TextButton(text=book))

    # text = open('SYNO.txt', mode='r')



ft.app(main)
