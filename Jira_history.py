import torch
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import Trainer, TrainingArguments
import pandas as pd

# Загрузка предварительно обученной модели и токенизатора
model_name = 'bert-base-uncased'
model = BertForSequenceClassification.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)

# Загрузка данных из DataFrame
data = pd.read_csv("your_data.csv")  # Замените на свой файл данных

# Подготовка данных для дообучения
train_texts = data["text_column"].tolist()
train_labels = data["flag_column"].tolist()

# Токенизация и кодирование данных
train_encodings = tokenizer(train_texts, padding=True, truncation=True, return_tensors='pt')
train_labels = torch.tensor(train_labels)

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

# Сохранение дообученной модели и токенизатора
output_model_dir = "./custom_bert_model"
model.save_pretrained(output_model_dir)
tokenizer.save_pretrained(output_model_dir)
