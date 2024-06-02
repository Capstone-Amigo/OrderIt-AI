# 캡스톤 디자인 AI part
---

2024년 캡스톤디자인 AI part입니다. 크게 2가지로 나뉩니다. 
- API
- AI Training, Build Dataset

<br>

## API
---

### 사용 기술 스택
- Docker
- Flask
- GCP(Google Cloud Platform)

### 구현 과정
1. GCP에서 VM 인스턴스 생성
2. Docker를 이용해 컨테이너를 생성
3. Flask로 API 배포

## AI
---

### 사용 기술 스택
- PyTorch
- PyTorch Lightning

### 구현과정

1. Hugging Face에서 ko-en 쌍으로 훈련되어있는 KoBART모델을 Base로 함.
2. KoBART모델을 자체 생성한 데이터셋으로 Fine-tuning 진행
3. wandb를 통해 Training Loss 확인하며 Fine-tuning 진행
4. Loss가 가장 괜찮은 모델을 선택하여 github에 업로드

