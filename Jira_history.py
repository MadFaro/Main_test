import torch
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import Trainer, TrainingArguments
from torch.utils.data import Dataset
import pandas as pd

# Загрузка предварительно обученной модели из файла h5 с помощью TensorFlow
h5_model_path = "путь_к_файлу_модели.h5"
loaded_model = tf.keras.models.load_model(h5_model_path)

# Используйте эту модель как базовую для модели BertForSequenceClassification
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", state_dict=loaded_model.state_dict())

# Загрузка токенизатора из файла JSON
tokenizer_path = "путь_к_файлу_токенизатора.json"
tokenizer = BertTokenizer.from_pretrained(tokenizer_path, do_lower_case=True)  # Установите do_lower_case в зависимости от токенизатора

# Загрузка данных из DataFrame
data = pd.read_csv("your_data.csv")  # Замените на свой файл данных

# Подготовка данных для дообучения
train_texts = data["text_column"].tolist()
train_labels = data["flag_column"].tolist()

# Токенизация и кодирование данных
train_encodings = tokenizer(train_texts, padding=True, truncation=True, return_tensors='pt')
train_labels = torch.tensor(train_labels)

# Создание класса набора данных
class MyDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels
    
    def __len__(self):
        return len(self.labels)
    
    def __getitem__(self, idx):
        item = {key: val[idx] for key, val in self.encodings.items()}
        item['labels'] = self.labels[idx]
        return item

# Настройка тренировки
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=8,
    evaluation_strategy="steps",
    eval_steps=500,
    save_steps=1000,
    save_total_limit=2,
)

# Создание и обучение трейнера
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=MyDataset(train_encodings, train_labels),
)

trainer.train()

# Сохранение дообученной модели
output_model_dir = "./custom_bert_model"
model.save_pretrained(output_model_dir)
