import os
import pytest
import time
import shutil
import json
from utils.notify import send_feishu_notification
from utils.notify import get_real_url
class Run:
    
    
    def run():
        time_stamp = time.strftime("%Y%m%d_%H%M%S")
        temp_results = "./reports/allure_results"
        archive_dir = f"./reports/archive/{time_stamp}"      #时间戳

        print(f"🚀 开始测试任务，时间: {time_stamp}")
        
        exit_code =pytest.main([
            "-sv",
            "test_api.py",
            f"--alluredir={temp_results}",
            "--clean-alluredir"
        ]
        )                                                    #运行命令

        passed = 0
        failed = 0
        if os.path.exists(temp_results):
            for file in os.listdir(temp_results):
                if file.endswith("-result.json"):
                    with open(os.path.join(temp_results, file), 'r') as f:
                        result = json.load(f)
                        if result.get("status") == "passed":
                            passed += 1
                        else:
                            failed += 1
        total = passed + failed
        print(f"🏁 测试结束：总计 {total}, 通过 {passed}, 失败 {failed}")                   
        final_url = get_real_url()
        send_feishu_notification(passed, failed, total,report_url=final_url)   #机器人报告的链接


        if os.path.exists(temp_results):
            shutil.copytree(temp_results,archive_dir,dirs_exist_ok=True)
            print(f"✅ 历史记录已存入: {archive_dir}")

    if __name__ == "__main__":
        run()
