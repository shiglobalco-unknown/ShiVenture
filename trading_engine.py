"""
AI Trading Engine
Handles order execution, position management, and AI agent coordination
"""

import uuid
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import logging
import asyncio
from live_data import data_manager, Position, MarketData
from trading_config import CONFIG

class OrderType(Enum):
    MARKET = "market"
    LIMIT = "limit"
    STOP = "stop"
    STOP_LIMIT = "stop_limit"

class OrderSide(Enum):
    BUY = "buy"
    SELL = "sell"

class OrderStatus(Enum):
    PENDING = "pending"
    FILLED = "filled"
    CANCELLED = "cancelled"
    REJECTED = "rejected"

@dataclass
class Order:
    """Trading order structure"""
    order_id: str
    symbol: str
    side: OrderSide
    quantity: float
    order_type: OrderType
    price: Optional[float] = None
    stop_price: Optional[float] = None
    status: OrderStatus = OrderStatus.PENDING
    created_time: datetime = None
    filled_time: Optional[datetime] = None
    filled_price: Optional[float] = None
    agent_id: Optional[str] = None  # Which AI agent created this order
    
    def __post_init__(self):
        if self.created_time is None:
            self.created_time = datetime.now()
        if self.order_id is None:
            self.order_id = str(uuid.uuid4())

class TradingEngine:
    """Core trading engine with AI agent integration"""
    
    def __init__(self):
        self.orders: Dict[str, Order] = {}
        self.execution_log: List[Dict] = []
        self.risk_checks_enabled = True
        self.ai_agents_active = CONFIG.enable_ai_trading
        
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Connect to data feed
        data_manager.connect_to_feed(
            CONFIG.data_feed_url, 
            CONFIG.allowed_symbols
        )
        
        # AI Agent status tracking
        self.agent_status = {
            'master_risk_controller': {'active': True, 'last_update': datetime.now()},
            'strategic_allocator': {'active': True, 'last_update': datetime.now()},
            'performance_monitor': {'active': True, 'last_update': datetime.now()},
            'equity_agent': {'active': True, 'last_update': datetime.now()},
            'fixed_income_agent': {'active': True, 'last_update': datetime.now()},
            'fx_agent': {'active': True, 'last_update': datetime.now()},
        }
    
    def submit_order(self, symbol: str, side: OrderSide, quantity: float, 
                    order_type: OrderType = OrderType.MARKET, 
                    price: Optional[float] = None,
                    agent_id: Optional[str] = None) -> Tuple[bool, str]:
        """Submit a trading order"""
        
        try:
            # Create order
            order = Order(
                order_id=str(uuid.uuid4()),
                symbol=symbol,
                side=side,
                quantity=quantity,
                order_type=order_type,
                price=price,
                agent_id=agent_id
            )
            
            # Risk checks
            if not self._risk_check(order):
                return False, "Order rejected by risk management"
            
            # Store order
            self.orders[order.order_id] = order
            
            # Execute order (simulate immediate fill for demo)
            if order_type == OrderType.MARKET:
                self._fill_market_order(order)
            
            self.logger.info(f"Order submitted: {order.symbol} {order.side.value} {order.quantity}")
            return True, order.order_id
            
        except Exception as e:
            self.logger.error(f"Order submission failed: {e}")
            return False, str(e)
    
    def _risk_check(self, order: Order) -> bool:
        """Perform risk checks on order"""
        if not self.risk_checks_enabled:
            return True
            
        # Check position size limits
        current_positions = data_manager.get_positions()
        total_exposure = sum(abs(pos.quantity * pos.current_price) 
                           for pos in current_positions.values())
        
        order_value = order.quantity * self._get_current_price(order.symbol, order.side)
        
        if total_exposure + abs(order_value) > CONFIG.max_position_size:
            self.logger.warning(f"Order rejected: exceeds position size limit")
            return False
        
        # Check symbol allowlist
        if order.symbol not in CONFIG.allowed_symbols:
            self.logger.warning(f"Order rejected: {order.symbol} not in allowed symbols")
            return False
        
        # Check maximum concurrent positions
        if len(current_positions) >= CONFIG.max_concurrent_positions:
            self.logger.warning(f"Order rejected: maximum concurrent positions reached")
            return False
            
        return True
    
    def _get_current_price(self, symbol: str, side: OrderSide) -> float:
        """Get current market price for order"""
        market_data = data_manager.get_market_data(symbol)
        if market_data:
            return market_data.ask if side == OrderSide.BUY else market_data.bid
        return 0.0
    
    def _fill_market_order(self, order: Order):
        """Simulate market order fill"""
        fill_price = self._get_current_price(order.symbol, order.side)
        
        if fill_price > 0:
            order.status = OrderStatus.FILLED
            order.filled_time = datetime.now()
            order.filled_price = fill_price
            
            # Create position
            position_id = str(uuid.uuid4())
            position = Position(
                symbol=order.symbol,
                quantity=order.quantity if order.side == OrderSide.BUY else -order.quantity,
                entry_price=fill_price,
                current_price=fill_price,
                unrealized_pnl=0.0,
                entry_time=datetime.now(),
                position_id=position_id
            )
            
            data_manager.add_position(position)
            
            # Log execution
            self._log_execution(order, position)
        else:
            order.status = OrderStatus.REJECTED
            self.logger.error(f"Order rejected: no market data for {order.symbol}")
    
    def _log_execution(self, order: Order, position: Position):
        """Log order execution"""
        execution_record = {
            'timestamp': datetime.now(),
            'order_id': order.order_id,
            'symbol': order.symbol,
            'side': order.side.value,
            'quantity': order.quantity,
            'fill_price': order.filled_price,
            'position_id': position.position_id,
            'agent_id': order.agent_id
        }
        self.execution_log.append(execution_record)
    
    def close_position(self, position_id: str, agent_id: Optional[str] = None) -> Tuple[bool, str]:
        """Close an existing position"""
        positions = data_manager.get_positions()
        
        if position_id not in positions:
            return False, "Position not found"
        
        position = positions[position_id]
        
        # Create closing order
        side = OrderSide.SELL if position.quantity > 0 else OrderSide.BUY
        success, result = self.submit_order(
            symbol=position.symbol,
            side=side,
            quantity=abs(position.quantity),
            agent_id=agent_id
        )
        
        if success:
            data_manager.close_position(position_id)
            self.logger.info(f"Position closed: {position.symbol}")
            return True, "Position closed successfully"
        
        return False, result
    
    def emergency_close_all(self) -> Dict[str, bool]:
        """Emergency close all positions"""
        self.logger.warning("EMERGENCY: Closing all positions")
        
        positions = data_manager.get_positions()
        results = {}
        
        for position_id, position in positions.items():
            success, msg = self.close_position(position_id, agent_id="emergency_system")
            results[position_id] = success
            
        return results
    
    def enable_trading_lock(self):
        """Enable trading lock - prevent new positions"""
        self.risk_checks_enabled = False
        self.logger.warning("TRADING LOCK ENABLED: No new positions allowed")
    
    def disable_trading_lock(self):
        """Disable trading lock - allow new positions"""
        self.risk_checks_enabled = True
        self.logger.info("Trading lock disabled")
    
    def get_portfolio_summary(self) -> Dict:
        """Get current portfolio summary"""
        positions = data_manager.get_positions()
        
        total_value = sum(pos.quantity * pos.current_price for pos in positions.values())
        total_pnl = sum(pos.unrealized_pnl for pos in positions.values())
        
        return {
            'total_positions': len(positions),
            'total_value': total_value,
            'unrealized_pnl': total_pnl,
            'positions': {pid: {
                'symbol': pos.symbol,
                'quantity': pos.quantity,
                'entry_price': pos.entry_price,
                'current_price': pos.current_price,
                'unrealized_pnl': pos.unrealized_pnl,
                'entry_time': pos.entry_time
            } for pid, pos in positions.items()},
            'recent_executions': self.execution_log[-10:],  # Last 10 executions
            'agent_status': self.agent_status
        }
    
    def update_agent_status(self, agent_id: str, active: bool):
        """Update AI agent status"""
        if agent_id in self.agent_status:
            self.agent_status[agent_id]['active'] = active
            self.agent_status[agent_id]['last_update'] = datetime.now()

# Global trading engine instance
trading_engine = TradingEngine()