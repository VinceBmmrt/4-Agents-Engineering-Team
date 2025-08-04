import gradio as gr
from accounts import Account

user_account = None

def create_account(username, initial_deposit):
    global user_account
    user_account = Account(username, float(initial_deposit))
    return f"Account created for {username} with an initial deposit of {initial_deposit}"

def deposit_funds(amount):
    global user_account
    user_account.deposit(float(amount))
    return f"Deposited: {amount}. Current balance: {user_account.balance}"

def withdraw_funds(amount):
    global user_account
    try:
        user_account.withdraw(float(amount))
        return f"Withdrew: {amount}. Current balance: {user_account.balance}"
    except ValueError as e:
        return str(e)

def buy_shares(symbol, quantity):
    global user_account
    try:
        user_account.buy_shares(symbol, int(quantity))
        return f"Bought {quantity} shares of {symbol}. Remaining balance: {user_account.balance}"
    except ValueError as e:
        return str(e)

def sell_shares(symbol, quantity):
    global user_account
    try:
        user_account.sell_shares(symbol, int(quantity))
        return f"Sold {quantity} shares of {symbol}. Remaining balance: {user_account.balance}"
    except ValueError as e:
        return str(e)

def get_holdings():
    global user_account
    return user_account.get_holdings()

def get_portfolio_value():
    global user_account
    return user_account.get_portfolio_value()

def get_profit_or_loss():
    global user_account
    return user_account.get_profit_or_loss()

def get_transactions():
    global user_account
    return user_account.get_transactions()

with gr.Blocks() as app:
    gr.Markdown("# Trading Simulation Platform")
    
    with gr.Tabs():
        with gr.Tab("Account Management"):
            username_input = gr.Textbox(label="Username")
            initial_deposit_input = gr.Number(value=0, label="Initial Deposit")
            create_btn = gr.Button("Create Account")
            deposit_input = gr.Number(value=0, label="Deposit Amount")
            deposit_btn = gr.Button("Deposit Funds")
            withdraw_input = gr.Number(value=0, label="Withdrawal Amount")
            withdraw_btn = gr.Button("Withdraw Funds")
            account_status = gr.Textbox(label="Account Status", interactive=False)
            
            create_btn.click(fn=create_account, inputs=[username_input, initial_deposit_input], outputs=account_status)
            deposit_btn.click(fn=deposit_funds, inputs=deposit_input, outputs=account_status)
            withdraw_btn.click(fn=withdraw_funds, inputs=withdraw_input, outputs=account_status)

        with gr.Tab("Trading"):
            symbol_input = gr.Textbox(label="Share Symbol (AAPL, TSLA, GOOGL)")
            quantity_input = gr.Number(value=1, label="Quantity")
            buy_btn = gr.Button("Buy Shares")
            sell_btn = gr.Button("Sell Shares")
            trading_status = gr.Textbox(label="Trading Status", interactive=False)

            buy_btn.click(fn=buy_shares, inputs=[symbol_input, quantity_input], outputs=trading_status)
            sell_btn.click(fn=sell_shares, inputs=[symbol_input, quantity_input], outputs=trading_status)

        with gr.Tab("Reports"):
            holdings_btn = gr.Button("Show Holdings")
            portfolio_value_btn = gr.Button("Show Portfolio Value")
            profit_loss_btn = gr.Button("Show Profit/Loss")
            transactions_btn = gr.Button("Show Transactions")
            reports_output = gr.Textbox(label="Reports", interactive=False)

            holdings_btn.click(fn=get_holdings, outputs=reports_output)
            portfolio_value_btn.click(fn=get_portfolio_value, outputs=reports_output)
            profit_loss_btn.click(fn=get_profit_or_loss, outputs=reports_output)
            transactions_btn.click(fn=get_transactions, outputs=reports_output)

app.launch()