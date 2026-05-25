FROM python:3.10-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0  # Production mode

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apk add --no-cache \
    gcc \
    musl-dev \
    python3-dev \
    postgresql-dev \
    jpeg-dev \
    zlib-dev \
    libffi-dev \
    openssl-dev

# Install Python dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Create media directory (CRITICAL STEP!)
RUN mkdir -p media/board_members media/gallery_images media/management media/success_stories

# Give proper permissions
RUN chmod -R 755 media/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8080

# Start command
CMD python manage.py migrate --noinput && \
    python manage.py createcachetable && \
    gunicorn dict.wsgi:application --bind 0.0.0.0:$PORT --workers 3 --timeout 120