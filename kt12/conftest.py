import pytest
from calculator_service import CalculatorServicer
import calculator_pb2_grpc

@pytest.fixture(scope="module")
def grpc_add_to_server():
    return calculator_pb2_grpc.add_CalculatorServicer_to_server

@pytest.fixture(scope="module")
def grpc_servicer():
    return CalculatorServicer()

@pytest.fixture(scope="module")
def grpc_stub_cls():
    return calculator_pb2_grpc.CalculatorStub
# pip install pytest-grpc
# pytest test_calculator.py -v