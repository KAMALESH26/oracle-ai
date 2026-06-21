import { useEffect, useState } from "react";
import axios from "axios";

function MomentumTable() {

  const [momentum, setMomentum] =
    useState([]);

  useEffect(() => {

    axios.get(
      "http://127.0.0.1:5000/api/momentum"
    )
    .then(res => {

      setMomentum(
        res.data
      );

    })
    .catch(console.error);

  }, []);

  return (

    <div style={{ padding: "20px" }}>

      <h2>
        Momentum Leaders
      </h2>

      <table border="1">

        <thead>

          <tr>

            <th>Keyword</th>
            <th>Growth %</th>
            <th>Momentum</th>

          </tr>

        </thead>

        <tbody>

          {
            momentum
            .slice(0, 10)
            .map((item, index) => (

              <tr key={index}>

                <td>
                  {item.keyword}
                </td>

                <td>
                  {item.growth}
                </td>

                <td>
                  {item.momentum}
                </td>

              </tr>

            ))
          }

        </tbody>

      </table>

    </div>
  );
}

export default MomentumTable;