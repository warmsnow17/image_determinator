import torch
from torchvision import transforms, models
from PIL import Image
from torchvision.models.resnet import ResNet50_Weights
import requests

LABELS_URL = 'https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json'
labels = requests.get(LABELS_URL).json()

model = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
model.eval()

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])


def image_determinator(image_path):
    img_pil = Image.open(image_path).convert('RGB')
    width, height = img_pil.size
    img_tensor = preprocess(img_pil)
    img_tensor = img_tensor.unsqueeze(0)

    with torch.no_grad():
        outputs = model(img_tensor)

    _, predicted = torch.max(outputs, 1)
    result = labels[predicted.item()]

    return width, height, result
