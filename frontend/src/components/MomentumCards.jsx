import { useEffect, useState } from "react";
import axios from "axios";

function MomentumCards() {

  const [data, setData] =
    useState([]);

  useEffect(() => {

    axios
      .get(
        "http://127.0.0.1:5000/api/momentum"
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
        Momentum Leaders
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
                Growth:
                {" "}
                {item.growth}%
              </p>

              <p>
                Momentum:
                {" "}
                {item.momentum}
              </p>

            </div>

          ))
        }

      </div>

    </div>
  );
}

export default MomentumCards;