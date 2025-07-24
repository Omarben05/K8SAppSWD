# Flask K8S Application

A simple Flask web application designed for Kubernetes deployment.

## 🚀 Features

- **Flask Web Framework**: Lightweight and efficient
- **CORS Support**: Cross-origin requests enabled
- **Docker Ready**: Containerized for easy deployment
- **Kubernetes Compatible**: Ready for K8s orchestration

## 📋 Prerequisites

- Python 3.11+
- Docker (optional)
- Kubernetes cluster (for K8s deployment)

## 🛠️ Installation & Setup

### Local Development

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/K8SAppSWD.git
cd K8SAppSWD
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Run the application**:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Docker Deployment

1. **Build the Docker image**:
```bash
docker build -t flask-k8s-app .
```

2. **Run the container**:
```bash
docker run -p 5000:5000 flask-k8s-app
```

### Kubernetes Deployment

```bash
kubectl apply -f k8s-deployment.yaml
```

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/`      | Returns a JSON greeting message |

### Response Example
```json
{
  "message": "Ciao da k8s!"
}
```

## 🏗️ Project Structure

```
K8SAppSWD/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── k8s-deployment.yaml # Kubernetes deployment
├── .gitignore         # Git ignore rules
└── README.md          # Project documentation
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Omar Benagoub

## 🙏 Acknowledgments

- Flask community for the excellent framework
- Kubernetes for container orchestration
