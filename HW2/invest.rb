# HW2, PS398, implementation in Ruby

# First we add a round_to method for Float numbers
class Float
  def round_to(x)
    (self * 10**x).round.to_f / 10**x
  end

  def ceil_to(x)
    (self * 10**x).ceil.to_f / 10**x
  end

  def floor_to(x)
    (self * 10**x).floor.to_f / 10**x
  end
end


class Portfolio < Object

  attr_reader :transactions, :cashBalance, :stockBalance, :mfBalance

  def initialize
    @transactions = ''
    @cashBalance = 0
    @stockBalance = Hash.new
    @mfBalance = Hash.new
  end

  def print
    @stock_list = "" # refresh lists
    @mf_list = ""

    temp_long_str = ''
    @stockBalance.each_key do |k|
      temp_str = String(k) + ' ' + String(@stockBalance[k]["shares"]) + "\n"
      temp_long_str += temp_str
    end
    @stock_list = temp_long_str[0..-2] # removes last newline

    temp_long_str = ''
    @mfBalance.each_key do |k|
      temp_str = String(k) + ' ' + String(@mfBalance[k]["shares"]) + "\n" 
      # TODO: round to 2 digits if numshares is float
      temp_long_str += temp_str
    end
    @mf_list = temp_long_str[0..-2] # removes last newline

    puts "Cash: %.2f \nStock: #{@stock_list} \nMutual Funds: #{@mf_list}" % @cashBalance
    puts
  end

  def history
    puts self.transactions
  end

  def addCash(amount)
    @cashBalance += amount
    @transactions += ("$%.2f added.\n" % amount)
  end

  def withdrawCash(amount)
    if amount < 0
      puts "Negative amounts not allowed."
      return
    end
    @cashBalance -= amount
    @transactions += ("$%.2f withdrawn.\n" % amount)
  end

  def buyStock(shares, stock)
    purchase_amount = shares * stock.price
    if (shares % 1 == 0) & (purchase_amount <= @cashBalance)
      @cashBalance -= purchase_amount
      @stockBalance[stock.name] = {"shares" => shares, "object" => stock}
      @transactions += ("Purchased #{shares} shares of #{stock.name} stock at $#{stock.price} per share, for a total of $#{purchase_amount}\n")
      puts "#{stock.name} successfully purchased."
    elsif (shares % 1 == 0) & (purchase_amount  >@cashBalance)
      puts "That purchase exceeds your cash balance of $#{cash_balance}."
    elsif (shares % 1 != 0)
      puts "Fractional shares cannot be purchased."
    end
  end

  def buyMutualFund(shares, fund)
    purchase_amount = shares * fund.price
    if (purchase_amount <= @cashBalance)
      @cashBalance -= purchase_amount
      @mfBalance[fund.name] = {'shares' => shares, 'object' => fund}
      @transactions += ("Purchased #{shares} shares of #{fund.name} fund at $#{fund.price} for a total of #{purchase_amount}.\n")
    else
      puts "That purchase exceeds your cash balance of #{@cashBalance}."
    end
  end

  def sellStock(symbol, shares_to_sell)
    #puts @stockBalance[symbol]
    shares_owned = @stockBalance[symbol]["shares"]
    if shares_owned >= shares_to_sell
      stock_obj = @stockBalance[symbol]["object"]
      stock_obj.calc_sell_price
      sell_price = stock_obj.sell_price
      total_sell_price = sell_price * shares_to_sell
      @cashBalance += total_sell_price
      temp_txt = "Sold #{ shares_to_sell } shares of #{symbol} at a price of $#{sell_price} for a total of $#{total_sell_price}."
      @transactions += temp_txt + "\n"
      puts temp_txt
      @stockBalance[symbol]["shares"] -= shares_to_sell
    else
      puts "You do not have that many shares."
    end
  end

  def sellMutualFund(symbol, shares_to_sell)
    shares_owned = @mfBalance[symbol]["shares"]
    if shares_owned >= shares_to_sell
      mf_obj = @mfBalance[symbol]["object"]
      mf_obj.calc_sell_price
      sell_price = mf_obj.sell_price
      total_sell_price = (sell_price * shares_to_sell).round_to(2)
      @cashBalance += total_sell_price
      temp_txt = "Sold #{ shares_to_sell } shares of #{symbol} at a price of $#{sell_price} for a total of $#{total_sell_price}."
      @transactions += temp_txt + "\n"
      puts temp_txt
      @mfBalance[symbol]["shares"] -= shares_to_sell
      #@mfBalance[symbol]["shares"].round_to(2)
    else
      puts "You do not have that many shares."
    end
  end

end


class Stock < Object

  attr_accessor :price, :name 
  attr_reader :sell_price

  def initialize(price, name)
    @price = price
    @name = name
  end

  def print
    puts "Name: #{@name} \nPrice: #{@price}"
    puts
  end

  def calc_sell_price
    @sell_price = ( @price * (0.5+rand)).round_to(2)
  end
end


class MutualFund < Object

  attr_accessor :price, :name 
  attr_reader :sell_price

  def initialize(name)
    @price = 1
    @name = name
  end

  def print
    puts "Name: #{@name}"
    puts
  end

  def calc_sell_price
    @sell_price = (0.9+rand*0.3).round_to(2)
  end
end


    
# TODO: add exceptions for when people try to sell stocks they don't own
# TODO: make all prints of cashBalance round to 2 decimal places
