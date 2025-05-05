import timeit

def test_prediction_speed():
    exec_time = timeit.timeit("from modules.arcanx import analyzer", number=10)
    assert exec_time < 2  # Ajuste le seuil
