import { useState } from 'react';

function CadastroUsuario() {
  // 1. Criando os estados para guardar o que o usuário digita
  const [nome, setNome] = useState('');
  const [cnpj, setCnpj] = useState('');
  const [email, setEmail] = useState('');
  const [celular, setCelular] = useState('');
  const [senha, setSenha] = useState('');

  // 2. Função que roda quando o usuário clica em "Cadastrar"
  const handleSubmit = async (e) => {
    e.preventDefault(); // Evita que a página recarregue do zero

    // Cria o objeto exatamente com as chaves que o Python espera
    const dadosUsuario = {
      nome: nome,
      cnpj: cnpj,
      email: email,
      celular: celular,
      senha: senha
    };

    try {
      // Faz o disparo POST para a API Flask rodando no Docker
      const resposta = await fetch('http://localhost:5000/user', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(dadosUsuario),
      });

      const dados = await resposta.json();

      if (resposta.ok) {
        alert(dados.mensagem); // "User salvo com sucesso"
        localStorage.setItem('cnpjAtivacao', cnpj);
        
        // Opcional: Limpar os campos após o sucesso
        setNome('');
        setCnpj('');
        setEmail('');
        setCelular('');
        setSenha('');
      } else {
        alert(`Erro: ${dados.erro || 'Falha ao cadastrar'}`);
      }
    } catch (erro) {
      console.error('Erro de conexão:', erro);
      alert('Não foi possível conectar com o servidor. Verifique se o backend está rodando e se o CORS está configurado.');
    }
  };

  // 3. O visual do formulário (HTML/JSX)
  return (
    <div style={{ maxWidth: '400px', margin: '50px auto', fontFamily: 'sans-serif' }}>
      <h2>Cadastro de Vendedor</h2>
      
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
        
        <div>
          <label>Nome Completo:</label>
          <input 
            type="text" 
            value={nome} 
            onChange={(e) => setNome(e.target.value)} 
            required 
            style={{ width: '100%', padding: '8px', marginTop: '5px' }}
          />
        </div>

        <div>
          <label>CNPJ:</label>
          <input 
            type="text" 
            value={cnpj} 
            onChange={(e) => setCnpj(e.target.value)} 
            required 
            style={{ width: '100%', padding: '8px', marginTop: '5px' }}
          />
        </div>

        <div>
          <label>E-mail:</label>
          <input 
            type="email" 
            value={email} 
            onChange={(e) => setEmail(e.target.value)} 
            required 
            style={{ width: '100%', padding: '8px', marginTop: '5px' }}
          />
        </div>

        <div>
          <label>Celular (WhatsApp):</label>
          <input 
            type="text" 
            value={celular} 
            onChange={(e) => setCelular(e.target.value)} 
            required 
            style={{ width: '100%', padding: '8px', marginTop: '5px' }}
          />
        </div>

        <div>
          <label>Senha:</label>
          <input 
            type="password" 
            value={senha} 
            onChange={(e) => setSenha(e.target.value)} 
            required 
            style={{ width: '100%', padding: '8px', marginTop: '5px' }}
          />
        </div>

        <button 
          type="submit" 
          style={{ padding: '10px', backgroundColor: '#007bff', color: 'white', border: 'none', cursor: 'pointer', fontSize: '16px' }}
        >
          Cadastrar
        </button>

      </form>
    </div>
  );
}

export default CadastroUsuario;