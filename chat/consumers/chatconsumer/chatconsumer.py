from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        pass

    async def receive(self, content):
        pass

    async def disconnect(self, close_code):
        pass
