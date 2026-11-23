import { useState } from "react";

function RegistroClientes() {

    const [nombre, setNombre] = useState("");
    const [apellidos, setApellidos] = useState("");
    const [telefono, setTelefono] = useState("");
    const [fechaRegistro, setFechaRegistro] = useState("");
    const [mensaje, setMensaje] = useState("");

    async function registrarCliente(evento) {
        evento.preventDefault();
        if (
            nombre.trim() === "" ||
            apellidos.trim() === "" ||
            telefono.trim() === "" ||
            fechaRegistro === ""
        ) {
        setMensaje("Debes completar todos los campos");
        return;
    }
        setMensaje("");

        const cliente = {
            nombre: nombre,
            apellido: apellidos,
            telefono: telefono,
            fecha_registro: fechaRegistro
        };

        try {
            const respuesta = await fetch(
                "http://localhost:8000/clientes/",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(cliente)
                }
            );

            if (respuesta.ok) {

                const datos = await respuesta.json();

                console.log(datos);

                setNombre("");
                setApellidos("");
                setTelefono("");
                setFechaRegistro("");
                                
            } else {
                console.log("Error HTTP:", respuesta.status);
            }

            

        } catch (error) {
            console.log("Error al registrar el cliente:", error);
        }
    

        
    }



    return (
        <div>
            <h1>Registro de clientes</h1>

            <form onSubmit={registrarCliente}>
                <label>Nombre:</label>
                <input 
                    type="text"
                    value={nombre}
                    onChange={(e) => setNombre(e.target.value)} 
                />

                <label>Apellidos:</label>
                <input 
                    type="text" 
                    value={apellidos}
                    onChange={(e) => setApellidos(e.target.value)}
                />

                <label>Teléfono:</label>
                <input 
                    type="tel"
                    value={telefono}
                    onChange={(e) => setTelefono(e.target.value)} 
                />

                <label>Fecha de registro:</label>
                <input 
                    type="date"
                    value={fechaRegistro}
                    onChange={(e) => setFechaRegistro(e.target.value)}
                />

                <button type="submit">Registrar cliente</button>
            </form>

             <p>{mensaje}</p>
</div>
        
    );
}

export default RegistroClientes;