// YAPPOLA-COIN ICO 

pragma solidity ^0.4.11; 


contract YAPPOLA_COIN_ICO{
    
    
    //INTRODUCING TOTAL YAPPOLA COINS FOR SALE 
    uint public max_YAPPOLAcoins = 1999999;
    
    // INTRODUCING USD TO YAPPOLA CONVERSION RATE 
    uint public usd_to_YAPPOLAcoins = 1999; 
    
    //INTRODUCING TOTAL NUMBER OF YAPPOLA COINS BOUGHT BY INVESTORS
    uint public total_YAPPOLAcoins_bought = 0; 
    
    //MAPPING IS STORED IN AN ARRAY 
    mapping(address => uint) equity_YAPPOLAcoins; 
    mapping(address => uint) equity_usd; 
    
    //CHECK IF INVESTORS CAN BUY YAPPOLACOINS 
    modifier can_buy_YAPPOLAcoins(uint usd_invested){
        require (usd_invested * usd_to_YAPPOLAcoins + total_YAPPOLAcoins_bought<=max_YAPPOLAcoins);
        _;
    }
    //GETTING EQUITY IN YAPPOLACOINS AS INVESTOR 
    function equity_in_YAPPOLAcoins(address investor) external constant returns(uint){
        return equity_YAPPOLAcoins[investor];
    }
    
    //GETTING EQUITY IN USD AS INVESTOR 
    function equity_in_USD(address investor) external constant returns(uint){
        return equity_usd[investor];
    }
    
    //buying YAPPOLACOINS 
    function buy_YAPPOLAcoins(address investor, uint usd_invested) external 
    can_buy_YAPPOLAcoins(usd_invested){
        uint YAPPOLAcoins_bought= usd_invested * usd_to_YAPPOLAcoins;
        equity_YAPPOLAcoins[investor] += YAPPOLAcoins_bought; 
        equity_usd[investor] = equity_YAPPOLAcoins[investor]/ 1999; 
        total_YAPPOLAcoins_bought += YAPPOLAcoins_bought;
    }
    //SELLING YAPPOLACOINS
    function sell_YAPPOLAcoins(address investor, uint YAPPOLAcoins_sold) external{
        equity_YAPPOLAcoins[investor] -= YAPPOLAcoins_sold; 
        equity_usd[investor] = equity_YAPPOLAcoins[investor]/ 1999; 
        total_YAPPOLAcoins_bought -= YAPPOLAcoins_sold;
    }
}
