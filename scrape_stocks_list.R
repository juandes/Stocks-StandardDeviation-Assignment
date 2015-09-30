library(rvest)
stocks <- data.frame(stock = character(), stringsAsFactors = FALSE)
stocks.site <- read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
for (i in 2:506) {
stock.symbol <- stocks.site %>% 
                  html_node(paste0("tr:nth-child(", i, ") td:nth-child(1) .text")) %>%
                  html_text()
stocks[i - 1, 1] <-stock.symbol
}

write.table(stocks, file = 'stocks_list.txt', col.names = FALSE, row.names = FALSE,
            quote = FALSE)


  