# Using py.test framework
import os
import shutil

# run training script
import app  # noqa


# Check that all our metrics are exported into the expected location
def test_metrics_export():
    assert os.path.exists("metrics/accuracy.metric")
    assert os.path.exists("metrics/confusion_matrix.png")
    assert os.path.exists("metrics/f1.metric")
    assert os.path.exists("metrics/logloss.metric")
    assert os.path.exists("metrics/roc_auc.metric")

    # clean up test artifacts
    shutil.rmtree("metrics")


# Check that the model is persisted as onnx
def test_model_export():
    assert os.path.exists("model.onnx")

    # clean up test artifacts
    os.remove("model.onnx")
