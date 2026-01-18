const face = document.getElementById('face-container');

async function loadState() {
    try {
        const res = await fetch("http://127.0.0.1:8765/state");
        return await res.json();
    } catch {
        return {};
    }
}

async function tick() {
    const state = await loadState();
    updateFace(state);
}

setInterval(tick, 300);

/**
 * Updates the UI based on the JSON state object
 * @param {Object} state - The JSON object containing mode, focus, etc.
 */
function updateFace(state) {
    face.classList.remove("calm", "alert", "narrow", "sleep");

    // Storm off
    if (state.mode === "off") {
        face.classList.add("sleep");
        return;
    }

    // Enforcement mode (strict focus)
    if (state.mode === "enforce") {
        face.classList.add("narrow");
        return;
    }

    // Speaking → alert animation
    if (state.speaking) {
        face.classList.add("alert");
        return;
    }

    // Default presence → calm blinking
    face.classList.add("calm");
}


