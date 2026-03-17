import React, { useState } from 'react';

function ValidacaoCodigo() {
  const [codigo, setCodigo] = useState('');
  const [mensagem, setMensagem] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    setMensagem('Validando...'); // Feedback visual rápido para o usuário

    // 1. Resgata o CNPJ que salvamos na memória na tela de cadastro
    const cnpjSalvo = localStorage.getItem('cnpjAtivacao');

    // Se a pessoa cair nessa tela de paraquedas sem ter cadastrado antes:
    if (!cnpjSalvo) {
      setMensagem('Erro: Nenhum CNPJ encontrado. Por favor, faça o cadastro primeiro.');
      return;
    }

    try {
      // 2. Faz a requisição POST para a sua API Python
      const resposta = await fetch('http://localhost:5000/user/activate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          cnpj: cnpjSalvo,
          activation_code: codigo
        }),
      });

      const dados = await resposta.json();

      // 3. Trata a resposta com base no que o Python devolveu
      if (resposta.ok) {
        setMensagem('Código validado com sucesso! Conta ativada.');
        // Limpa a memória pois já ativamos com sucesso
        localStorage.removeItem('cnpjAtivacao'); 
      } else {
        // Mostra o erro exato que veio do seu back-end ou um erro genérico
        setMensagem(`Erro: ${dados.erro || 'Código inválido. Tente novamente.'}`);
      }
    } catch (erro) {
      console.error('Erro de conexão:', erro);
      setMensagem('Erro de conexão com o servidor. O backend está rodando?');
    }
  };

  return (
    <div style={{ padding: '20px', border: '1px solid #ccc', borderRadius: '8px', maxWidth: '400px', margin: '20px auto', fontFamily: 'sans-serif' }}>
      <h2 style={{ textAlign: 'center' }}>Validar Código</h2>
      <p style={{ textAlign: 'center' }}>Digite o código enviado para o seu WhatsApp.</p>
      
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
        <div>
          <label htmlFor="codigo" style={{ display: 'block', marginBottom: '5px' }}>Código de Validação:</label>
          <input
            type="text"
            id="codigo"
            value={codigo}
            onChange={(e) => setCodigo(e.target.value)}
            maxLength="6" // Se o código do banco de dados na sua imagem era 3965, você pode ajustar para "4" se for sempre 4 dígitos
            style={{ width: '100%', padding: '10px', boxSizing: 'border-box', textAlign: 'center', fontSize: '20px', letterSpacing: '4px' }}
            required
          />
        </div>
        <button type="submit" style={{ padding: '12px', background: '#007bff', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer', fontSize: '16px', fontWeight: 'bold' }}>
          Validar Código
        </button>
      </form>

      {mensagem && (
        <p style={{ marginTop: '15px', fontWeight: 'bold', textAlign: 'center', color: mensagem.includes('sucesso') ? 'green' : 'red' }}>
          {mensagem}
        </p>
      )}
    </div>
  );
}

export default ValidacaoCodigo;