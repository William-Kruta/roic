import time
from .scraper import Scraper
from .utils import clean_dataframe


class ROIC:
    def __init__(self, headless: bool = True, log: bool = False):
        self.scraper = Scraper(headless, log)

    def scrape_summary(self, ticker: str):
        url = "https://www.roic.ai/quote/{}"
        col_start_index = 3
        row_start_index = 1
        col_xpath = "/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/table/thead/tr/th[{}]/div/span"
        row_xpath = "/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/table/tbody/tr[{}]/td[1]/div/div[2]/span"
        base_xpath = "/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/table/tbody/tr[{}]/td[{}]/div/span"
        # base_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[1]/div/div/div/table/tbody/tr[{}]/td[{}]"
        table = self._extract_table(
            url.format(ticker.upper()),
            row_xpath,
            col_xpath,
            row_start_index,
            col_start_index,
            base_xpath,
        )
        return table

    def scrape_income_statement(self, ticker: str):
        url = "https://www.roic.ai/quote/{}/financials"
        col_start_index = 3
        row_start_index = 1
        col_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[1]/div/div/div/table/thead/tr/th[{}]/div/span"
        row_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[1]/div/div/div/table/tbody/tr[{}]/td[1]/div/div[2]/span"
        base_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[1]/div/div/div/table/tbody/tr[{}]/td[{}]"
        table = self._extract_table(
            url.format(ticker.upper()),
            row_xpath,
            col_xpath,
            row_start_index,
            col_start_index,
            base_xpath,
        )
        return table

    def scrape_balance_sheet(self, ticker: str):
        url = "https://www.roic.ai/quote/{}/financials"
        col_start_index = 3
        row_start_index = 1
        col_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[2]/div/div/div/table/thead/tr/th[{}]/div/span"
        row_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[2]/div/div/div/table/tbody/tr[{}]/td[1]/div/div[2]/span"
        base_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[2]/div/div/div/table/tbody/tr[{}]/td[{}]"
        table = self._extract_table(
            url.format(ticker.upper()),
            row_xpath,
            col_xpath,
            row_start_index,
            col_start_index,
            base_xpath,
        )
        return table

    def scrape_cash_flow(self, ticker: str):
        url = "https://www.roic.ai/quote/{}/financials"
        col_start_index = 3
        row_start_index = 1
        col_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[3]/div/div/div/table/thead/tr/th[{}]/div/span"
        row_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[3]/div/div/div/table/tbody/tr[{}]/td[1]/div/div[2]/span"
        base_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[3]/div/div/div/table/tbody/tr[{}]/td[{}]"
        table = self._extract_table(
            url.format(ticker.upper()),
            row_xpath,
            col_xpath,
            row_start_index,
            col_start_index,
            base_xpath,
        )
        return table

    def scrape_profitability(self, ticker: str):
        url = "https://www.roic.ai/quote/{}/ratios"
        col_start_index = 3
        row_start_index = 1
        col_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[1]/div/div/div/table/thead/tr/th[{}]/div/span"
        row_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[1]/div/div/div/table/tbody/tr[{}]/td[1]/div/div[2]/span"
        base_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[1]/div/div/div/table/tbody/tr[{}]/td[{}]"
        table = self._extract_table(
            url.format(ticker.upper()),
            row_xpath,
            col_xpath,
            row_start_index,
            col_start_index,
            base_xpath,
        )
        return table

    def scrape_credit(self, ticker: str):
        url = "https://www.roic.ai/quote/{}/ratios"
        col_start_index = 3
        row_start_index = 1
        col_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[2]/div/div/div/table/thead/tr/th[{}]/div/span"
        row_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[2]/div/div/div/table/tbody/tr[{}]/td[1]/div/div[2]/span"
        base_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[2]/div/div/div/table/tbody/tr[{}]/td[{}]"
        table = self._extract_table(
            url.format(ticker.upper()),
            row_xpath,
            col_xpath,
            row_start_index,
            col_start_index,
            base_xpath,
        )
        return table

    def scrape_liquidity(self, ticker: str):
        url = "https://www.roic.ai/quote/{}/ratios"
        col_start_index = 3
        row_start_index = 1
        col_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[3]/div/div/div/table/thead/tr/th[{}]/div/span"
        row_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[3]/div/div/div/table/tbody/tr[{}]/td[1]/div/div[2]/span"
        base_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[3]/div/div/div/table/tbody/tr[{}]/td[{}]"
        table = self._extract_table(
            url.format(ticker.upper()),
            row_xpath,
            col_xpath,
            row_start_index,
            col_start_index,
            base_xpath,
        )
        return table

    def scrape_working_capital(self, ticker: str):
        url = "https://www.roic.ai/quote/{}/ratios"
        col_start_index = 3
        row_start_index = 1
        col_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[4]/div/div/div/table/thead/tr/th[{}]/div/span"
        row_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[4]/div/div/div/table/tbody/tr[{}]/td[1]/div/div[2]/span"
        base_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[4]/div/div/div/table/tbody/tr[{}]/td[{}]"
        table = self._extract_table(
            url.format(ticker.upper()),
            row_xpath,
            col_xpath,
            row_start_index,
            col_start_index,
            base_xpath,
        )
        return table

    def scrape_enterprise_value(self, ticker: str):
        url = "https://www.roic.ai/quote/{}/ratios"
        col_start_index = 3
        row_start_index = 1
        col_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[5]/div/div/div/table/thead/tr/th[{}]/div/span"
        row_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[5]/div/div/div/table/tbody/tr[{}]/td[1]/div/div[2]/span"
        base_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[5]/div/div/div/table/tbody/tr[{}]/td[{}]"
        table = self._extract_table(
            url.format(ticker.upper()),
            row_xpath,
            col_xpath,
            row_start_index,
            col_start_index,
            base_xpath,
        )
        return table

    def scrape_multiples(self, ticker: str):
        url = "https://www.roic.ai/quote/{}/ratios"
        col_start_index = 3
        row_start_index = 1
        col_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[6]/div/div/div/table/thead/tr/th[{}]/div/span"
        row_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[6]/div/div/div/table/tbody/tr[{}]/td[1]/div/div[2]/span"
        base_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[6]/div/div/div/table/tbody/tr[{}]/td[{}]"
        table = self._extract_table(
            url.format(ticker.upper()),
            row_xpath,
            col_xpath,
            row_start_index,
            col_start_index,
            base_xpath,
        )
        return table

    def scrape_per_share_data(self, ticker: str):
        url = "https://www.roic.ai/quote/{}/ratios"
        col_start_index = 3
        row_start_index = 1
        col_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[7]/div/div/div/table/thead/tr/th[{}]/div/span"
        row_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[7]/div/div/div/table/tbody/tr[{}]/td[1]/div/div[2]/span"
        base_xpath = "/html/body/div[1]/div/div[2]/div[3]/div[7]/div/div/div/table/tbody/tr[{}]/td[{}]"
        xpath = "/html/body/div[1]/div/div[2]/div[3]/div[1]/div/div/div/table/tbody/tr[1]/td[17]/div/span"
        table = self._extract_table(
            url.format(ticker.upper()),
            row_xpath,
            col_xpath,
            row_start_index,
            col_start_index,
            base_xpath,
        )
        return table

    def _extract_table(
        self,
        url: str,
        row_xpath: str,
        col_xpath: str,
        row_start_index: int,
        col_start_index: int,
        base_xpath,
    ):
        self.scraper.create_browser(url)
        rows, cols = self.scraper.get_table_labels(
            row_xpath, col_xpath, row_start_index, col_start_index
        )
        table = self.scraper._scrape_table(
            min_col=col_start_index,
            max_col=(len(cols) + col_start_index) - 1,
            base_xpath=base_xpath,
            keys=cols,
        )
        table.index = rows
        table = clean_dataframe(table)
        return table


if __name__ == "__main__":

    roic = ROIC()
    df = roic.scrape_summary("AAPL")
    # df = roic.scrape_per_share_data("AAPL")
    print(f"DF: {df}")
