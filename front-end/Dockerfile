FROM nginx:latest

# Скопировать файлы конфигурации Nginx
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

# Скопировать файлы контента вашего приложения
COPY src /usr/share/nginx/html

EXPOSE 80