import importlib.util
import subprocess
import sys

def installAndCheck(package):
    if importlib.util.find_spec(package) is None:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"{package} installed")
    else:
        print(f"{package} already installed")

try:
    import flet as ft
    import datetime
    def main(page: ft.Page):
        page.title = "Registro de usuarios"
        page.window_width = 700
        page.window_height = 650
        page.window_resizable = False
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    # Título centrado
        titulo = ft.Text("Registro de usuarios", 
                         size=24, 
                         weight=ft.FontWeight.BOLD, 
                         text_align=ft.TextAlign.CENTER)

    # Primera fila: Nombre y Apellidos
        fila_nombre_apellido = ft.Row([
            ft.TextField(label="Nombre"),
            ft.TextField(label="Apellidos")
        ], alignment=ft.MainAxisAlignment.CENTER)

    # Segunda fila: Cédula y Apartamento/Torre
        fila_cedula_apartamento = ft.Row([
            ft.TextField(label="Cédula"),
            ft.Dropdown(label="Apartamento", options=[ft.dropdown.Option("option1"), ft.dropdown.Option("option2"), ft.dropdown.Option("option3")]),
            ft.Dropdown(label="Torre", options=[ft.dropdown.Option("option1"), ft.dropdown.Option("option2"), ft.dropdown.Option("option3")])
        ], alignment=ft.MainAxisAlignment.CENTER)
        now = datetime.datetime.now()
        fecha_actual = now.strftime("%Y/%m/%d")
        hora_actual = now.strftime("%I:%M %p")
    # Tercera fila: Fecha y Hora de llegada
        fila_fecha_hora = ft.Row([
            ft.TextField(label="Fecha de llegada", value=fecha_actual),
            ft.TextField(label="Hora de llegada", value=hora_actual)
        ], alignment=ft.MainAxisAlignment.CENTER)

    # Responsable
        texto_responsable = ft.Text("Responsable", text_align=ft.TextAlign.CENTER)

        fila_responsable = ft.Row([
            ft.Dropdown(label="Responsable", options=[ft.dropdown.Option("option1"), ft.dropdown.Option("option2"), ft.dropdown.Option("option3")]),
            ft.TextField(label="Nombres apellidos del responsable")
        ], alignment=ft.MainAxisAlignment.CENTER)

    # Botón Registrar
        boton_registrar = ft.ElevatedButton("Registrar", bgcolor=ft.colors.GREEN, color=ft.colors.WHITE)

    # Contenedor principal
        page.add(
            titulo,
            fila_nombre_apellido,
            fila_cedula_apartamento,
            fila_fecha_hora,
            texto_responsable,
            fila_responsable,
            ft.Row([boton_registrar], alignment=ft.MainAxisAlignment.CENTER)
    )

    ft.app(target=main)

except ImportError:
    installAndCheck("flet")
