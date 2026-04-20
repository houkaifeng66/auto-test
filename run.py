import os
import pytest
import time
import shutil

class Run:
    
    
    def run():
        time_stamp = time.strftime("%Y%m%d_%H%M%S")
        temp_results = "./reports/allure_results"
        archive_dir = f"./reports/archive/{time_stamp}"

        print(f"🚀 开始测试任务，时间: {time_stamp}")
        
        pytest.main([
            "-sv",
            "test_api.py",
            f"--alluredir={temp_results}",
            "--clean-alluredir"
        ]
        )

        if os.path.exists(temp_results):
            shutil.copytree(temp_results,archive_dir,dirs_exist_ok=True)
            print(f"✅ 历史记录已存入: {archive_dir}")

    if __name__ == "__main__":
        run()
