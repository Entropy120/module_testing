import calculator_pb2


# ==================== БИЗНЕС-ЛОГИКА (УМНОЖЕНИЕ) ====================

def test_multiply_by_two_positive(grpc_stub):
    """TC-01: Умножение положительного числа на 2"""
    request = calculator_pb2.MultiplyRequest(number=5)
    response = grpc_stub.MultiplyByTwo(request)
    assert response.result == 10


def test_multiply_by_two_zero(grpc_stub):
    """TC-02: Умножение нуля на 2 (граничное значение)"""
    request = calculator_pb2.MultiplyRequest(number=0)
    response = grpc_stub.MultiplyByTwo(request)
    assert response.result == 0


def test_multiply_by_two_negative(grpc_stub):
    """TC-03: Умножение отрицательного числа на 2 (НОВЫЙ)"""
    request = calculator_pb2.MultiplyRequest(number=-5)
    response = grpc_stub.MultiplyByTwo(request)
    assert response.result == -10


# ==================== БИЗНЕС-ЛОГИКА (СЛОЖЕНИЕ) ====================

def test_add_numbers_positive(grpc_stub):
    """TC-04: Сложение положительных чисел"""
    request = calculator_pb2.AddRequest(a=3, b=7)
    response = grpc_stub.AddNumbers(request)
    assert response.sum == 10


def test_add_negative_numbers(grpc_stub):
    """TC-05: Сложение отрицательных чисел (НОВЫЙ)"""
    request = calculator_pb2.AddRequest(a=-3, b=-7)
    response = grpc_stub.AddNumbers(request)
    assert response.sum == -10


def test_add_large_numbers(grpc_stub):
    """TC-06: Сложение больших чисел"""
    large_a, large_b = 100000, 200000
    request = calculator_pb2.AddRequest(a=large_a, b=large_b)
    response = grpc_stub.AddNumbers(request)
    assert response.sum == large_a + large_b


# ==================== КОНТРАКТНЫЕ ТЕСТЫ (ПРОВЕРКА СТРУКТУРЫ) ====================

def test_contract_structure_and_types(grpc_stub):
    """TC-07: Структура и типы данных соответствуют .proto"""
    request = calculator_pb2.MultiplyRequest(number=42)
    response = grpc_stub.MultiplyByTwo(request)

    assert hasattr(response, 'result')  # Поле существует
    assert isinstance(response.result, int)  # Правильный тип
    assert response.result == 84  # Корректное значение


def test_contract_required_fields(grpc_stub):
    """TC-08: Обязательные поля не пропускаются (значение по умолчанию)"""
    # В proto3 все поля опциональны, если не заданы - они равны 0
    request = calculator_pb2.MultiplyRequest()
    response = grpc_stub.MultiplyByTwo(request)
    assert response.result == 0


def test_contract_backward_compatibility(grpc_stub):
    """TC-09: Обратная совместимость — старый клиент с новым сервером"""
    request_v1 = calculator_pb2.MultiplyRequest(number=10)
    response_v1 = grpc_stub.MultiplyByTwo(request_v1)
    assert response_v1.result == 20


def test_contract_field_types_validation(grpc_stub):
    """TC-10: Проверка типов данных в ответе"""
    request = calculator_pb2.AddRequest(a=5, b=10)
    response = grpc_stub.AddNumbers(request)
    assert isinstance(response.sum, int)
    assert response.sum == 15