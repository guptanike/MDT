from flask import Flask, request, jsonify
from flask_cors import CORS

# ChatGPT Logic directly here to avoid ImportErrors
def calculate_impact(decision_id):
    impact_map = {
        "D1": {"health": -3, "focus": -4, "career": -2},
        "D2": {"health": -1, "focus": -3, "career": -4},
        "D3": {"health": -2, "focus": -4, "career": -3},
        "G1": {"health": 3, "focus": 2, "career": 1},
        "G2": {"health": 1, "focus": 3, "career": 3},
        "G4": {"health": 4, "focus": 2, "career": 1}
    }
    return impact_map.get(decision_id, {"health": 0, "focus": 0, "career": 0})

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.json
        d_id = data.get("decision_id")
        freq = int(data.get("frequency", 1))
        time = int(data.get("time_period", 30))

        impact = calculate_impact(d_id)
        intensity = (impact['health'] + impact['focus'] + impact['career']) * freq * time
        
        pattern = "Positive Growth Loop" if intensity > 0 else "Negative Habit Loop"
        
        return jsonify({
            "pattern": pattern,
            "intensity": intensity,
            "butterfly_effect": impact
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)