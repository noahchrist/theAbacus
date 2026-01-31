import { useState, useEffect } from 'react';

function AccountBalance() {
  const [balance, setBalance] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchBalance = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch('http://localhost:8000/api/account/balance');
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      
      if (!data.configured) {
        setError("Not configured");
      }
      
      setBalance(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchBalance();
  }, []);

  if (loading) {
    return (
      <div className="account-balance loading">
        <span>Loading...</span>
      </div>
    );
  }

  if (error) {
    return (
      <div className="account-balance error">
        <span>⚠️ Balance: Not Connected</span>
      </div>
    );
  }

  return (
    <div className="account-balance">
      <span className="label">Balance:</span>
      <span className="amount">${parseFloat(balance.balance).toLocaleString('en-US', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
      })}</span>
      <button onClick={fetchBalance} className="refresh-btn" title="Refresh balance">↻</button>
    </div>
  );
}

export default AccountBalance;