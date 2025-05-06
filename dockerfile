# Dockerfile
FROM python:3.11.9

# Set the working directory in the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Set the PYTHONPATH to include src/
ENV PYTHONPATH=/app/src

# Copy the application code
COPY . .

# Specify the command to run on container start
# CMD ["crewai", "run"]

# Set the entrypoint to crewai
ENTRYPOINT ["crewai"]

# Default to "run" if no command is provided
CMD ["run"]