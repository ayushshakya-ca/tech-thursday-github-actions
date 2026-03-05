from flask import Flask, jsonify, render_template
import os
import time
import threading

app = Flask(__name__)

# =========================
# APPLICATION READINESS FLAG
# =========================
app_ready = False
# Optional flag to force health check failure
#FORCE_FAIL_HEALTH = os.environ.get("FORCE_FAIL_HEALTH", "false").lower() == "false"


def initialize_application():
    """
    Simulate startup tasks like:
    - DB connection
    - Cache warmup
    - External API validation
    Replace sleep with real checks in production.
    """
    global app_ready
    print("Initializing application...")

    time.sleep(250)  # simulate startup delay

    app_ready = True
    print("Application is now HEALTHY")


# Run initialization in background
threading.Thread(target=initialize_application, daemon=True).start()


# =========================
# HEALTH ENDPOINT
# =========================
@app.route("/health", methods=["GET"], strict_slashes=False)
def health():
    if app_ready:
        return jsonify(status="healthy"), 200
    else:
        return jsonify(status="starting"), 503


# =========================
# MAIN ROUTE
# =========================
@app.route("/")
def home():
    return render_template("index.html")


# =========================
# APPLICATION START
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
