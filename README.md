# Raspberry Pi FastAPI Monitor

A web-based monitoring application built with FastAPI that tracks your Raspberry Pi's hardware status, including CPU temperature and uptime. The application connects to your Raspberry Pi via SSH, collects real-time data, stores it in a local SQLite database, and displays it on a responsive web dashboard.

## Features

- **Real-time Monitoring**: Automatically collects CPU temperature and system uptime every 5 seconds
- **Web Dashboard**: Clean, responsive web interface with auto-refresh
- **Data Persistence**: Stores all readings in a SQLite database with timestamps
- **SSH Connectivity**: Secure remote monitoring via SSH (requires sshpass)
- **FastAPI Backend**: Modern, fast web framework with automatic API documentation

## Prerequisites

- Python 3.8+
- Raspberry Pi with SSH access enabled
- `sshpass` installed on the monitoring machine (for password-based SSH authentication)
- Network connectivity between the monitoring machine and Raspberry Pi

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Raspberry-Pi-FastAPI-monitor.git
   cd Raspberry-Pi-FastAPI-monitor
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn sqlalchemy jinja2 python-multipart
   ```

4. **Install sshpass (Linux/macOS):**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install sshpass

   # macOS with Homebrew
   brew install hudochenkov/sshpass/sshpass
   ```

## Configuration

Before running the application, configure your Raspberry Pi connection details in `pi_data/hardware_monitor.py`:

```python
pi_user = "your_pi_username"
pi_pass = "your_pi_password"
pi_ip = "your_pi_ip_address"
```

**Security Note:** Consider using SSH key authentication instead of passwords for production use.

## Running the Application

1. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate
   ```

2. **Start the FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```

3. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:8000
   ```

The dashboard will automatically refresh every 5 seconds to show the latest readings.

## API Documentation

When the server is running, you can access the automatic API documentation at:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Database

The application uses SQLite (`raspberryPi.db`) to store monitoring data. The database schema includes:

- `temp`: CPU temperature in Celsius (Float)
- `uptime`: System uptime as formatted string
- `timeStamp`: Automatic timestamp when data was recorded

## Project Structure

```
Raspberry-Pi-FastAPI-monitor/
├── main.py                 # FastAPI application and routes
├── models.py              # SQLAlchemy database models
├── schemas.py             # Pydantic data validation schemas
├── database.py            # Database configuration
├── pi_data/
│   ├── __init__.py
│   └── hardware_monitor.py # Raspberry Pi data collection
├── static/
│   └── style.css          # CSS styling
├── templates/
│   └── home.html          # Jinja2 template
└── README.md
```

## Troubleshooting

- **Connection Issues**: Ensure your Raspberry Pi is reachable via SSH and the credentials are correct
- **Permission Errors**: Make sure the SSH user has access to `/sys/class/hwmon/` and `/proc/uptime`
- **Missing Dependencies**: Install all required Python packages and system tools

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
