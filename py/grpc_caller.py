import grpc
from protos.octopus_pb2_grpc import OctopusStub
from protos import octopus_pb2


class Stub:
    def __init__(self, host, port, auth, stub_cls):
        channel = grpc.insecure_channel("{}:{}".format(host, port),)
        self.stub = stub_cls(channel)

    def __getattr__(self, name):
        return getattr(self.stub, name)


if __name__ == "__main__":
    stub = Stub("127.0.0.1", "10003", "codetime-rpc.codetime", OctopusStub)
    #  req = octopus_pb2.CreateServiceReq(service_name="codetime-rpc.codetime")
    #  res = stub.CreateService(req)
    req = octopus_pb2.GetServiceReq(service_name="codetime-rpc.codetime")
    res = stub.GetService(req)
    print(res)
