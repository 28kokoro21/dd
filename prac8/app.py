from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Define Prometheus counter
REQUEST_COUNT = Counter(
    "api_request_total",
    "Total number of API requests"
)

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "Hello"

@app.route("/hello")
def hello():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)



# yaml
global:
  scrape_interval: 5s

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  - job_name: "python-app"
    static_configs:
      - targets: ["localhost:8000"]

  - job_name: "windows"
    static_configs:
      - targets: ["localhost:9182"]

