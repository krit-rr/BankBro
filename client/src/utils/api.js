import { formatTwoDecimalPlaces } from "./format";
import { iex } from "./iex";

const fetchSymbolData = async (query) => {
  try {
    const response = await fetch(
      `${iex.base_url}/stock/${query}/batch?types=quote,company,news,intraday-prices&last=1&token=${iex.api_token}`
    );

    if (!response.ok) return handleAPIError(response, query);

    const data = await response.json();

    /* Edge case for IEX API in which the data is not in
     * the database, but the response returned ok
     */
    if (data.quote === null || data.company === null) {
      const customError = { status: 404 };
      return handleAPIError(customError, query);
    }

    return {
      ...data,
      quote: extractQuoteData(data.quote),
      company: extractCompanyData(data.company),
    };
  } catch (error) {
    const customError = { status: 500 };
    return handleAPIError(customError);
  }
};

export default fetchSymbolData;

/* Helper Functions */
const handleAPIError = (response, query = "") => {
  const errorMessage = setHTTPErrorMessage(response.status, query);
  return {
    error: true,
    status: response.status,
    message: response.statusText || errorMessage,
  };
};

const extractQuoteData = (data) => {
  const filtered_quote = {
    symbol: data.symbol,
    companyName: data.companyName,
    primaryExchange: data.primaryExchange,
    open: formatTwoDecimalPlaces(data.open),
    previousClose: formatTwoDecimalPlaces(data.previousClose),
    high: formatTwoDecimalPlaces(data.high),
    low: formatTwoDecimalPlaces(data.low),
    latestPrice: formatTwoDecimalPlaces(data.latestPrice),
    latestSource: data.latestSource,
    latestUpdate: data.latestUpdate,
    latestVolume: data.latestVolume,
    volume: data.volume,
    avgTotalVolume: data.avgTotalVolume,
    change: formatTwoDecimalPlaces(data.change),
    changePercent: formatTwoDecimalPlaces(data.changePercent * 100),
    week52High: formatTwoDecimalPlaces(data.week52High),
    week52Low: formatTwoDecimalPlaces(data.week52Low),
    peRatio: formatTwoDecimalPlaces(data.peRatio),
    marketCap: data.marketCap,
  };
  return filtered_quote;
};

const extractCompanyData = (data) => {
  const filtered_company = {
    description: data.description,
    CEO: data.CEO,
    employees: data.employees,
    sector: data.sector,
    industry: data.industry,
    city: data.city,
    state: data.state,
    address: data.address,
    website: data.website,
  };
  return filtered_company;
};

const setHTTPErrorMessage = (status, query) => {
  if (status === 400) return `Error: Bad request`;
  if (status === 401) return `Error: Forbidden`;
  if (status === 402) return `Error: Free API credit limit has been exceeded`;
  if (status === 403) return `Error: The API token provided is no longer valid`;
  if (status === 404) return `No results found for "${query}"`;
  if (status === 429) return `Error: Too many requests`;
  if (status === 451)
    return `Error: Requested data requires additional permission to access`;
  return `Internal server error`;
};
