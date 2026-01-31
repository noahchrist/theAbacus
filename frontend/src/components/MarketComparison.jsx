import { useState, useEffect } from 'react';
import { fetchMarkets } from '../services/api';

function MarketComparison() {
  const [markets, setMarkets] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadMarkets = async () => {
      try {
        const data = await fetchMarkets();
        setMarkets(data);
      } catch (error) {
        console.error('Error fetching markets:', error);
      } finally {
        setLoading(false);
      }
    };

    loadMarkets();
    // Refresh every 5 minutes
    const interval = setInterval(loadMarkets, 300000);
    return () => clearInterval(interval);
  }, []);

  if (loading) return <div>Loading markets...</div>;

  return (
    <div className="market-comparison">
      <h2>Active Markets</h2>
      {markets.length === 0 ? (
        <p>No markets with positive edge found.</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>Sport</th>
              <th>Market</th>
              <th>Line</th>
              <th>Kalshi Ask</th>
              <th>Pinnacle Fair</th>
              <th>Edge</th>
              <th>EV/Dollar</th>
            </tr>
          </thead>
          <tbody>
            {markets.map((market) => (
              <tr key={market.id} className={market.edge > 0.05 ? 'positive-edge' : ''}>
                <td>{market.sport}</td>
                <td>{market.market_type}</td>
                <td>{market.line}</td>
                <td>{(market.kalshi_ask * 100).toFixed(1)}%</td>
                <td>{(market.pinnacle_fair * 100).toFixed(1)}%</td>
                <td className={market.edge > 0 ? 'positive' : 'negative'}>
                  {(market.edge * 100).toFixed(2)}%
                </td>
                <td>${market.ev_per_dollar.toFixed(3)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default MarketComparison;