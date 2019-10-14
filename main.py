# coding=utf-8
import requests
from apig_sdk import signer

if __name__ == '__main__':
    sig = signer.Signer()
    sig.Key = "bbeed2b5-8b7f-44d2-8ae1-3d7a78b5b249"
    sig.Secret = "52cf34a05b4c3cfd467fc60c6a9571bd3a3b19d5d12d93b3860f72b582551567"

    r = signer.HttpRequest("GET", 
                           #"https://29c8bf7004354c28a8ece1e9db45d710.apic.cn-east-2.huaweicloudapis.com/test",
                           "https://3d98f804db0e4fb4bb32677f973c3d44.apic.cn-east-2.huaweicloudapis.com/testA",
                           {"x-stage": "RELEASE"},
                           "body")
    sig.Sign(r)
    print(r.headers["X-Sdk-Date"])
    print(r.headers["Authorization"])
    resp = requests.request(r.method, r.scheme + "://" + r.host + r.uri, headers=r.headers, data=r.body)
    print(resp.status_code, resp.reason)
    print(resp.content)
