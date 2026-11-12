import { useState, useEffect } from "react";

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
        obtenerOpiniones();
    }, []);

   /* function enviarComentario() {
        if (comentario.trim() === "") {
            return;
        }

        setOpiniones([...opiniones, comentario]);
        setComentario("");
    }
*/ 
    return (
        <div className="contenedor">
            <h1>RESEÑAS</h1>

            <h2>Escribe tu comentario</h2>

            <textarea
                placeholder="Escribe aquí tu opinión..."
                value={comentario}
                onChange={(e) => setComentario(e.target.value)}
            ></textarea>

            <button >
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
