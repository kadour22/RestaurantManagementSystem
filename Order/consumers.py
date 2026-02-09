from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ordering_consumer(AsyncWebsocketConsumer) :

    async def connect(self):
        self.group_name = "orders"
        await self.channel_layer.group_add(self.group_name,self.channel_name)
        await self.accept()
        print("connected")

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name,self.channel_name)
        print("disconnected..")
    
    async def create_order(self,event) :
        await self.send(
            text_data=json.dumps({
                "type":"create_order",
                "table":event["table"],
                "status":event["status"],
                "total_price":str(event["total_price"]),
                "created_at":event["created_at"]
            })
        )
