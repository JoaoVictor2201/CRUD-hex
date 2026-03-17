// src/App.js
import React from 'react';
import './App.css';
import CadastroUsuario from './components/CadastroUsuario';
import ValidacaoCodigo from './components/ValidacaoCodigo';

function App() {
  return (
    <div className="App">
      <h1 style={{ textAlign: 'center' }}>Nosso Mercado - Cadastro</h1>
      <main>
        {/* Exibe ambos os componentes na mesma página para teste inicial */}
        <CadastroUsuario />
        <hr /> {/* Uma linha divisória */}
        <ValidacaoCodigo />
      </main>
    </div>
  );
}

export default App;