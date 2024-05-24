FROM --platform=linux/amd64 python:3.10-slim-bullseye as build

# 필수 패키지 설치
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 설정
WORKDIR /usr/src

# requirements.txt 복사 및 설치
COPY requirements.txt ./
RUN pip install -r requirements.txt

# 전체 소스 코드 복사
COPY . .

# 포트 노출
EXPOSE 8000

# 컨테이너 시작 시 실행할 명령어
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
