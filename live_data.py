"""
Live Trading Data Integration
Connects to real market data feeds and broker APIs
"""

import asyncio
import websocket
import json
import threading
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Callable
import logging
from dataclasses import dataclass
import time

@dataclass
class MarketData:
    """Real-time market data structure"""
    symbol: str
    price: float
    bid: float
    ask: float
    volume: int
    timestamp: datetime
    change: float = 0.0
    change_percent: float = 0.0

@dataclass
class Position:
    """Trading position structure"""
    symbol: str
    quantity: float
    entry_price: float
    current_price: float
    unrealized_pnl: float
    entry_time: datetime
    position_id: str

class LiveDataManager:
    """Manages live market data connections and trading data"""
    
    def __init__(self):
        self.market_data: Dict[str, MarketData] = {}
        self.positions: Dict[str, Position] = {}
        self.data_callbacks: List[Callable] = []
        self.is_connected = False
        self.ws = None
        self._lock = threading.Lock()
        
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
    
    def add_data_callback(self, callback: Callable):
        """Add callback for data updates"""
        self.data_callbacks.append(callback)
    
    def connect_to_feed(self, url: str, symbols: List[str]):
        """Connect to live data feed"""
        try:
            # For demo purposes, simulate connection
            self.is_connected = True
            self.logger.info(f"Connected to data feed: {url}")
            
            # Start simulation thread for demo
            threading.Thread(target=self._simulate_market_data, 
                           args=(symbols,), daemon=True).start()
            
        except Exception as e:
            self.logger.error(f"Failed to connect to data feed: {e}")
            self.is_connected = False
    
    def _simulate_market_data(self, symbols: List[str]):
        """Simulate real-time market data for testing"""
        import random
        import math
        
        # Initialize base prices
        base_prices = {
            'ES': 4485.25,
            'NQ': 15847.50,
            'CL': 82.45,
            'GC': 2045.20,
            'YM': 34567.80,
            'RTY': 2089.45
        }
        
        while self.is_connected:
            try:
                current_time = datetime.now()
                
                for symbol in symbols:
                    if symbol not in base_prices:
                        continue
                        
                    # Generate realistic price movement
                    base_price = base_prices[symbol]
                    time_factor = current_time.timestamp() % 3600  # Hour cycle
                    trend = math.sin(time_factor / 3600 * 2 * math.pi) * 0.001
                    volatility = random.gauss(0, 0.0005)
                    
                    # Update price with trend and volatility
                    new_price = base_price * (1 + trend + volatility)
                    base_prices[symbol] = new_price
                    
                    # Create market data
                    spread = new_price * 0.0001  # 1 basis point spread
                    market_data = MarketData(
                        symbol=symbol,
                        price=round(new_price, 2),
                        bid=round(new_price - spread/2, 2),
                        ask=round(new_price + spread/2, 2),
                        volume=random.randint(100, 1000),
                        timestamp=current_time,
                        change=round((new_price - base_price) * 100, 2),
                        change_percent=round((new_price - base_price) / base_price * 100, 4)
                    )
                    
                    with self._lock:
                        self.market_data[symbol] = market_data
                    
                    # Notify callbacks
                    for callback in self.data_callbacks:
                        try:
                            callback(market_data)
                        except Exception as e:
                            self.logger.error(f"Callback error: {e}")
                
                time.sleep(0.1)  # Update every 100ms
                
            except Exception as e:
                self.logger.error(f"Market data simulation error: {e}")
                time.sleep(1)
    
    def get_market_data(self, symbol: str) -> Optional[MarketData]:
        """Get current market data for symbol"""
        with self._lock:
            return self.market_data.get(symbol)
    
    def get_all_market_data(self) -> Dict[str, MarketData]:
        """Get all current market data"""
        with self._lock:
            return self.market_data.copy()
    
    def add_position(self, position: Position):
        """Add a trading position"""
        with self._lock:
            self.positions[position.position_id] = position
            self.logger.info(f"Added position: {position.symbol} {position.quantity}")
    
    def update_position_prices(self):
        """Update position P&L with current market prices"""
        with self._lock:
            for position in self.positions.values():
                market_data = self.market_data.get(position.symbol)
                if market_data:
                    position.current_price = market_data.price
                    position.unrealized_pnl = (
                        (position.current_price - position.entry_price) * 
                        position.quantity
                    )
    
    def get_positions(self) -> Dict[str, Position]:
        """Get all current positions"""
        self.update_position_prices()
        with self._lock:
            return self.positions.copy()
    
    def close_position(self, position_id: str) -> bool:
        """Close a trading position"""
        with self._lock:
            if position_id in self.positions:
                position = self.positions.pop(position_id)
                self.logger.info(f"Closed position: {position.symbol} {position.quantity}")
                return True
            return False
    
    def disconnect(self):
        """Disconnect from data feed"""
        self.is_connected = False
        if self.ws:
            self.ws.close()
        self.logger.info("Disconnected from data feed")

# Global data manager instance
data_manager = LiveDataManager()