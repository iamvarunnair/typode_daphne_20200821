from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': URLRouter(
        websocket_urlpatterns
    )
})
