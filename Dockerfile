FROM python:3.10

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv \
    libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev \
    libwebp-dev libtiff5-dev \
    curl build-essential gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*  

# Install Rust (needed for some ML libraries)
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

WORKDIR /app

# Upgrade pip and install dependencies
RUN pip3 install --upgrade pip setuptools wheel  

COPY requirements.txt .  
RUN pip3 install --no-cache-dir -r requirements.txt  && \
    pip3 install -U langchain-community huggingface_hub

# Create a directory for Llama model


RUN mkdir -p /app/models

# Download Llama model (replace with the actual model URL)
# RUN curl -o /app/models/llama-model.gguf "https://huggingface.co/TheBloke/Llama-2-7B-GGUF/resolve/main/llama-2-7b.Q4_K_M.gguf"
# RUN curl -o /app/models/llama-model.gguf "https://huggingface.co/matrixportal/Llama-2-7b-chat-hf-Q4_K_M-GGUF/raw/main/llama-2-7b-chat-hf-q4_k_m.gguf"
# Copy the app files

# Download the model directly
RUN huggingface-cli download TheBloke/Llama-2-7B-Chat-GGUF llama-2-7b-chat.Q2_K.gguf --local-dir /app/models/ --local-dir-use-symlinks False

# Rename to your standard name
RUN mv /app/models/llama-2-7b-chat-hf-q4_k_m.gguf /app/models/llama-model.gguf

# Set the path in environment
ENV LLAMA_MODEL_PATH="/app/models/llama-model.gguf"

# Set the correct path in the code
ENV LLAMA_MODEL_PATH="/app/models/llama-model.gguf"

COPY . . 
# Ensure scripts are executable
RUN chmod +x manage.py

EXPOSE 8000  

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]  
