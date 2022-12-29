from elasticsearch import Elasticsearch
import json
import time
from elasticsearch import helpers


class connect_kafka():
    def __init__(self):
        try:
            self.es = Elasticsearch(['192.168.1.133:9200'], timeout=6, max_retries=6, retry_on_timeout=True)
            print("connect to elasticsearch sucessful")
        except Exception as e:
            print("connect failed", e)

    def writemany(self, topic, message):
        # print(es)
        # es.indices.create(index="python_es01", ignore=400)
        # print(data)
        action = [{
            "_index": "s3",
            "_type": "doc",
            "_source": {
                "title": i
            }
        } for i in range(100000)]
        start_time = time.time()
        helpers.bulk(self.es, action)
        print(f"耗时为：{time.time() - start_time}")
        print("finnish write to es")

    def writeone(self):
        start_time1 = time.time()
        info = [{
            "_index": "device_info1",
            "_type": "doc",
            "_source": {
                "safeDefendSoftware": [],
                "isInstallProbe": "0",
                "runtime": "0",
                "inputTime": 1651827180905,
                "security": 5,
                "isDelete": "0",
                "@timestamp": "2022-09-08T09:15:52.966Z",
                "safetyOfQualitative": "0",
                "sourceFactory": "和丰电厂",
                "linkWeights": 0,
                "insertDataBaseFunction": "1",
                "safetyOfTime": 0,
                "sourceCity": "塔城地区",
                "isHaveVul": "0",
                "usedLinks": 0,
                "storageTime": 1651827180905,
                "outageTime": 0,
                "deviceName": "#1机组OP5工控机",
                "isVirtualMachine": "0",
                "os": [],
                "deviceTypeOneName": "终端主机",
                "usability": 5,
                "dbMemoryOccupy": 0,
                "dbCpuOccupy": 0,
                "dataSource": "手动录入",
                "founders": "HFMDwhrg",
                "lastOnlineTime": 0,
                "isStandby": "0",
                "maintenanceTime": 0,
                "physicalRegion": "1",
                "residueLinks": 0,
                "lastOfflineTime": 0,
                "isImportantAsset": "1",
                "deviceScore": 5,
                "otherSoftware": [],
                "commissioningTime": 0,
                "integrality": 5,
                "database": [],
                "businessSector": "4",
                "linkMark": "0",
                "ipList": [
                    {
                        "ipAddr": "202.206.212.105",
                        "type": "业务",
                        "macAddr": "00:D0:C9:C3:E4:1B"
                    }
                ],
                "sourcePrefecture": "和布克赛尔蒙古自治县",
                "orgCode": "000010001000005",
                "deviceTypeOne": "5",
                "@version": "1",
                "deviceTypeTwo": "OWS",
                "syncTime": 1653879360715,
                "vendorChn": "研华科技",
                "internal": "1",
                "businessSoftware": [],
                "createTime": 1651827180905,
                "isHaveDB": "0",
                "systemId": "_EojmXoBqSTNc9dA3UTB",
                "securityScore": 0,
                "eventTypeId": "000012_5OWS_001249",
                "licenseExpiredTime": 0,
                "updateTime": 1651827260734,
                "deviceModel": " IPC-610-L",
                "id": "Z5OSmIABeccaN25yhaqM",
                "deviceStatus": "离线",
                "state": "3",
                "deviceTypeTwoName": "操作员站",
                "offtime": 300000,
                "isUrgentVul": "0",
                "sourceProvince": "新疆维吾尔自治区",
                "sid": i
            }
        } for i in range(100000)]
        print(f"生成数据耗时：{time.time() - start_time1}")
        try:
            start_time = time.time()
            helpers.bulk(self.es, info)
            print(f"插入ES耗时：{time.time() - start_time}")
        except Exception as e:
            print(e)
        # self.es.index(index="device_info", doc_type="_doc", body=info)

        # try:
        #     for i in range(10000000):
        #         helpers.bulk(es, action)

        # es.index(index=topic, doc_type="doc", body=message)
        # es.index(index="python_es01", doc_type="doc", id=i, body={"name": "kitty", "age": 50})
        # except Exception as e:
        #     print('failed ', e)
        # es.close()


if __name__ == '__main__':
    abc = connect_kafka()
    abc.writeone()

    # write_kafka = connect_kafka()
    # data = {"name": "kitty", "age": 50}
    # write_kafka.write('hello', data)
