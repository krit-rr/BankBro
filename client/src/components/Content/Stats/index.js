import { formatLargeNumbers } from "../../../utils/format";
import "./style.css";

const Stats = ({ data }) => {
  return (
    <section id="stats-section">
      <div className="stats-content">
        <div className="stats-grid">
          <div className="column">
          </div>
          <div className="column">
            <div>
              <p>Prev. Close</p>
              <p>{data.previousClose || "--"}</p>
            </div>
            <div>
              <p>Open</p>
              <p>{data.open || "--"}</p>
            </div>
          </div>
          <div className="column">
            <div>
              <p>High</p>
              <p>{data.high || "--"}</p>
            </div>
            <div>
              <p>Low</p>
              <p>{data.low || "--"}</p>
            </div>
          </div>
          <div className="column">
            <div>
              <p>52 Week High</p>
              <p>{data.week52High || "--"}</p>
            </div>
            <div>
              <p>52 Week Low</p>
              <p>{data.week52Low || "--"}</p>
            </div>
          </div>
          <div className="column">
            <div>
              <p>Volume</p>
              <p>{formatLargeNumbers(data.latestVolume) || "--"}</p>
            </div>
            <div>
              <p>Avg. Volume</p>
              <p>{formatLargeNumbers(data.avgTotalVolume) || "--"}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Stats;
