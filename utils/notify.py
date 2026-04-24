# utils/notify.py
import requests
import json
import requests

def send_feishu_notification(passed, failed, total, report_url="http://localhost:5050"):
    # 替换成你真实的 Webhook 地址
    webhook_url = "https://open.feishu.cn/open-apis/bot/v2/hook/871c814e-60ad-4b99-8bf0-bb75481dba45"
    
    # 构造飞书卡片消息
    payload = {
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": "📊 自动化测试执行报告",
                    "content": [
                        [{"tag": "text", "text": f"项目名称：Lianxi2 接口自动化"}],
                        [{"tag": "text", "text": f"测试结果：✅ {passed} 通过 | ❌ {failed} 失败"}],
                        [{"tag": "text", "text": f"总用例数：{total}"}],
                        [{"tag": "a", "text": "🌐 点击查看详细 Allure 报告", "href": report_url}]
                    ]
                }
            }
        }
    }
    try:
        requests.post(webhook_url, json=payload, timeout=5)
    except Exception as e:
        print(f"发送通知失败: {e}")
    

def get_real_url():
    my_ip = "192.168.4.36"
    """
    自动判断：如果开了穿透就拿公网链接，没开就拿内网IP
    """
    try:
        # 4040 是 cpolar 默认的后台监控端口
        res = requests.get("http://127.0.0.1:4040/api/tunnels", timeout=1)
        # 自动获取第一个隧道的公网地址
        public_url = res.json()['tunnels'][0]['public_url']
        return public_url
    except:
        # 没开穿透就返回你公司的局域网 IP
        company_ip = f"http://{my_ip}:5050"
        return company_ip    