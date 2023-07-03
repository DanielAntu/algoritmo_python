import flet as ft


def main(page: ft.Page):
    page.title = 'Algoritmo 18'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(
        hint_text='Digite um número', text_align=ft.TextAlign.LEFT, width=500)
    txt_res = ft.TextField(
        value='0', text_align=ft.TextAlign.CENTER, width=700, height=100, border=None, border_color='#fff', read_only=True, text_size=50)

    def Soma(e):
        txt_res.value = str(int(txt_number.value) + 1)
        txt_number.value = ''
        txt_number.autofocus = True
        page.update()

    bsoma = ft.ElevatedButton(
        on_click=Soma, bgcolor=ft.colors.BLUE, text='Somar', width=200, height=60, color='#ffffff')

    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        txt_number,
                        bsoma
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        txt_res
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ]
        )
    )


ft.app(target=main)
