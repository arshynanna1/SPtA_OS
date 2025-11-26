FROM jenkins/jenkins:lts

USER root

# Встановлюємо інструменти збірки
RUN apt-get update && \
    apt-get install -y \
    devscripts \
    debhelper \
    build-essential \
    rpm \
    git \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Перевіряємо встановлення
RUN which dpkg-deb && which rpmbuild

# Створюємо робочу папку
RUN mkdir -p /home/jenkins/workspace
RUN chown jenkins:jenkins /home/jenkins/workspace

USER jenkins

# Встановлюємо плагіни (без :latest)
RUN jenkins-plugin-cli --plugins \
    pipeline \
    git \
    workflow-aggregator

EXPOSE 8080

CMD ["jenkins.sh"]
