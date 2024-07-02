from pysilico.utils.constants import Constants


def _getDefaultConfigFilePath():
    from plico.utils.config_file_manager import ConfigFileManager
    cfgFileMgr= ConfigFileManager(Constants.APP_NAME,
                                  Constants.APP_AUTHOR,
                                  Constants.THIS_PACKAGE)
    return cfgFileMgr.getConfigFilePath()


defaultConfigFilePath= _getDefaultConfigFilePath()


def camera(hostname, port):

    from pysilico.client.camera_client import CameraClient
    from plico.rpc.zmq_remote_procedure_call import ZmqRemoteProcedureCall
    from plico.rpc.zmq_ports import ZmqPorts
    from plico.rpc.sockets import Sockets


    rpc= ZmqRemoteProcedureCall()
    zmqPorts= ZmqPorts(hostname, port)
    sockets= Sockets(zmqPorts, rpc)
    return CameraClient(rpc, sockets)


def list_cameras(timeout_in_seconds=2):
    from plico.utils.discovery_server import DiscoveryClient
    return DiscoveryClient().run(timeout_in_seconds=timeout_in_seconds, filter={'server_type': 'pysilico'})

def find(camera_name, timeout_in_seconds=2):
    from plico.utils.discovery_server import DiscoveryClient
    server_info = DiscoveryClient().run(camera_name, timeout_in_seconds, filter={'server_type': 'pysilico'})
    return camera(server_info.host, server_info.port)
