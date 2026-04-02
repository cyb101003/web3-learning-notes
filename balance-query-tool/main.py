# 0G链/以太坊 余额查询小工具
# 作者：陈宇博 (Chen Yubo)
# 开发时间：2026.03

import requests
import json

# 0G测试RPC节点
OG_TESTNET_RPC = "https://og-testnet-rpc.0g.ai"

def get_balance(address, rpc_url=OG_TESTNET_RPC):
    """
    查询0G链地址余额
    :param address: 钱包地址（0x）
    :param rpc_url: 链上RPC节点
    :return: 余额（单位：0G）
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [address, "latest"],
        "id": 1
    }
    
    try:
        response = requests.post(rpc_url, json=payload)
        data = response.json()
        
        # 十六进制余额转十进制，换算为0G
        balance_wei = int(data["result"], 16)
        balance_og = balance_wei / 10**18
        return round(balance_og, 4)
    
    except Exception as e:
        print(f"查询出错：{e}")
        return 0

# 测试用例
if __name__ == "__main__":
    test_address = "0x1234567890123456789012345678901234567890"
    print(f"测试地址：{test_address}")
    print(f"0G测试网余额：{get_balance(test_address)} 0G")
    print("工具运行成功！")
