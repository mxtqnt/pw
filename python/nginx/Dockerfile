FROM nginx

# Copy custom configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Copy static content directory
COPY static-content/ /usr/share/nginx/html

# Expose port 80 for incoming traffic
EXPOSE 80

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]