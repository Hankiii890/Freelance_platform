FROM python

# Установка зависимостей
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта django
COPY . .

# Настраиваем среду
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Запускаем сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]




