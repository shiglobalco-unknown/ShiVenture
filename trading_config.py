"""
Trading Configuration System
Manages AI trading system parameters and API connections
"""

import os
from dataclasses import dataclass
from typing import Dict, List, Optional
import json

@dataclass
class TradingConfig:
    """Configuration for AI trading system"""
    
    # API Configuration
    broker_api_key: str = ""
    broker_secret: str = ""
    data_feed_url: str = "wss://stream.tradier.com/v1/markets/events"
    
    # Trading Parameters
    max_position_size: float = 100000.0
    risk_per_trade: float = 0.02  # 2% risk per trade
    max_daily_drawdown: float = 0.05  # 5% max daily drawdown
    
    # AI Agent Configuration
    enable_ai_trading: bool = True
    agent_update_interval: float = 1.0  # seconds
    max_concurrent_positions: int = 10
    
    # Risk Management
    emergency_stop_loss: float = 0.10  # 10% emergency stop
    position_timeout: int = 86400  # 24 hours in seconds
    
    # Supported Instruments
    allowed_symbols: List[str] = None
    
    def __post_init__(self):
        if self.allowed_symbols is None:
            self.allowed_symbols = [
                'ES', 'NQ', 'YM', 'RTY',  # Index futures
                'CL', 'NG', 'GC', 'SI',   # Commodities
                'ZN', 'ZB', 'ZF', 'ZT'    # Treasury futures
            ]
    
    @classmethod
    def load_from_env(cls) -> 'TradingConfig':
        """Load configuration from environment variables"""
        return cls(
            broker_api_key=os.getenv('BROKER_API_KEY', ''),
            broker_secret=os.getenv('BROKER_SECRET', ''),
            data_feed_url=os.getenv('DATA_FEED_URL', 'wss://stream.tradier.com/v1/markets/events'),
            max_position_size=float(os.getenv('MAX_POSITION_SIZE', '100000.0')),
            risk_per_trade=float(os.getenv('RISK_PER_TRADE', '0.02')),
            max_daily_drawdown=float(os.getenv('MAX_DAILY_DRAWDOWN', '0.05')),
            enable_ai_trading=os.getenv('ENABLE_AI_TRADING', 'True').lower() == 'true',
            agent_update_interval=float(os.getenv('AGENT_UPDATE_INTERVAL', '1.0')),
            max_concurrent_positions=int(os.getenv('MAX_CONCURRENT_POSITIONS', '10'))
        )
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization"""
        return {
            'broker_api_key': '***' if self.broker_api_key else '',
            'broker_secret': '***' if self.broker_secret else '',
            'data_feed_url': self.data_feed_url,
            'max_position_size': self.max_position_size,
            'risk_per_trade': self.risk_per_trade,
            'max_daily_drawdown': self.max_daily_drawdown,
            'enable_ai_trading': self.enable_ai_trading,
            'agent_update_interval': self.agent_update_interval,
            'max_concurrent_positions': self.max_concurrent_positions,
            'emergency_stop_loss': self.emergency_stop_loss,
            'position_timeout': self.position_timeout,
            'allowed_symbols': self.allowed_symbols
        }

# Global configuration instance
CONFIG = TradingConfig.load_from_env()