FROM nginx:alpine

# Copy static assets and nginx config into the image
COPY index.html /usr/share/nginx/html/index.html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80