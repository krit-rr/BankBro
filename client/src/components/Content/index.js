import Quote from "./Quote";
import Stats from "./Stats";
import DataChart from "./DataChart";
import Error from "./Error";
import "./style.css";

const Content = ({ data }) => {
  const { quote } = data;

  if (data.error) return <Error data={data} />;

  return (
    <>
      <div className="main-header">
        <div>
          <h1 className="main-title">{quote.companyName}</h1>
          <p>{`${quote.primaryExchange}`}</p>
        </div>
      </div>

      <div className="main-item first">
        <Quote data={quote} />
        <Stats data={quote} />
      </div>
      <div className="main-item">
        <DataChart data={data["intraday-prices"]} priceChange={quote.change} />
      </div>
    </>
  );
};

export default Content;
