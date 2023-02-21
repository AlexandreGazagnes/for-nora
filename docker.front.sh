#! /bin/sh




docker build -f ./Dockerfile.front -t for-nora-front:latest . &&  \
docker run -p 5000-5000 -ti for-nora-front:latest streamlit run run_front.py --server.port 5000  