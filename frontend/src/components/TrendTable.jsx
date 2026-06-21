import { useEffect, useState } from "react";
import axios from "axios";

function TrendTable() {

  const [trends, setTrends] =
    useState([]);

  useEffect(() => {

    axios.get(
      "http://127.0.0.1:5000/api/trends"
    )
    .then(res => {

      setTrends(
        res.data
      );

    });

  }, []);

  return (

    <div
      style={{
        padding: "20px"
      }}
    >

      <h2>
        Top Trends
      </h2>

      <table>

        <tbody>

          {
            trends.slice(0,10).map(
              (
                trend,
                index
              ) => (

                <tr key={index}>

                  <td>
                    {trend.keyword}
                  </td>

                  <td>
                    {trend.mentions}
                  </td>

                </tr>

              )
            )
          }

        </tbody>

      </table>

    </div>
  );
}

export default TrendTable;