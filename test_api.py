from core.engine.sync_engine import SyncEngine
from core.loader.loader import Loader
import pytest
from core.runner.case_runner import CaseRunner
import allure


engine = SyncEngine()
loader = Loader()
case_map, runnable_case = loader.load_cases()

print(f"找到的用例数量为{len(runnable_case)}")

runner = CaseRunner(engine,case_map)


class Test_Api:
    @pytest.mark.parametrize("runnable_case",runnable_case,ids= [c.get("name") for c in runnable_case])
    def test_api(self,runnable_case):
        runner.case_runner(runnable_case)