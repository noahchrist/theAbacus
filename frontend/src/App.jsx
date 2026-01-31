import { useState } from 'react';
import MarketComparison from './components/MarketComparison.jsx';
import AccountBalance from './components/AccountBalance.jsx';
import './App.css';

function App() {
  return (
    <div className="App">
      <header>
        <div className="header-content">
          <div className="title-section">
            <h1>The Abacus</h1>
            <p>Count Every Edge</p>
          </div>
          <AccountBalance />
        </div>
      </header>
      <main>
        <MarketComparison />
      </main>
    </div>
  );
}

export default App;