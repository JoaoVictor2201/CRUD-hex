import { useState } from 'react';

const Login = ({ onLoginSuccess }) => {
  const [cnpj, setCnpj] = useState('');
  const [password, setPassword] = useState('');
  const [mensagem, setMensagem] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          cnpj: cnpj,
          password: password,
        }),
      });

      const data = await response.json();

      if (response.ok) {
        setMensagem('Login realizado com sucesso!');
        localStorage.setItem('token', data.token);

        if (onLoginSuccess) {
            onLoginSuccess(data.nome);
        }
        
        console.log("Token salvo:", data.token);
      } else {
        setMensagem(data.erro || 'Erro ao fazer login.');
      }
    } catch (error) {
      setMensagem('Erro de conexão com o servidor.');
      console.error("Erro:", error);
    }
  };

  return (
    <div style={{ maxWidth: '400px', margin: '20px auto 50px', padding: '20px', borderRadius: '8px' }}>
      
      <form onSubmit={handleLogin} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
        
        <div className=''>
          <label>CNPJ:</label>
          <input 
            type="text" 
            value={cnpj} 
            onChange={(e) => setCnpj(e.target.value)} 
            placeholder="00.000.000/0001-00"
            required 
            style={{ width: '100%', padding: '8px' }}
          />
        </div>

        <div>
          <label>Senha:</label>
          <input 
            type="password" 
            value={password} 
            onChange={(e) => setPassword(e.target.value)} 
            placeholder="Sua senha"
            required 
            style={{ width: '100%', padding: '8px' }}
          />
        </div>

        <button type="submit" style={{ padding: '10px', backgroundColor: '#007BFF', color: '#FFF', border: 'none', cursor: 'pointer' }}>
          Entrar
        </button>
      </form>

      {mensagem && <p style={{ marginTop: '15px', color: mensagem.includes('sucesso') ? 'green' : 'red' }}>{mensagem}</p>}
    </div>
  );
};

export default Login;