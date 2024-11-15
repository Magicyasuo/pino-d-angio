import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [series, setSeries] = useState([]); // Asegúrate de definir useState aquí

  useEffect(() => {
    axios.get(`${process.env.REACT_APP_API_BASE_URL}series/`)
      .then(response => {
        console.log("Datos recibidos:", response.data);
        setSeries(response.data); // Aquí usamos setSeries para actualizar el estado
      })
      .catch(error => {
        console.error('Error fetching series:', error);
      });
  }, []); // La dependencia vacía [] asegura que solo se ejecute una vez al montar el componente

  return (
    <div>
      <h1>Series Documentales</h1>
      <ul>
        {series.map(serie => (
          <li key={serie.id}>{serie.nombre}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;

