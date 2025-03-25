# Survey App

A Flask-based web application to collect and analyze income/spending data, with MongoDB storage and AWS deployment capabilities.

## Features

- **User Survey**: Collects comprehensive demographic and financial data including age, gender, income, and expenses
- **Data Storage**: Robust MongoDB integration for secure and scalable data persistence
- **Data Processing**: Seamless data export functionality to CSV for advanced analysis
- **Visualization**: Interactive charts visualizing key insights like age vs. income and gender spending distribution
- **Deployment**: Fully configured for straightforward AWS cloud hosting

## Prerequisites

- Python 3.8+
- MongoDB (local installation or MongoDB Atlas)
- AWS account (optional, for cloud deployment)

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/healthcare-survey-tool.git
cd healthcare-survey-tool
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root with the following configuration:

```
MONGODB_USERNAME=your_username
MONGODB_PASSWORD=your_password
MONGODB_HOST=localhost      # For local MongoDB
MONGODB_PORT=27017          # Default MongoDB port
```

### 4. Set Up MongoDB

#### Local MongoDB

Ensure the MongoDB service is running:

```bash
# Linux
sudo systemctl start mongod

# Windows
net start MongoDB
```

#### MongoDB Atlas

Replace the `.env` file with your Atlas connection URI:

```
MONGODB_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/survey_db
```

## Usage

### 1. Run the Flask App

```bash
python app.py
```

Access the survey at: `http://localhost:5000`

### 2. Process Data

Generate a CSV from MongoDB:

```bash
python process_data.py
```

### 3. Analyze Data with Jupyter Notebook

Launch Jupyter:

```bash
jupyter notebook
```

Open `analysis.ipynb` to view and interact with data visualizations.

## Deployment to AWS

### 1. Launch an EC2 Instance

- **AMI**: Ubuntu 22.04 LTS
- **Security Group**: Allow HTTP (80), HTTPS (443), and SSH (22)

### 2. Deploy the Application

```bash
# SSH into the instance
ssh -i "your-key.pem" ubuntu@ec2-ip-address

# Clone and set up project
git clone https://github.com/yourusername/healthcare-survey-tool.git
cd healthcare-survey-tool
pip install -r requirements.txt

# Run with Gunicorn
gunicorn app:app -b 0.0.0.0:80
```

### 3. Set Up Persistence (Optional)

Create a systemd service:

```bash
sudo nano /etc/systemd/system/survey.service
```

Add the following configuration:

```ini
[Unit]
Description=Healthcare Survey App
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/healthcare-survey-tool
ExecStart=/usr/bin/gunicorn app:app -b 0.0.0.0:80
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

```bash
sudo systemctl start survey
sudo systemctl enable survey
```

## Project Structure

```
healthcare-survey-tool/
├── app.py                # Flask application
├── process_data.py       # Data processing script
├── analysis.ipynb        # Jupyter notebook for visualization
├── templates/
│   └── survey.html       # Styled survey form
├── .env                  # Environment variables
└── requirements.txt      # Dependencies
```

## Troubleshooting

- **MongoDB Connection Issues**: Verify credentials in `.env` and ensure MongoDB is running
- **Form Not Submitting**: Check Flask logs for errors (use `app.py` debug mode)
- **AWS Deployment**: Confirm security groups allow traffic on port 80

## License

MIT License