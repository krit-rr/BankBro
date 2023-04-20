import Chart from "react-apexcharts";

import { setSeries, setOptions } from "./chart-settings";
import "./style.css";

const DataChart = ({ data, priceChange }) => {
  const series = setSeries(data);
  const options = setOptions(priceChange);

  return (
    <section id="chart-section">
      
      <Chart
        options={options}
        series={series}
        type="area"
        height={450}
        width="100%"
      />
    </section>
  );
};

export default DataChart;
