import os
import yaml

class Loader:
    def load_cases(self,case_dir="./test_cases"):
        all_entries = []
        for root , dirs , files in os.walk(case_dir):
            for file in files:
                if file.endswith(".yaml"):
                    file_path = os.path.join(root,file)
                    with open(file_path,"r",encoding="utf-8") as f:
                        file_data = yaml.safe_load(f)
                        if isinstance(file_data,list):
                            for entry in file_data:
                                entry["file_path"] = file_path
                            all_entries.extend(file_data)
                        else:
                            raise Exception(f"{file_path}数据错误，非列表")

        case_map = {entry["name"]:entry for entry in all_entries if "name" in entry}

        runnable_case = []
        skip_count = 0
        for entry in all_entries:
            is_in_scenarios = "scenarios" in entry.get("file_path","")
            is_runnable_true = entry.get("is_runnable") is True
            if is_in_scenarios or is_runnable_true:
                runnable_case.append(entry)
            else:
                skip_count += 1

        print(f"✅ 发现总用例数: {len(all_entries)}")   
        print(f"🚀 计划执行用例数: {len(runnable_case)}")
        print(f"📦 存入单个接口数量: {skip_count}")

        return case_map,runnable_case







        # for file in os.listdir(case_dir):
        #     if file.endswith(".yaml"):
        #         file_path = os.path.join(case_dir,file)
        #         with open(file_path,"r",encoding="utf-8") as f:
        #             file_data = yaml.safe_load(f)
        #             if file_data and isinstance(file_data,list):
        #                 all_entries.extend(file_data)
        #             else:
        #                 print(f"⚠️ 跳过文件 {file_path}: 格式错误（不是列表）。")
        #                 continue
        #                 # raise Exception(f"{file_path}有问题")
        # case_map = {}
        # for entry in all_entries:
        #     if "name" in entry:
        #         case_map[entry["name"]] = entry
        # runable_cases = []
        # for entry in all_entries:
        #     if "scenario" in entry or "request" in entry:
        #         runable_cases.append(entry)
        # return case_map,runable_cases

