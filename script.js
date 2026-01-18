console.log("Script loaded");

function predictEnergy() {
    console.log("Predict clicked");

    const building = document.getElementById("building");
    const square = document.getElementById("sqft");
    const occupants = document.getElementById("occupants");
    const appliances = document.getElementById("appliances");
    const temperature = document.getElementById("temp");
    const day = document.getElementById("day");
    const result = document.getElementById("result");

    
    console.log(building, square, occupants, appliances, temperature, day);

    if (!building || !square || !occupants || !appliances || !temperature || !day) {
        result.innerText = "HTML ID mismatch error ❌";
        return;
    }

    fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
        buildingType: building.value,
        squareFootage: square.value,
        occupants: occupants.value,
        appliances: appliances.value,
        temperature: temperature.value,
        day: day.value
    })
})
.then(res => res.json())
.then(data => {
    if (data.prediction) {
        result.innerText = "Predicted Energy: " + data.prediction + " kWh";
    } else {
        result.innerText = "Error: " + data.error;
    }
})
.catch(err => {
    console.error(err);
    result.innerText = "Prediction failed ❌";
})};