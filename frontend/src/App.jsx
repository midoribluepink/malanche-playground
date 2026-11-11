import { useState } from "react";

function App() {
    const [comentario, setComentario] = useState("");
    const [opiniones, setOpiniones] = useState([]);

    async function obtenerOpiniones() {
        const respuesta = await fetch(
            "http://localhost:8000/api/opiniones/"
        );

        if (respuesta.ok) {
            const datos = await respuesta.json();
            setOpiniones(datos);
        } else {
            console.log("Error al obtener las opiniones");
        }
    }

    function enviarComentario() {
        if (comentario.trim() === "") {
            return;
        }

        setOpiniones([...opiniones, comentario]);
        setComentario("");
    }

    return (
        <div className="contenedor">
            <h1>RESEÑAS</h1>

            <h2>Escribe tu comentario</h2>

            <textarea
                placeholder="Escribe aquí tu opinión..."
                value={comentario}
                onChange={(e) => setComentario(e.target.value)}
            ></textarea>

            <button onClick={enviarComentario}>
                Enviar comentario
            </button>

            <h2>Opiniones</h2>

            {opiniones.map((opinion, indice) => (
                <p key={indice}>{opinion}</p>
            ))}
        </div>
    );
}

export default App;
