let myChart = null;

async function analyzeDecision() {
    const dream = document.getElementById("dreamJob").value || "your goal";
    const dId = document.getElementById("decisionSelect").value;
    const freq = document.getElementById("frequency").value || 1;
    const time = document.getElementById("timePeriod").value || 30;

    const response = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ decision_id: dId, frequency: freq, time_period: time })
    });

    const data = await response.json();
    document.getElementById("resultSection").classList.remove("hidden");

    const isGood = data.intensity > 0;
    let percentage = isGood ? Math.min(99, 45 + (data.intensity/5)) : Math.max(1, 45 + (data.intensity/5));
    
    // UI Update
    document.getElementById("percentVal").innerText = percentage.toFixed(0);
    document.getElementById("hScore").innerText = data.butterfly_effect.health;
    document.getElementById("fScore").innerText = data.butterfly_effect.focus;
    document.getElementById("cScore").innerText = data.butterfly_effect.career;

    // Verdict logic
    let verdict = isGood ? `🚀 Amazing! To become a ${dream}, this habit is perfect.` : `❌ Careful! This will stop you from becoming a ${dream}.`;
    document.getElementById("adviceText").innerText = verdict;

    // Chart Update
    const ctx = document.getElementById("impactChart").getContext('2d');
    if (myChart) myChart.destroy();
    myChart = new Chart(ctx, {
        type: "line",
        data: {
            labels: ["Start", "Middle", "End"],
            datasets: [{
                label: "Trajectory",
                data: [0, data.intensity/2, data.intensity],
                borderColor: isGood ? '#4ade80' : '#f87171', // Green or Red
                backgroundColor: isGood ? 'rgba(74, 222, 128, 0.1)' : 'rgba(248, 113, 113, 0.1)',
                fill: true, tension: 0.4
            }]
        }
    });
}