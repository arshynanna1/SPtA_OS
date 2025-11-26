FROM jenkins/jenkins:lts

# Перемикаємо на root для встановлення пакетів
USER root

# Оновлюємо та встановлюємо інструменти для збірки
RUN apt-get update && \
    apt-get install -y \
    devscripts \
    debhelper \
    build-essential \
    rpm \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Створюємо папку для проектів
RUN mkdir -p /home/jenkins/workspace

# Повертаємося до користувача jenkins
USER jenkins

# Встановлюємо плагіни Jenkins
RUN jenkins-plugin-cli --plugins \
    pipeline:latest \
    git:latest \
    workflow-aggregator:latest

# Вказуємо порт
EXPOSE 8080

# Команда запуску
CMD ["jenkins.sh"]
