import {
  Line
} from "react-chartjs-2";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Legend
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Legend
);

function TrendGrowthChart() {

  const data = {

    labels: [

      "Mon",
      "Tue",
      "Wed",
      "Thu",
      "Fri",
      "Sat",
      "Sun"
    ],

    datasets: [

      {

        label:
        "Trend Growth",

        data:
        [12,18,27,22,35,42,50],

        borderColor:
        "#60A5FA",

        tension: 0.4
      }
    ]
  };

  return (

    <div
      style={{
        background:"#111827",
        padding:"20px",
        borderRadius:"12px",
        marginBottom:"30px"
      }}
    >

      <h2>
        Trend Growth
      </h2>

      <Line data={data} />

    </div>
  );
}

export default TrendGrowthChart;