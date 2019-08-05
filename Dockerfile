FROM       josephharrisonlim/rasa as base
RUN        echo "PYTHONUNBUFFERED=1" >> /etc/profile
WORKDIR    /app
COPY       . .

# TODO: Not sure how to actually run this inside a container while on Windows, somehow need to let it access the mic
# docker build -t voice:vrec --target vrec . && docker run --rm voice:vrec
FROM       base as vrec
WORKDIR    /app
ENTRYPOINT ["/bin/bash", "-cl", "python", "vrec.py"]

# docker build -t voice:app --target app . && docker run --rm voice:app
FROM       base as app
WORKDIR    /app
ENTRYPOINT ["/bin/bash", "-cl", "rasa shell"]
