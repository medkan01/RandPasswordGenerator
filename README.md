# RandPasswordGenerator

A random password generator available as both a desktop application and a web service.

## Features

Generate secure random passwords with customizable options:
- **Lowercase letters** (a-z)
- **Uppercase letters** (A-Z)
- **Numbers** (0-9)
- **Symbols** (!@#$%...)
- **Adjustable length** (1-128 characters)

## Web Application (SaaS)

### Quick Start with Docker

```bash
# Clone the repository
git clone https://github.com/medkan01/RandPasswordGenerator.git
cd RandPasswordGenerator

# Start with Docker Compose
docker-compose up

# Access at http://localhost:8000
```

### Manual Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
cd api
uvicorn app:app --reload

# Access at http://localhost:8000
```

### API Endpoints

#### POST /api/generate
Generate a password with specified options.

```bash
curl -X POST http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -d '{"length": 16, "lowercase": true, "uppercase": true, "numbers": true, "symbols": true}'
```

#### GET /api/generate
Generate a password using query parameters.

```bash
curl "http://localhost:8000/api/generate?length=16&lowercase=true&uppercase=true"
```

## Desktop Application

The original desktop application uses PySimpleGUI.

```bash
# Install PySimpleGUI
pip install PySimpleGUI

# Run the application
python main.py
```

## Project Structure

```
RandPasswordGenerator/
├── api/                    # Web API
│   ├── app.py             # FastAPI application
│   └── password.py        # Password generation logic
├── static/                 # Web frontend
│   ├── index.html
│   ├── style.css
│   └── script.js
├── Model/                  # Desktop app model
├── View/                   # Desktop app view
├── Controller/             # Desktop app controller
├── main.py                # Desktop app entry point
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Deployment

### Docker

```bash
# Build the image
docker build -t password-generator .

# Run the container
docker run -p 8000:8000 password-generator
```

### Cloud Platforms

The Docker setup works with:
- **Railway** - `railway up`
- **Render** - Connect GitHub repo
- **Fly.io** - `fly launch`
- **Google Cloud Run** - `gcloud run deploy`

## License

MIT
