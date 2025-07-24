# Flask K8S Application

A simple Flask web application designed for Kubernetes deployment with Docker containerization.

## 🚀 Features

- **Flask Web Framework**: Lightweight and efficient Python web framework
- **CORS Support**: Cross-origin requests enabled for frontend integration
- **Docker Ready**: Fully containerized with optimized Dockerfile
- **Kubernetes Compatible**: Multiple deployment options (Pod and Deployment)
- **Resource Management**: CPU and memory limits configured
- **Production Ready**: Proper logging and error handling

## 📋 Prerequisites

- Python 3.11+
- Docker (for containerization)
- Kubernetes cluster (minikube, Docker Desktop, or cloud provider)
- kubectl CLI tool

## 🛠️ Installation & Setup

### Local Development

1. **Clone the repository**:
```bash
git clone https://github.com/Omarben05/K8SAppSWD.git
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
docker build -t k8sappswd:v1 .
```

2. **Run the container**:
```bash
docker run -p 5000:5000 k8sappswd:v1
```

### Kubernetes Deployment

#### Option 1: Single Pod Deployment
```bash
kubectl apply -f pod.yaml
```

#### Option 2: Deployment with Replicas (Recommended)
```bash
kubectl apply -f deployment.yaml
```

#### Option 3: Complete Deployment with Service
```bash
# Deploy the application
kubectl apply -f deployment.yaml

# Create service to expose the application
kubectl apply -f service.yaml
```

#### Validate Before Deployment (Recommended)
```bash
# Dry-run validation for deployment
kubectl apply -f deployment.yaml --dry-run=client -o yaml

# Dry-run validation for service
kubectl apply -f service.yaml --dry-run=client -o yaml

# Validate YAML syntax
kubectl apply -f deployment.yaml --validate=true --dry-run=client
kubectl apply -f service.yaml --validate=true --dry-run=client

# Check what would be created without actually creating
kubectl create -f deployment.yaml --dry-run=client
kubectl create -f service.yaml --dry-run=client
```

#### Verify Deployment
```bash
# Check pods status
kubectl get pods

# Check deployment status (if using deployment.yaml)
kubectl get deployments

# Check service status
kubectl get services

# View application logs
kubectl logs <pod-name>

# Access the application (if using minikube)
minikube service k8sappswd-service
```

## 📡 API Endpoints

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| GET    | `/`      | Returns a JSON greeting message | `{"message": "Ciao da k8s!"}` |
| GET    | `/hostname` | Returns hostname and custom message | `{"hostname": "pod-name", "message": "hello from k8s"}` |

### Response Examples

#### Root Endpoint (`/`)
```json
{
  "message": "Ciao da k8s!"
}
```

#### Hostname Endpoint (`/hostname`)
```json
{
  "hostname": "demo-k9sappswd-pod",
  "message": "hello from k8s"
}
```

*Note: The hostname will show the actual pod name when running in Kubernetes, making it useful for identifying which pod is responding in a multi-replica deployment.*

## 🏗️ Project Structure

```
K8SAppSWD/
├── app.py              # Main Flask application with CORS
├── requirements.txt    # Python dependencies (Flask, Flask-CORS)
├── Dockerfile         # Docker configuration with Python 3.11-slim
├── pod.yaml           # Kubernetes Pod configuration
├── deployment.yaml    # Kubernetes Deployment with replicas and resources
├── service.yaml       # Kubernetes Service to expose the application
├── .gitignore         # Git ignore rules for Python projects
├── LICENSE           # MIT License
└── README.md         # Project documentation
```

## 🔧 Configuration

### Docker Image
- **Base Image**: `python:3.11-slim`
- **Port**: 5000
- **Working Directory**: `/app`

### Environment Variables
- **MESSAGE**: Custom message for the `/hostname` endpoint (default: "hello from k8s")

### Kubernetes Resources
- **Pod**: Single instance deployment
- **Deployment**: 2 replicas with resource limits
  - Memory: 64Mi (request) / 128Mi (limit)
  - CPU: 250m (request) / 500m (limit)
- **Service**: Exposes the application internally/externally
  - Type: LoadBalancer or NodePort
  - Port: 80 (external) → 5000 (internal)

## 🚀 Deployment Commands

```bash
# Build and tag Docker image
docker build -t k8sappswd:v1 .

# Validate configurations before deployment
kubectl apply -f deployment.yaml --dry-run=client --validate=true
kubectl apply -f service.yaml --dry-run=client --validate=true

# Deploy complete application stack
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Scale deployment (useful to test hostname endpoint with multiple pods)
kubectl scale deployment k8sappswd-deployment --replicas=3

# Update deployment with custom environment variable
kubectl set env deployment/k8sappswd-deployment MESSAGE="Custom message from K8s"

# Get service URL (minikube)
minikube service k8sappswd-service --url

# Validate running resources
kubectl get all -l app=k8sappswddeployment

# Test connectivity
kubectl port-forward deployment/k8sappswd-deployment 8080:5000

# Test hostname endpoint (shows which pod responds)
curl <service-url>/hostname

# Delete complete deployment
kubectl delete -f service.yaml
kubectl delete -f deployment.yaml
```

## 🔍 Troubleshooting

### Validation Commands
```bash
# Check YAML syntax
kubectl apply -f deployment.yaml --dry-run=client -o yaml
kubectl apply -f service.yaml --dry-run=client -o yaml

# Validate against cluster
kubectl apply -f deployment.yaml --server-dry-run
kubectl apply -f service.yaml --server-dry-run

# Describe resources for debugging
kubectl describe deployment k8sappswd-deployment
kubectl describe service k8sappswd-service
kubectl describe pods -l app=k8sappswddeployment

# Check events
kubectl get events --sort-by=.metadata.creationTimestamp
```

### Testing Multiple Replicas
```bash
# Scale to multiple replicas
kubectl scale deployment k8sappswd-deployment --replicas=3

# Test which pod responds (hostname will vary)
kubectl port-forward deployment/k8sappswd-deployment 8080:5000
curl http://localhost:8080/hostname

# Watch pods to see different hostnames
kubectl get pods -l app=k8sappswddeployment -w
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

**Omar Benagoub**
- GitHub: [@Omarben05](https://github.com/Omarben05)

## 🙏 Acknowledgments

- Flask community for the excellent web framework
- Kubernetes for container orchestration platform
- Docker for containerization technology

## 📚 Learn More

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Docker Documentation](https://docs.docker.com/)
