import asyncio
import websockets
import webbrowser

async def handler(websocket, path):
    print(f"Cliente conectado: {websocket.remote_address}")
    async for message in websocket:
        print(f"Mensaje recibido: {message}")
        if message == "open_web":
            webbrowser.open('https://refactoring.guru/es/design-patterns')
        elif message == "open_sheet":
            webbrowser.open('https://docs.google.com/spreadsheets/d/0B7uNrThIIZTmeWZka2ZvemUtYkE/edit?gid=1307076623&resourcekey=0-2Be8unJoKd74W_jnqGKNaQ#gid=1307076623')
        elif message == "open_whatsapp":
            webbrowser.open('https://web.whatsapp.com')

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("Servidor WebSocket escuchando en ws://0.0.0.0:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
