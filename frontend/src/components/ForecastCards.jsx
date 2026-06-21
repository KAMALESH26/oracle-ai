import { useEffect, useState } from "react";
import axios from "axios";

function ForecastCards() {

  const [data,setData] =
    useState([]);

  useEffect(() => {

    axios
      .get(
        "http://127.0.0.1:5000/api/forecast"
      )
      .then(res => {

        setData(
          res.data
        );

      });

  }, []);

  return (

    <div>

      <h2>
        Forecasted Trends
      </h2>

      <div
        style={{

          display:"grid",

          gridTemplateColumns:
          "repeat(auto-fit,minmax(220px,1fr))",

          gap:"20px",

          marginBottom:"30px"
        }}
      >

        {
          data
          .slice(0,6)
          .map((item,index)=>(

            <div

              key={index}

              style={{

                background:"#111827",

                padding:"20px",

                borderRadius:"12px"
              }}
            >

              <h3>
                {item.keyword}
              </h3>

              <p>
                Current:
                {" "}
                {item.current}
              </p>

              <p>
                Predicted:
                {" "}
                {item.predicted_mentions}
              </p>

            </div>

          ))
        }

      </div>

    </div>
  );
}

export default ForecastCards;