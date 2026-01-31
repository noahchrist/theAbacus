import { useState, useEffect } from 'react';

function ConnectionTest() {
  const [status, setStatus] = useState('checking...');
  const [response, setResponse] = useState(null);

  const checkConnection = async () => {
    try {
      const res = await fetch('http://localhost:8000/api/ping');
      const data = await res.json();
      setStatus('✅ Connected');
      setResponse(data);
    } catch (error) {
      setStatus('❌ Disconnected');
      setResponse({ error: error.message });
    }
  };

  useEffect(() => {
    checkConnection();
  }, []);

  return (
    <div style={{ 
      padding: '20px', 
      margin: '20px', 
      border: '1px solid #ccc',
      borderRadius: '8px',
      backgroundColor: '#f5f5f5'
    }}>
      <h3>Backend Connection Status</h3>
      <p><strong>Status:</strong> {status}</p>
      {response && (
        <div>
          <p><strong>Response:</strong></p>
          <pre style={{ 
            backgroundColor: '#fff', 
            padding: '10px',
            borderRadius: '4px',
            overflow: 'auto'
          }}>
            {JSON.stringify(response, null, 2)}
          </pre>
        </div>
      )}
      <button 
        onClick={checkConnection}
        style={{
          padding: '8px 16px',
          marginTop: '10px',
          cursor: 'pointer',
          backgroundColor: '#4CAF50',
          color: 'white',
          border: 'none',
          borderRadius: '4px'
        }}
      >
        Test Connection Again
      </button>
    </div>
  );
}

export default ConnectionTest;