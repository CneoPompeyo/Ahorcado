async function startGame() {
    const palabra = document.getElementById("palabra").value;
    const response = await fetch("/start", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ palabra: palabra }),
    });
    const data = await response.json();
    if (response.ok) {
        document.getElementById("start-screen").style.display = "none";
        document.getElementById("game-screen").style.display = "block";
        document.getElementById("palabra-escondida").innerText = data.palabra;
    } else {
        alert(data.message);
    }
}

async function adivinarLetra() {
    const letra = document.getElementById("letra").value;
    const response = await fetch("/guess_letter", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ letra: letra }),
    });
    const data = await response.json();
    if (response.ok) {
        document.getElementById("palabra-escondida").innerText = data.palabra;
        document.getElementById("vidas").innerText = `Vidas restantes: ${data.vidas}`;
        document.getElementById("letras-usadas").innerText = `Letras usadas: ${data.letrasUsadas.join(", ")}`;
        document.getElementById("mensaje").innerText = data.message;
        // Deshabilitar inputs y botones si el juego termina
        if (data.message === "GANASTE" || data.message === "PERDISTE") {
            disableInputs();
        }
    } else {
        alert(data.message);
    }
    document.getElementById("letra").value = "";
}

async function adivinarPalabra() {
    const palabra = document.getElementById("palabra-completa").value;
    const response = await fetch("/guess_word", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ palabra: palabra }),
    });
    const data = await response.json();
    if (response.ok) {
        document.getElementById("mensaje").innerText = data.message;
        // Deshabilitar inputs y botones si el juego termina
        if (data.message === "GANASTE" || data.message === "PERDISTE") {
            disableInputs();
        }
    } else {
        alert(data.message);
    }
    document.getElementById("palabra-completa").value = "";
}

async function resetGame() {
    const response = await fetch("/reset", { method: "POST" });
    const data = await response.json();
    if (response.ok) {
        window.location.reload();
    } else {
        alert(data.message);
    }
}

function disableInputs() {
    document.getElementById("letra").disabled = true;
    document.getElementById("palabra-completa").disabled = true;
    document.querySelector("button[onclick='adivinarLetra()']").disabled = true;
    document.querySelector("button[onclick='adivinarPalabra()']").disabled = true;
}
