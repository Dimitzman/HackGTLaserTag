from channels import route
from shooting_stuff.players import connect_player, disconnect_player

channel_routing = [
    route("websocket.connect",connect_player,path=r'^/user/(?P<slug>[^/]+)/stream/$'),

    route("websocket.disconnect",disconnect_player,path=r'^/user/(?P<slug>[^/]+)/stream/$'),

]