from src.ROIC.roic import ROIC


if __name__ == "__main__":

    roic = ROIC()
    TICKER = "AAPL"
    summary = roic.scrape_summary(TICKER)
    income_statement = roic.scrape_income_statement(TICKER)
