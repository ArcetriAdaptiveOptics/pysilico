#!/usr/bin/env python

from pysilico.client.camera_client import CameraClient
from pysilico.utils.timeout import Timeout


class CBlueClient(CameraClient):

    def __init__(self, rpcHandler, sockets):
        super().__init__(rpcHandler, sockets)
