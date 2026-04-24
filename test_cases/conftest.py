import pytest
from utils.db_handler import DBHandler

@pytest.fixture(scope="session")# session 表示整个测试过程只运行一次，省资源
def db():
    print("\n--- [Fixture] 正在连接数据库 ---")
    handler = DBHandler()
    
    yield handler

    print("\n--- [Fixture] 正在关闭数据库 ---")
    handler.close()