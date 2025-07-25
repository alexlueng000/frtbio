FROM php:7.4-apache

# 启用 Apache mod_rewrite
RUN a2enmod rewrite

# 可选：开启 Apache 错误日志显示（开发用）
RUN sed -i 's|^#ServerName www.example.com|ServerName localhost|' /etc/apache2/apache2.conf

# 修改 Apache 的 DocumentRoot 配置，使 .htaccess 生效
RUN sed -i '/<Directory \/var\/www\/>/,/<\/Directory>/ s/AllowOverride None/AllowOverride All/' /etc/apache2/apache2.conf