import torch
import torch.onnx
from ultralytics import YOLO 
import onnx
from onnx_tf.backend import prepare

# 모델 로드
weights = '/home/dnflrha12/PathPal-ML/yolov5/yolov8s_epoch80_stairs_and_greenlight.pt'

model = YOLO(weights) 
model.eval()

# 더미 입력 데이터 생성
example_input = torch.randn(1, 3, 640, 640)

torch.onnx.export(model, example_input, 'model.onnx', export_params=True)

# ONNX 파일 로드
model_onnx = onnx.load('model.onnx')

# TensorFlow 모델로 변환
tf_rep = prepare(model_onnx)

# 변환된 모델을 저장
tf_rep.export_graph('model_tf')
