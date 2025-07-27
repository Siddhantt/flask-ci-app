from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Simple HTML calculator form
HTML_FORM = '''
<!DOCTYPE html>
<html>
<head>
    <title>Calculator</title>
</head>
<body>
    <h2>Calculator App</h2>
    <form method="post" action="/calculate-form">
        <input type="number" name="a" placeholder="Enter A" step="any" required>
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">−</option>
            <option value="multiply">×</option>
            <option value="divide">÷</option>
        </select>
        <input type="number" name="b" placeholder="Enter B" step="any" required>
        <button type="submit">Calculate</button>
    </form>
    {% if result is not none %}
        <h3>Result: {{ result }}</h3>
    {% elif error %}
        <h3 style="color:red;">{{ error }}</h3>
    {% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_FORM, result=None, error=None)

@app.route("/calculate-form", methods=["POST"])
def calculate_form():
    try:
        a = float(request.form["a"])
        b = float(request.form["b"])
        operation = request.form["operation"]

        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            if b == 0:
                raise ValueError("Division by zero")
            result = a / b
        else:
            raise ValueError("Invalid operation")

        return render_template_string(HTML_FORM, result=result, error=None)

    except Exception as e:
        return render_template_string(HTML_FORM, result=None, error=str(e))

@app.route("/calculate", methods=["POST"])
def calculate_api():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    operation = data.get("operation")

    try:
        a = float(a)
        b = float(b)
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Must be numbers."}), 400

    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return jsonify({"error": "Division by zero"}), 400
        result = a / b
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
