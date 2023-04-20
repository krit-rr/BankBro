import { unixToDateString } from "../../../utils/date";
import { formatChangeString } from "../../../utils/format";
import "./style.css";

const Quote = ({ data }) => {
  return (
    <section id="quote-section">
      <h2 className="quote">
        {data.latestPrice || "--"}
        <span
          className={`${
            Number(data.change) >= 0 ? "color-bullish" : "color-bearish"
          }`}
        >
          {" "}
          {formatChangeString(data.change, data.changePercent) || "-- (--)"}
        </span>
      </h2>
      <p className="quote-meta">
        {data.latestSource || "--"} |{" "}
        {unixToDateString(data.latestUpdate) || "--"}
        
      </p>
    </section>
  );
};

export default Quote;
