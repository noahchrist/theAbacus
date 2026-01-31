def remove_vig(over_implied: float, under_implied: float) -> tuple[float, float]:
    """
    Remove vig from implied probabilities
    Returns (fair_over, fair_under)
    """
    total = over_implied + under_implied
    fair_over = over_implied / total
    fair_under = under_implied / total
    return fair_over, fair_under

def decimal_to_implied(decimal_odds: float) -> float:
    """Convert decimal odds to implied probability"""
    return 1 / decimal_odds

def american_to_implied(american_odds: int) -> float:
    """Convert American odds to implied probability"""
    if american_odds > 0:
        return 100 / (american_odds + 100)
    else:
        return abs(american_odds) / (abs(american_odds) + 100)

def calculate_edge(kalshi_ask: float, pinnacle_over: float, pinnacle_under: float) -> dict:
    """
    Calculate edge for a market
    
    Args:
        kalshi_ask: Kalshi's ask price (0-1)
        pinnacle_over: Pinnacle's decimal odds for over
        pinnacle_under: Pinnacle's decimal odds for under
    
    Returns:
        dict with edge calculations
    """
    # Convert Pinnacle odds to implied probabilities
    pinnacle_over_implied = decimal_to_implied(pinnacle_over)
    pinnacle_under_implied = decimal_to_implied(pinnacle_under)
    
    # Calculate vig
    total_implied = pinnacle_over_implied + pinnacle_under_implied
    vig = total_implied - 1.0
    
    # Remove vig to get fair probability
    fair_over, fair_under = remove_vig(pinnacle_over_implied, pinnacle_under_implied)
    
    # Calculate edge
    edge = fair_over - kalshi_ask
    
    # Calculate EV per $1 bet (if holding to settlement)
    payout_if_win = 1 - kalshi_ask
    ev = (fair_over * payout_if_win) - ((1 - fair_over) * kalshi_ask)
    
    return {
        "kalshi_ask": kalshi_ask,
        "pinnacle_over_implied": pinnacle_over_implied,
        "pinnacle_under_implied": pinnacle_under_implied,
        "vig": vig,
        "pinnacle_fair": fair_over,
        "edge": edge,
        "ev_per_dollar": ev,
        "roi": (ev / kalshi_ask) if kalshi_ask > 0 else 0
    }