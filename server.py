import asyncio

import httpx

clients = [
    {"url": "http://192.168.10.13:8888/click"},
    {"url": "http://192.168.10.20:8888/click"},
]


async def send_click(client):
    async with httpx.AsyncClient() as client_session:
        try:
            response = await client_session.get(client["url"], timeout=3.0)
            print(f"Response from {client['url']}: {response.text}")
        except Exception as e:
            print(f"Error from {client['url']}: {str(e)}")


async def main():
    while True:
        input("Press Enter to send click... (Ctrl+C to exit)")
        tasks = [send_click(client) for client in clients]
        await asyncio.gather(*tasks)


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("\nProgram terminated by user")
