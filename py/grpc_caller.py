import grpc
from protos.octopus.octopus_pb2_grpc import OctopusStub
from protos.octopus import octopus_pb2
from protos.


class Stub:
    def __init__(self, host, port, auth, stub_cls):
        channel = grpc.insecure_channel("{}:{}".format(host, port),)
        self.stub = stub_cls(channel)

    def __getattr__(self, name):
        return getattr(self.stub, name)


if __name__ == "__main__":
    stub = Stub("127.0.0.1", "10003", "bayuser-rpc.xyz", OctopusStub)
    #  req = octopus_pb2.CreateServiceReq(service_name="postman-rpc.xyz")
    #  res = stub.CreateService(req)
    #  req = octopus_pb2.GetServiceReq(service_name="postman-rpc.xyz")
    #  res = stub.GetService(req)
    print(res)
