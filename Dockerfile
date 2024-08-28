# Use an official Nginx image as the base image
FROM nginx:alpine

# Copy static files to the Nginx HTML directory
COPY ./deploy /usr/share/nginx/html

# Expose port 80 to allow access to the web server
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]