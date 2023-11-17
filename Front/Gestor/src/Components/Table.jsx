import React, { useState } from 'react';

function Table() {
    const [data, setData] = useState([]);

    const agregarFila = () => {
        const nuevaFila = {
            id: data.length + 1,
            terminado: false,
            actividad: '',
            fechaLimite: '',
        };

        setData([...data, nuevaFila]);
    };

    const handleChange = (id, campo, valor) => {
        setData((prevData) =>
            prevData.map((fila) =>
                fila.id === id ? { ...fila, [campo]: valor } : fila
            )
        );
    };

    return (
        <div className="container">
            <table>
                <thead>
                    <tr>
                        <th>Terminado</th>
                        <th>Actividad</th>
                        <th>Fecha limite</th>
                    </tr>
                </thead>
                <tbody>
                
          
                    {data.map((fila) => (
                        
                        <tr key={fila.id} >
                            <td>
                                <input
                                    type="checkbox"
                                    checked={fila.terminado}
                                    onChange={(e) =>
                                        handleChange(fila.id, 'terminado', e.target.checked)
                                    }
                                />
                            </td>
                            <td>
                                <input
                                    type="text"
                                    value={fila.actividad}
                                    onChange={(e) =>
                                        handleChange(fila.id, 'actividad', e.target.value)
                                    }
                                />
                            </td>
                            <td>
                                <input
                                    type="date"
                                    value={fila.fechaLimite}
                                    onChange={(e) =>
                                        handleChange(fila.id, 'fechaLimite', e.target.value)
                                    }
                                />
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
            <button className='btn' onClick={agregarFila}>Agregar Fila</button>
        </div>
    );
}

export default Table;
