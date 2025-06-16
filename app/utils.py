# utils.py 各种工具函数
import os
import random
import json
import time
from datetime import datetime

import requests

from dotenv import load_dotenv
import logging

load_dotenv()

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TOKEN_FILE = os.path.join(BASE_DIR, "dingtalk_token.json")

logger = logging.getLogger(__name__)

now_str = datetime.now().strftime("%Y-%m-%d %H:%M")


# 生成3个5-60之间的随机数
def generate_random_number() -> list[int]:
    return [random.randint(5, 60) for _ in range(3)]


# 宜搭get access token
def get_dingtalk_access_token() -> str:
    # 尝试读取已有 token
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            data = json.load(f)
            if time.time() < data.get("expires_at", 0):
                print("✅ 使用缓存的 accessToken")
                return data["access_token"]

    # 缓存不存在或已过期，重新获取
    url = "https://api.dingtalk.com/v1.0/oauth2/accessToken"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "appKey": os.getenv("DINGTALK_APP_KEY"),
        "appSecret": os.getenv("DINGTALK_APP_SECRET")
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        res_data = response.json()
        access_token = res_data.get("accessToken")
        expire_in = res_data.get("expireIn", 7200)  # 默认 2 小时

        if access_token:
            print("✅ 成功获取新的 accessToken")
            with open(TOKEN_FILE, "w") as f:
                json.dump({
                    "access_token": access_token,
                    "expires_at": time.time() + expire_in - 60  # 提前 1 分钟过期
                }, f)
            return access_token
        else:
            print("⚠️ 获取失败，响应内容：", res_data)
            return None
    except requests.exceptions.RequestException as e:
        print("❌ 请求失败：", e)
        return None

# 更新宜搭邮件管理表单实例
def create_yida_form_instance(
    access_token: str,
    app_type: str,
    system_token: str,
    user_id: str,
    form_uuid: str,
    form_data: dict,
    # use_alias: bool = False,
    # language: str = "zh_CN"
) -> dict:
    url = "https://api.dingtalk.com/v2.0/yida/forms/instances"
    headers = {
        "Content-Type": "application/json",
        "x-acs-dingtalk-access-token": access_token
    }

    payload = {
        "appType": app_type,
        "systemToken": system_token,
        "userId": user_id,
        "formUuid": form_uuid,
        "formDataJson": json.dumps(form_data, ensure_ascii=False),
    }

    print(payload)

    try:
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()

        print(data)

        # 判断是否成功（钉钉返回的业务字段）
        if response.status_code == 200 and data.get("result"):
            logger.info("✅ 表单创建成功，ID：", data["result"])
            return {"success": True, "formInstanceId": data["result"]}
        else:
            logger.error("⚠️ 表单创建失败，响应内容：", data)
            return {"success": False, "detail": data}

    except requests.exceptions.RequestException as e:
        logger.error("❌ 网络请求失败：", e)
        return {"success": False, "error": str(e)}


if __name__ == "__main__":
    create_yida_form_instance(
        access_token=get_dingtalk_access_token(),
        user_id="571848422",
        form_data={
            "textField_m8sdofy7": "test",
            "textField_m8sdofy8": "test",
            "textfield_G00FCbMy": "test",
            "editorField_m8sdofy9": "test",
            "radioField_manpa6yh": "发送成功",
            "textField_mbyk13kz": now_str,
            "textField_mbyk13l0": now_str,
        },
        app_type="APP_CO8KQ06DK6RV8P21ZQGM",
        system_token="P1A66RD1E73U50OZE98UWA2GB10L2GIVKDS8M4S",
        form_uuid="FORM-49866E71Y53UDC1MCPD8D587FTQD3OCPNDS8M3"
    )