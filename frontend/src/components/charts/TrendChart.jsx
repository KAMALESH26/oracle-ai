import {
  useEffect,
  useState
} from "react";

import axios from "axios";

function TrendCards() {

  const [trends,setTrends] =
    useState([]);

  useEffect(() => {

    axios
      .get(
        "http://127.0.0.1:5000/api/trends"
      )
      .then(res => {

        setTrends(
          res.data
        );
      });

  }, []);

  return (

    <div>

      <h2>
        Top Trends
      </h2>

      <div
        style={{

          display:"grid",

          gridTemplateColumns:
          "repeat(auto-fit,minmax(220px,1fr))",

          gap:"20px",

          marginTop:"20px",

          marginBottom:"30px"
        }}
      >

        {
          trends
          .slice(0,8)
          .map((trend,index)=>(

            <div

              key={index}

              style={{

                background:"#111827",

                padding:"20px",

                borderRadius:"12px"
              }}
            >

              <h3>

                {
                  trend.keyword
                }

              </h3>

              <p>

                Mentions:
                {" "}
                {
                  trend.mentions
                }

              </p>

            </div>

          ))
        }

      </div>

    </div>
  );
}

export default TrendCards;