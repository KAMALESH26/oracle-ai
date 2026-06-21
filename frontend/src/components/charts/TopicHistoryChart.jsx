import {
  useEffect,
  useState
} from "react";

import axios from "axios";

import {
  Line
} from "react-chartjs-2";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement
);

function TopicHistoryChart() {

  const [history,setHistory] =
    useState([]);

  useEffect(() => {

    axios

      .get(
        "http://127.0.0.1:5000/api/topic-history/Generative%20AI"
      )

      .then(res => {

        setHistory(
          res.data
        );

      });

  }, []);

  const data = {

    labels:

      history.map(
        h => h.time
      ),

    datasets: [

      {

        label:
        "Generative AI",

        data:

          history.map(
            h => h.mentions
          ),

        borderColor:
        "#60A5FA",

        tension:0.4
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
        Topic Growth
      </h2>

      <Line
        data={data}
      />

    </div>
  );
}

export default TopicHistoryChart;