# Ujimaru API

### Build

```
docker build -t ujimaru-api .
```

### Run locally

```
docker run -e PORT=8000 -p 8000:8000 ujimaru-api
```

### Deploy

```
gcloud builds submit --tag gcr.io/ujimaru-api/api --project ujimaru-api
```