import json
import grpc
from protos.octopus_pb2_grpc import OctopusStub
from protos import octopus_pb2


class Stub:
    def __init__(self, host, port, stub_cls):
        channel = grpc.insecure_channel("{}:{}".format(host, port),)
        self.stub = stub_cls(channel)

    def __getattr__(self, name):
        return getattr(self.stub, name)


if __name__ == "__main__":
    # k port-forward krake-v2-b74f59c86-6cccd 10003:10003 -n mesh
    services = "readingoperation-api.cuckoo"
    stub = Stub("127.0.0.1", "10003", OctopusStub)
    res = dict()
    for s in services.split("\n"):
        s = s.strip()
        if not s:
            continue
        service = stub.CreateService(octopus_pb2.CreateServiceReq(service_name=s))
        service = stub.GetService(octopus_pb2.GetServiceReq(service_name=s))
        print(service)
        res[s] = {
            "auth_token": service.auth_token,
            "service_name": service.service_name,
            "service_code": service.service_code,
        }
    json.dump(res, open("svc_auth.json", "w"))
