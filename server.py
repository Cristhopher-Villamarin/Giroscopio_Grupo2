import asyncio
import websockets
import webbrowser

async def handler(websocket):
    print(f"Cliente conectado: {websocket.remote_address}")
    async for message in websocket:
        print(f"Mensaje recibido: {message}")
        if message == "open_web":
            webbrowser.open('https://www.google.com/?hl=es')
        elif message == "open_sheet":
            webbrowser.open('https://docs.google.com/document/d/1WM3TNf-1JgdyRRVZQUH6Wh_KVj0wbednESM34saASms/edit?tab=t.0')
        elif message == "open_whatsapp":
            webbrowser.open('https://web.whatsapp.com/')

async def main():
    print("Iniciando el servidor WebSocket...")
    try:
        async with websockets.serve(handler, "0.0.0.0", 8080):
            print("Servidor WebSocket escuchando en ws://0.0.0.0:8080")
            await asyncio.Future()  # Mantiene el servidor corriendo
    except Exception as e:
        print(f"Error al iniciar el servidor: {e}")
  # run forever

if __name__ == "__main__":
    asyncio.run(main())
