import { useState, useEffect } from "react";

function obtenerCookie(nombre) {
    const cookies = document.cookie.split(";");

    for (const cookie of cookies) {
        const [clave, ...valor] = cookie.trim().split("=");

        if (clave === nombre) {
            return decodeURIComponent(valor.join("="));
        }
    }

    return null;
}

function App() {
    const [comentario, setComentario] = useState("");
    const [opiniones, setOpiniones] = useState([]);

    async function obtenerOpiniones() {
        try{
            const respuesta = await fetch(
                "http://localhost:8000/comentarios/"
            );

            if (respuesta.ok) {
                const datos = await respuesta.json();
                if (Array.isArray(datos)){
                    setOpiniones(datos);
                } else {
                    console.log("La respuesta no contiene una lista de opiniones");
                }
            } else {
                console.log("Error HTTP:", respuesta.status);
            }
            
        } catch(error){
            console.log("Error al procesar la respuesta", error);
        }
    }
       
    useEffect(() => {
        async function inicializar() {
            try {
                await fetch("http://localhost:8000/csrf/", {
                    credentials: "include"
                });

                await obtenerOpiniones();
            } catch (error) {
                console.log("Error al obtener CSRF:", error);
            }
        }

        inicializar();
}, []); 

async function enviarComentario() {
    if (comentario.trim() === "") {
        return;
    }

    try {
        const csrfToken = obtenerCookie("csrftoken");

        if (!csrfToken) {
            console.log("No se encontró el token CSRF");
            return;
        }

        const respuesta = await fetch(
            "http://localhost:8000/comentarios/",
            {
                method: "POST",
                credentials: "include",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken
                },
                body: JSON.stringify({
                    texto: comentario
                })
            }
        );

        if (respuesta.ok) {
            const datos = await respuesta.json();

            setOpiniones((anteriores) => [...anteriores, datos]);
            setComentario("");
        } else {
            console.log("Error HTTP:", respuesta.status);
        }

    } catch (error) {
        console.log("Error al enviar el comentario:", error);
    }
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

            {opiniones.map((opinion) => (
                <p key={opinion.id}>{opinion.texto}</p>
            ))}
        </div>
    );
}

export default App;
