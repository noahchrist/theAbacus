import { useState } from 'react';
import MarketComparison from './components/MarketComparison.jsx';
import ConnectionTest from './components/ConnectionTest.jsx';
import './App.css';

function App() {
  return (
    <div className="App">
      <header>
        <h1>The Abacus</h1>
        <p>Count Every Edge</p>
      </header>
      <main>
        <ConnectionTest />
        <MarketComparison />
      </main>
    </div>
  );
}

export default App;