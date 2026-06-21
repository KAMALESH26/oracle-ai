import { useEffect, useState } from "react";
import axios from "axios";

function ForecastTable() {

  const [forecast, setForecast] =
    useState([]);

  useEffect(() => {

    axios.get(
      "http://127.0.0.1:5000/api/forecast"
    )
    .then(res => {

      setForecast(
        res.data
      );

    })
    .catch(console.error);

  }, []);

  return (

    <div style={{ padding: "20px" }}>

      <h2>
        Forecasted Trends
      </h2>

      <table border="1">

        <thead>

          <tr>

            <th>Keyword</th>
            <th>Current</th>
            <th>Predicted</th>

          </tr>

        </thead>

        <tbody>

          {
            forecast
            .slice(0, 10)
            .map((item, index) => (

              <tr key={index}>

                <td>
                  {item.keyword}
                </td>

                <td>
                  {item.current}
                </td>

                <td>
                  {item.predicted_mentions}
                </td>

              </tr>

            ))
          }

        </tbody>

      </table>

    </div>
  );
}

export default ForecastTable;