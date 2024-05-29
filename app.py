from flask import Flask, render_template, request

app = Flask(__name__)


def determine_risk_level(total):
    if total <= 55:
        return "Low"
    elif 56 <= total <= 70:
        return "Medium"
    elif 71 <= total <= 85:
        return "High"
    elif total >= 86:
        return "Critical"


# New route for the documentation page
@app.route("/documentation")
def documentation():
    return render_template("documentation.html")


@app.route("/", methods=["GET", "POST"])
def index():
    # Initialize form data with default values
    form_data = {
        "traffic_flow": None,
        "data_type": None,
        "destination_source": None,
        "access_method": None,
        "compensating_controls": None,
        "rule_frequency": None,
    }

    if request.method == "POST":
        # Retrieve selected values from the form
        form_data = {
            "traffic_flow": request.form.get("traffic_flow"),
            "data_type": request.form.get("data_type"),
            "destination_source": request.form.get("destination_source"),
            "access_method": request.form.get("access_method"),
            "compensating_controls": request.form.get("compensating_controls"),
            "rule_frequency": request.form.get("rule_frequency"),
        }

        # Simple example of processing values - you can adjust this logic as needed
        total = sum(int(value) for value in form_data.values() if value)

        # Determine risk level
        risk_level = determine_risk_level(total)

        return render_template(
            "index.html", form_data=form_data, total=total, risk_level=risk_level
        )

    return render_template(
        "index.html", form_data=form_data, total=None, risk_level=None
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8989)
