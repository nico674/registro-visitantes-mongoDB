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
    import pymongo

# Conectar a la base de datos MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["registro_usuarios"]
    collection = db["usuarios"]

    def registrar_usuario(e):
        usuario = {
            "nombre": nombre_field.value,
            "apellidos": apellidos_field.value,
            "cedula": cedula_field.value,
            "apartamento": apartamento_dropdown.value,
            "torre": torre_dropdown.value,
            "fecha_llegada": fecha_field.value,
            "hora_llegada": hora_field.value,
            "responsable": responsable_dropdown.value,
            "nombre_responsable": nombre_responsable_field.value
    }
        collection.insert_one(usuario)
        print("Usuario registrado correctamente en la base de datos.")

    def actualizar_fecha_hora():
        now = datetime.datetime.now()
        fecha_field.value = now.strftime("%Y/%m/%d")
        hora_field.value = now.strftime("%I:%M %p")
        fecha_field.update()
        hora_field.update()

    def main(page: ft.Page):
        page.title = "Registro de usuarios"
        page.window_width = 700
        page.window_height = 650
        page.window_resizable = False
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Título centrado
        titulo = ft.Text("Registro de usuarios", size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)

    # Campos de entrada
        global nombre_field, apellidos_field, cedula_field, apartamento_dropdown, torre_dropdown, responsable_dropdown, nombre_responsable_field, fecha_field, hora_field
        nombre_field = ft.TextField(label="Nombre")
        apellidos_field = ft.TextField(label="Apellidos")
        cedula_field = ft.TextField(label="Cédula")
        apartamento_dropdown = ft.Dropdown(label="Apartamento", options=[ft.dropdown.Option("option1"), ft.dropdown.Option("option2"), ft.dropdown.Option("option3")])
        torre_dropdown = ft.Dropdown(label="Torre", options=[ft.dropdown.Option("option1"), ft.dropdown.Option("option2"), ft.dropdown.Option("option3")])
        responsable_dropdown = ft.Dropdown(label="Responsable", options=[ft.dropdown.Option("option1"), ft.dropdown.Option("option2"), ft.dropdown.Option("option3")])
        nombre_responsable_field = ft.TextField(label="Nombres apellidos del responsable")

        fecha_field = ft.TextField(label="Fecha de llegada", read_only=True)
        hora_field = ft.TextField(label="Hora de llegada", read_only=True)
        actualizar_fecha_hora()
    
    # Fila de Nombre y Apellidos
        fila_nombre_apellido = ft.Row([nombre_field, apellidos_field], alignment=ft.MainAxisAlignment.CENTER)

    # Fila de Cédula y Apartamento/Torre
        fila_cedula_apartamento = ft.Row([cedula_field, apartamento_dropdown, torre_dropdown], alignment=ft.MainAxisAlignment.CENTER)

    # Fila de Fecha y Hora de llegada
        fila_fecha_hora = ft.Row([fecha_field, hora_field], alignment=ft.MainAxisAlignment.CENTER)

        # Responsable
        texto_responsable = ft.Text("Responsable", text_align=ft.TextAlign.CENTER)
        fila_responsable = ft.Row([responsable_dropdown, nombre_responsable_field], alignment=ft.MainAxisAlignment.CENTER)

    # Botón Registrar
        boton_registrar = ft.ElevatedButton("Registrar", bgcolor=ft.colors.GREEN, color=ft.colors.WHITE, on_click=registrar_usuario)

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

    # Actualizar fecha y hora cada segundo
        def actualizar_periodicamente():
            actualizar_fecha_hora()
            page.update()
            page.run_async(lambda: page.run_task(asyncio.sleep(1), actualizar_periodicamente))

        actualizar_periodicamente()

    ft.app(target=main)


except ImportError as e:
    installAndCheck("flet")
    print(f"✖️ error al conectar la base de datos  {e}")